import pymysql
import pytest as pytest


@pytest.fixture(scope="class")
def setup(request):
    connection = pymysql.connect(host='localhost', user='root', password='qwerty', db='sys')
    cursor = connection.cursor()
    request.cls.cursor = cursor
    yield
    connection.close()
