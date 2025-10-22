import pytest

from gendiff.main import core

@pytest.fixture
def get_path():
    return 'tests/test_data/'

def test_stylish_diff(get_path):
    format = 'stylish'
    file_path_1 =  get_path + 'data1.json'
    file_path_2 =  get_path + 'data2.json'
    result_path =  get_path + 'stylish.txt'
    stylish_diff = core(format, file_path_1, file_path_2)
    expected = open(result_path).read()
    assert stylish_diff == expected