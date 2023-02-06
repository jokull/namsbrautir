import json
from typing import ContextManager
from pathlib import Path
from contextlib import contextmanager


from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine("sqlite:///./.db", poolclass=SingletonThreadPool)
_Session = sessionmaker(bind=engine, autoflush=True)


from models import Base, Programme, Exam, Course, School, programme_courses


@contextmanager
def session_scope() -> ContextManager[Session]:
    """Provide a transactional scope around a series of operations."""
    session = _Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def get_or_create_school(db, id):
    school = db.query(School).get(id)
    if school is None:
        school = School(id=id)
        db.add(school)
        db.commit()
    return school


def get_or_create_exam(db, items):
    exam = db.query(Exam).get(items["_id"])
    if exam is None:
        exam = Exam(
            id=items["_id"],
            **{
                k: v
                for k, v in items.items()
                if k
                in (
                    "title",
                    "level",
                    "maximum_credits",
                    "minimum_credits",
                    "number",
                )
            }
        )
        db.add(exam)
        db.commit()
    return exam


def main(db: Session):
    for filename in Path(".dumps").iterdir():
        data = json.loads(filename.read_text())
        programme = db.query(Programme).get(data["_id"])
        if programme is None:
            items = {k: v for k, v in data.items() if k in ("credits", "title")}
            serial = data["ministry_serial"]
            year_code, approval_code, ability_code, finish_code = serial.split("-")
            programme = Programme(
                id=data["_id"],
                serial=serial,
                year_code=year_code,
                approval_code=approval_code,
                ability_code=ability_code,
                finish_code=finish_code,
                courses=[],
                status=data["programme_type"]["status"],
                **items
            )

        programme.exam = get_or_create_exam(db, data["programme_type"]["exam"])

        schools = [get_or_create_school(db, id) for id in data["schools"]]
        for school in schools:
            programme.school = school

        for items in data["core"]:
            category = items.get("title")
            for data in items["courses"]:
                course = db.query(Course).get(data["_id"])
                if course is None:
                    course = Course(
                        id=data["_id"],
                        topics=data["topics"],
                        abbreviation=data["abbreviation"],
                        subject=data["subject"],
                        title=data["title"],
                        status=data["status"],
                        credits=data["credits"],
                        level=data["level"],
                        schools=[],
                    )

                schools = [get_or_create_school(db, id) for id in data["schools"]]
                for school in schools:
                    if school not in course.schools:
                        course.schools.append(school)

                if course not in programme.courses:
                    programme_course = db.query(programme_courses).filter_by(
                        programme_id=programme.id, course_id=course.id
                    )
                    if not programme_course:
                        ins = programme_courses.insert().values(
                            programme_id=programme.id,
                            course_id=course.id,
                            category=category,
                        )
                        db.get_bind().execute(ins)

                db.add(course)

        db.add(programme)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    with session_scope() as db:
        main(db)
