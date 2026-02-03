# CashMeOutside Cookiecutter Template

This is a cookiecutter template for creating FastAPI applications with all the modern tooling.

## Usage

```bash
pip install cookiecutter
cookiecutter https://github.com/jochst/CashMeOutside.git
```

## Template Variables

The following variables can be customized during project generation:

- `project_name`: Name of your project (default: CashMeOutside)
- `project_slug`: Python-friendly project name (auto-generated from project_name)
- `project_description`: Project description
- `author_name`: Your name
- `author_email`: Your email
- `version`: Initial version (default: 0.1.0)
- `python_version`: Python version to use (default: 3.11)
- `postgres_version`: PostgreSQL version (default: 16)
- `postgres_user`: PostgreSQL username (default: postgres)
- `postgres_password`: PostgreSQL password (default: postgres)
- `postgres_db`: PostgreSQL database name (auto-generated)
- `postgres_port`: PostgreSQL port (default: 5432)
- `api_port`: API port (default: 8000)
- `jwt_secret_key`: JWT secret key (default: changeme_secret_key_for_jwt_tokens)
- `jwt_algorithm`: JWT algorithm (default: HS256)
- `access_token_expire_minutes`: Token expiration time (default: 30)

## What's Included

- FastAPI application with JWT authentication
- PostgreSQL database with async/sync support
- Docker and Docker Compose configuration
- Alembic for database migrations
- Pre-commit hooks for code quality
- GitHub Actions CI/CD pipeline
- Comprehensive test suite
- API documentation
- Makefile for common tasks
- Setup scripts

## After Generation

1. Navigate to your project directory
2. Run `./setup.sh` or `make setup`
3. Edit `.env` with your configuration
4. Run `make up` to start the services
5. Access your API at http://localhost:8000/docs
