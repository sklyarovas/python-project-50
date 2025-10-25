import pytest

from gendiff import generate_diff


@pytest.fixture
def get_path():
    return 'tests/test_data/'


@pytest.mark.parametrize('data1, data2, result', [
    ('data1.json', 'data2.json', 'stylish.txt'),
    ('data1.yaml', 'data2.yml', 'stylish.txt'),
])
def test_default_diff(get_path, data1, data2, result):
    file1_path = get_path + data1
    file2_path = get_path + data2
    result_path = get_path + result
    default_diff = generate_diff(file1_path, file2_path)

    expected = open(result_path).read()
    assert default_diff == expected


@pytest.mark.parametrize('data1, data2, result', [
    ('data1.json', 'data2.json', 'stylish.txt'),
    ('data1.yaml', 'data2.yml', 'stylish.txt'),
])
def test_stylish_diff(get_path, data1, data2, result):
    output_format = 'stylish'
    file1_path = get_path + data1
    file2_path = get_path + data2
    result_path = get_path + result
    stylish_diff = generate_diff(file1_path, file2_path, output_format)

    expected = open(result_path).read()
    assert stylish_diff == expected


@pytest.mark.parametrize('data1, data2, result', [
    ('data1.json', 'data2.json', 'plain.txt'),
    ('data1.yaml', 'data2.yml', 'plain.txt'),
])
def test_plain_diff(get_path, data1, data2, result):
    output_format = 'plain'
    file1_path = get_path + data1
    file2_path = get_path + data2
    result_path = get_path + result
    plain_diff = generate_diff(file1_path, file2_path, output_format)

    expected = open(result_path).read()
    assert plain_diff == expected


@pytest.mark.parametrize('data1, data2, result', [
    ('data1.json', 'data2.json', 'json.txt'),
    ('data1.yaml', 'data2.yml', 'json.txt'),
])
def test_json_diff(get_path, data1, data2, result):
    output_format = 'json'
    file1_path = get_path + data1
    file2_path = get_path + data2
    result_path = get_path + result
    json_diff = generate_diff(file1_path, file2_path, output_format)

    expected = open(result_path).read()
    assert json_diff == expected


@pytest.mark.parametrize('data1, data2', [
    ('data1.json', 'data2.json'),
])
def test_unknown_output(get_path, data1, data2):
    output_format = 'text'
    file1_path = get_path + data1
    file2_path = get_path + data2
    result = generate_diff(file1_path, file2_path, output_format)

    expected = 'Unknown output format, expected: stylish, plain, json'
    assert result == expected


@pytest.mark.parametrize('data1, data2', [
    ('data1.html', 'data2.json'),
])
def test_unknown_input(get_path, data1, data2):
    output_format = 'json'
    file1_path = get_path + data1
    file2_path = get_path + data2
    result = generate_diff(file1_path, file2_path, output_format)

    expected = 'Unknown input format, expected: json, yaml, yml'
    assert result == expected


@pytest.mark.parametrize('data1, data2', [
    ('data1.json', 'data2.yaml'),
])
def test_file_not_found(get_path, data1, data2):
    output_format = 'json'
    file1_path = get_path + data1
    file2_path = get_path + data2
    result = generate_diff(file1_path, file2_path, output_format)

    expected = 'File not found: tests/test_data/data2.yaml'
    assert result == expected
