.PHONY: help build up down restart logs shell db-shell migrate test lint format clean install

help:
	@echo "Available commands:"
	@echo "  make build       - Build Docker images"
	@echo "  make up          - Start all services"
	@echo "  make down        - Stop all services"
	@echo "  make restart     - Restart all services"
	@echo "  make logs        - View logs"
	@echo "  make shell       - Access API container shell"
	@echo "  make db-shell    - Access database shell"
	@echo "  make migrate     - Run database migrations"
	@echo "  make revision    - Create new migration"
	@echo "  make test        - Run tests"
	@echo "  make lint        - Run linters"
	@echo "  make format      - Format code"
	@echo "  make clean       - Clean up containers and volumes"
	@echo "  make install     - Install dependencies locally"

build:
	docker compose build

up:
	docker compose up -d
	@echo "Services started. API available at http://localhost:8000"
	@echo "API docs at http://localhost:8000/docs"

down:
	docker compose down

restart:
	docker compose restart

logs:
	docker compose logs -f

shell:
	docker compose exec api /bin/bash

db-shell:
	docker compose exec db psql -U postgres -d cashmeoutside_db

migrate:
	docker compose exec api alembic upgrade head

revision:
	@read -p "Enter migration message: " msg; \
	docker compose exec api alembic revision --autogenerate -m "$$msg"

test:
	docker compose exec api pytest tests/ -v

test-local:
	pytest tests/ -v

lint:
	black --check .
	ruff check .
	mypy app/

format:
	black .
	ruff check --fix .

clean:
	docker compose down -v
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +

install:
	pip install -r requirements.txt
	pre-commit install

setup: install
	cp .env.example .env
	@echo "Setup complete! Edit .env with your configuration."
	@echo "Run 'make up' to start the services."
