import pytest

from databaseconnection.BaseClass import BaseClass
from databaseconnection.DatabaseConnection import DatabaseConnection


class TestDatabaseConnection(BaseClass):

    def test_insert_data(self):
        db = DatabaseConnection(self.cursor)
        db.insert_data('arun', 23, "Student_detail")
        db.insert_data('kutty', 23, "Student_detail")

    def test_retrieve_data(self):
        db = DatabaseConnection(self.cursor)
        db.retrieve_data("Student_detail")
