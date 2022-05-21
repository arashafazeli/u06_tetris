import sqlite3

CREATE_SCORES_TABLE = """CREATE TABLE IF NOT EXISTS scores (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    score_list score,
    status INTEGER default 1
);"""

INSERT_SCORE = "INSERT INTO scores (score_list) VALUES (?);"
MAX_SCORE = "SELECT max(score_list) FROM scores ;"


def get_max_score():
    with connection:
        result = connection.execute(MAX_SCORE,).fetchall()
        return result[0][0]


def create_tables():
    with connection:
        connection.execute(CREATE_SCORES_TABLE)


def add_score(score_list):
    with connection:
        connection.execute(INSERT_SCORE, (score_list,))


connection = sqlite3.connect("data_u06.db")
create_tables()
