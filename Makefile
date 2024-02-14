setup:
	pip install poetry
	poetry install

run:
	poetry run python ./new_project/manage.py runserver