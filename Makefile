install: 
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl

package-uninstall:
	python3 -m pip uninstall --yes dist/*.whl

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml tests/

lint:
	poetry run flake8 page_loader

build: check
	poetry build
