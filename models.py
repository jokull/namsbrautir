from sqlalchemy import Column, Integer, String, Table, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


programme_courses = Table('programme_courses', Base.metadata,
    Column('programme_id', ForeignKey('programmes.id'), primary_key=True),
    Column('course_id', ForeignKey('courses.id'), primary_key=True),
    Column('category', Integer),
)


course_schools = Table('course_schools', Base.metadata,
    Column('course_id', ForeignKey('courses.id'), primary_key=True),
    Column('school_id', ForeignKey('schools.id'), primary_key=True),
)


class School(Base):
    __tablename__ = 'schools'
    id = Column(String, primary_key=True)

    courses = relationship('Course', secondary=course_schools)


class Exam(Base):
    __tablename__ = 'exams'
    id = Column(String, primary_key=True)
    title = Column(String)
    level = Column(Integer)
    maximum_credits = Column(Integer)
    minimum_credits = Column(Integer)
    number = Column(String)


class Course(Base):
    __tablename__ = 'courses'
    id = Column(String, primary_key=True)
    category = Column(Integer)
    topics = Column(String)
    abbreviation = Column(String)
    subject = Column(String)
    title = Column(String)
    status = Column(String)
    credits = Column(Integer)
    level = Column(Integer)

    schools = relationship(School, secondary=course_schools)
    programmes = relationship("Programme", secondary=programme_courses)


class Programme(Base):
    __tablename__ = 'programmes'
    id = Column(String, primary_key=True)
    school_id = Column(String, ForeignKey('schools.id'))
    credits = Column(Integer)
    status = Column(String)
    title = Column(String)
    serial = Column(String)
    year_code = Column(Integer)
    approval_code = Column(Integer)
    ability_code = Column(Integer)
    finish_code = Column(Integer)

    courses = relationship(Course, secondary=programme_courses)
    school = relationship(School)

