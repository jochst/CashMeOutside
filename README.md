# CashMeOutside

CashMeOutside or cMo is a comprehensive, production-ready FastAPI boilerplate with Docker, PostgreSQL, JWT authentication, and modern Python tooling for building web applications.

## 🚀 Features

- **FastAPI** with uvicorn server for high-performance APIs
- **Docker & Docker Compose** for containerized development
- **PostgreSQL 16** with AsyncPG for async database operations
- **Sync DB connection** for development testing and migrations
- **JWT Authentication** with secure token-based auth
- **SQLAlchemy 2.0** ORM with both async and sync support
- **Pydantic v2** for data validation and settings management
- **Alembic** for database migrations
- **Pre-commit hooks** with Black, Ruff, and MyPy
- **CORS** middleware configuration
- **GitHub Actions** CI/CD workflows
- **Cookiecutter** template support

## 📦 Quick Start

```bash
# Clone the repository
git clone https://github.com/jochst/CashMeOutside.git
cd CashMeOutside

# Copy environment file
cp .env.example .env

# Start with Docker Compose
docker compose up -d

# Run migrations
docker compose exec api alembic upgrade head

# Access the API
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

## 📖 Documentation

See [DOCUMENTATION.md](DOCUMENTATION.md) for comprehensive documentation including:
- Detailed setup instructions
- API endpoints and usage examples
- Database migration guide
- Testing instructions
- Deployment guide
- Architecture overview

## 🏗️ Project Structure

```
app/                    # Application code
├── api/                # API routes and endpoints
├── core/               # Core functionality (config, security)
├── crud/               # Database operations
├── db/                 # Database session management
├── models/             # SQLAlchemy models
├── schemas/            # Pydantic schemas
└── main.py             # Application entry point

alembic/                # Database migrations
tests/                  # Test suite
.github/workflows/      # CI/CD pipelines
```

## 🔧 Development

```bash
# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install

# Run tests
pytest

# Format code
black .

# Lint code
ruff check .

# Type check
mypy app/
```

## 🐳 Docker Commands

```bash
# Build and start
docker compose up -d --build

# View logs
docker compose logs -f api

# Stop services
docker compose down

# Remove everything including volumes
docker compose down -v
```

## 📝 License

MIT License - see LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please read the contributing guidelines first.

## 📚 Learn More

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Docker Documentation](https://docs.docker.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/) 
