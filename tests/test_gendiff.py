import pytest

from gendiff import generate_diff

@pytest.fixture
def get_path():
    return 'tests/test_data/'

@pytest.mark.parametrize('data1, data2, result', [
    ('data1.json', 'data2.json', 'stylish.txt'),
    ('data1.yaml', 'data2.yml', 'stylish.txt'),
])
def test_stylish_diff(get_path, data1, data2, result):
    output_format = 'stylish'
    file1_path =  get_path + data1
    file2_path =  get_path + data2
    result_path =  get_path + result
    stylish_diff = generate_diff(output_format, file1_path, file2_path)

    expected = open(result_path).read()
    assert stylish_diff == expected

@pytest.mark.parametrize('data1, data2, result', [
    ('data1.json', 'data2.json', 'plain.txt'),
    ('data1.yaml', 'data2.yml', 'plain.txt'),
])
def test_plain_diff(get_path, data1, data2, result):
    output_format = 'plain'
    file1_path =  get_path + data1
    file2_path =  get_path + data2
    result_path =  get_path + result
    plain_diff = generate_diff(output_format, file1_path, file2_path)

    expected = open(result_path).read()
    assert plain_diff == expected