import unittest
import sqlite3
import database
import pytest


@pytest.fixture
def setup_database():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
	    CREATE TABLE IF NOT EXISTS scores (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    score_list score,
    status INTEGER default 1
);''')
    sample_data = [
        ('1', '120', '1'),
        ('2', '50', '1'),
    ]
    cursor.executemany('INSERT INTO scores VALUES(?, ?, ?)', sample_data)
    yield conn


def test_connection(setup_database):

    cursor = setup_database
    assert len(list(cursor.execute('SELECT * FROM scores'))) == 2


def test_scores_table():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
    	    CREATE TABLE IF NOT EXISTS scores (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        score_list score,
        status INTEGER default 1
);''')
    conn.commit()
    cursor.execute("SELECT * FROM scores;")
    data = cursor.fetchall()
    assert len(data) == 0
    conn.close()


class TestProject(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        c = self.conn.cursor()

        cmd = database.CREATE_SCORES_TABLE
        c.execute(cmd)

    def test_get_max_score(self):
        score_list = '120'
        cursor = self.conn.cursor()
        cursor.execute(database.INSERT_SCORE, (score_list,))
        cursor.execute(database.MAX_SCORE)
        result = cursor.fetchall()
        try:
            self.assertTrue(result)
        except Exception as ex:
            self.fail(f'GET DATA FROM MOVIE TABLE FAILED. TEST FAILED exception is: {ex}')

    def test_add_score(self):
        score_list = '100'
        cursor = self.conn.cursor()
        cursor.execute(database.INSERT_SCORE, (score_list,))
        try:
            self.conn.commit()
        except Exception as ex:
            self.fail(f'Add DATA TO MOVIE TABLE FAILED. TEST FAILED exception is: {ex}')