### Tests and linter status, SQ status:
[![Actions Status](https://github.com/sklyarovas/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/sklyarovas/python-project-50/actions)
[![Check project](https://github.com/sklyarovas/python-project-50/actions/workflows/check-project.yml/badge.svg)](https://github.com/sklyarovas/python-project-50/actions/workflows/check-project.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=sklyarovas_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=sklyarovas_python-project-50)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=sklyarovas_python-project-50&metric=bugs)](https://sonarcloud.io/summary/new_code?id=sklyarovas_python-project-50)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=sklyarovas_python-project-50&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=sklyarovas_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=sklyarovas_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=sklyarovas_python-project-50)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=sklyarovas_python-project-50&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=sklyarovas_python-project-50)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=sklyarovas_python-project-50&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=sklyarovas_python-project-50)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=sklyarovas_python-project-50&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=sklyarovas_python-project-50)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=sklyarovas_python-project-50&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=sklyarovas_python-project-50)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=sklyarovas_python-project-50&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=sklyarovas_python-project-50)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=sklyarovas_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=sklyarovas_python-project-50)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=sklyarovas_python-project-50&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=sklyarovas_python-project-50)

### Setup

```bash
make install
make build
make package-install
```

### Run

```bash
gendiff -f {format} tests/test_data/{file1} tests/test_data/{file2}
```

### Development

```bash
make check
```

### Description

#### Консольная утилита для определения разницы между двумя файлами
* Поддерживаемые форматы вывода: stylish (default)

### Demo
* [stylish-for-json/yaml](https://asciinema.org/a/nnrlX6GxKZsbI86dYhkMGsJ2R)
