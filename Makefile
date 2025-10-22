install:
	uv sync

run:
	uv run gendiff

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml

check: test lint
