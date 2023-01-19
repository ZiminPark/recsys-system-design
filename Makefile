PYTHON=3.9
BASENAME=$(shell basename $(CURDIR))

.PHONY: backend streamlit

setup:
	pre-commit install

format:
	black .
	isort .

lint:
	pytest backend --flake8 --mypy
	pytest streamlit --flake8 --mypy

utest:
	PYTHONPATH=src pytest test/utest --cov=src --cov-report=html --cov-report=term --cov-config=setup.cfg

cov:
	open htmlcov/index.html

backend:
	python3 backend/main.py

streamlit:
	streamlit run streamlit/demo.py

redis:
	redis-server --port 6379