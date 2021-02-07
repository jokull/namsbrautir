# Staðfestar námsbrautalýsingar

https://mms.is/stadfestar-namsbrautalysingar

Project to fetch and load data into SQLite for further analysis.

```
poetry install
mkdir .dumps
# To download the JSON
poetry run scrapy runspider spider.py
# To load into SQLite
poetry run python load.py
# To start Datasette
poetry run datasette .db
```
