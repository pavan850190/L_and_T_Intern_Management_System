import pytest
import csv
"""imported csv file"""
res_file = open("intern.csv", "r")
list_of_lists = [(line.strip()) for line in res_file]
"""splited csv file data into list"""

@pytest.fixture
def expected_data1():
    expected_data = list_of_lists[0]
    return expected_data
    """adding fist person data """
    res_file.close()


@pytest.fixture
def expected_data2():
    expected_data2 = list_of_lists[2]
    return expected_data2
    res_file.close()


@pytest.fixture
def input_data1():
    return '99007476,pavan,22,pavan@gmail.com,123456'
    """ input data by user for testing """


@pytest.fixture
def input_data2():
    return '123456,ram,22,ram@mail,987654'


def test1(input_data1, expected_data1):
    assert expected_data1 == input_data1
    """testing the data"""


def test2(input_data2, expected_data2):
    assert expected_data2 == input_data2
