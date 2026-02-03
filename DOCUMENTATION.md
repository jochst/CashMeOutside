# CashMeOutside - FastAPI Boilerplate

A comprehensive, production-ready FastAPI boilerplate with Docker, PostgreSQL, JWT authentication, and modern Python tooling.

## Features

- 🚀 **FastAPI** - Modern, fast web framework for building APIs
- 🐘 **PostgreSQL** - Powerful relational database
- 🔄 **AsyncPG** - High-performance async PostgreSQL driver
- 🔐 **JWT Authentication** - Secure token-based authentication
- 🗄️ **SQLAlchemy** - ORM with both async and sync support
- 📦 **Alembic** - Database migration tool
- 🐳 **Docker & Docker Compose** - Containerized development and deployment
- ✅ **Pydantic** - Data validation using Python type annotations
- 🎨 **Pre-commit Hooks** - Automated code formatting and linting
- 🔍 **CORS** - Cross-Origin Resource Sharing support
- 🤖 **GitHub Actions** - CI/CD pipeline
- 🍪 **Cookiecutter** - Project template for easy setup

## Tech Stack

- **Python 3.11+**
- **FastAPI 0.109+**
- **PostgreSQL 16**
- **SQLAlchemy 2.0**
- **Alembic**
- **Pydantic v2**
- **Docker & Docker Compose**

## Project Structure

```
.
├── app/                        # Application code
│   ├── api/                    # API routes
│   │   ├── v1/                 # API version 1
│   │   │   ├── endpoints/      # API endpoints
│   │   │   │   ├── auth.py     # Authentication endpoints
│   │   │   │   └── users.py    # User endpoints
│   │   │   └── api.py          # API router
│   │   └── dependencies.py     # API dependencies
│   ├── core/                   # Core functionality
│   │   ├── config.py           # Configuration
│   │   └── security.py         # Security utilities
│   ├── crud/                   # CRUD operations
│   │   └── user.py             # User CRUD
│   ├── db/                     # Database
│   │   └── session.py          # Database session
│   ├── models/                 # SQLAlchemy models
│   │   └── user.py             # User model
│   ├── schemas/                # Pydantic schemas
│   │   └── user.py             # User schemas
│   └── main.py                 # Application entry point
├── alembic/                    # Database migrations
│   ├── versions/               # Migration versions
│   ├── env.py                  # Alembic environment
│   └── script.py.mako          # Migration template
├── tests/                      # Tests
│   ├── conftest.py             # Test configuration
│   └── test_users.py           # User tests
├── init-scripts/               # Database initialization
│   └── 01-init.sh              # Init script
├── .github/                    # GitHub configuration
│   └── workflows/              # GitHub Actions
│       └── ci.yml              # CI/CD pipeline
├── docker-compose.yml          # Docker Compose configuration
├── Dockerfile                  # Docker image
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variables example
├── .pre-commit-config.yaml     # Pre-commit hooks
├── pyproject.toml              # Python project configuration
├── alembic.ini                 # Alembic configuration
└── cookiecutter.json           # Cookiecutter template
```

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)
- Git

### Quick Start with Docker

1. **Clone the repository**
   ```bash
   git clone https://github.com/jochst/CashMeOutside.git
   cd CashMeOutside
   ```

2. **Create environment file**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Start services with Docker Compose**
   ```bash
   docker compose up -d
   ```

4. **Run database migrations**
   ```bash
   docker compose exec api alembic upgrade head
   ```

5. **Access the API**
   - API: http://localhost:8000
   - Interactive API docs: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

### Local Development Setup

1. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

4. **Start PostgreSQL** (if not using Docker)
   ```bash
   # Make sure PostgreSQL is running on port 5432
   ```

5. **Run migrations**
   ```bash
   alembic upgrade head
   ```

6. **Start the development server**
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

### API Endpoints

#### Authentication

- `POST /api/v1/auth/login` - Login and get access token

#### Users

- `POST /api/v1/users/` - Register a new user
- `GET /api/v1/users/me` - Get current user (requires authentication)
- `PUT /api/v1/users/me` - Update current user (requires authentication)
- `GET /api/v1/users/` - List all users (requires superuser)
- `GET /api/v1/users/{user_id}` - Get user by ID (requires superuser)
- `PUT /api/v1/users/{user_id}` - Update user (requires superuser)
- `DELETE /api/v1/users/{user_id}` - Delete user (requires superuser)

### Example Usage

#### Register a new user

```bash
curl -X POST "http://localhost:8000/api/v1/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "johndoe",
    "password": "strongpassword123",
    "full_name": "John Doe"
  }'
```

#### Login

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=johndoe&password=strongpassword123"
```

#### Get current user

```bash
curl -X GET "http://localhost:8000/api/v1/users/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Database Migrations

### Create a new migration

```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply migrations

```bash
alembic upgrade head
```

### Rollback migrations

```bash
alembic downgrade -1
```

## Testing

### Run tests

```bash
pytest
```

### Run tests with coverage

```bash
pytest --cov=app tests/
```

## Code Quality

### Format code with Black

```bash
black .
```

### Lint with Ruff

```bash
ruff check .
```

### Type check with MyPy

```bash
mypy app/
```

### Run all pre-commit hooks

```bash
pre-commit run --all-files
```

## Environment Variables

Key environment variables (see `.env.example` for full list):

- `POSTGRES_USER` - PostgreSQL username
- `POSTGRES_PASSWORD` - PostgreSQL password
- `POSTGRES_DB` - PostgreSQL database name
- `DATABASE_URL` - Async database URL
- `SYNC_DATABASE_URL` - Sync database URL
- `JWT_SECRET_KEY` - Secret key for JWT tokens
- `JWT_ALGORITHM` - JWT algorithm (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiration time
- `CORS_ORIGINS` - Allowed CORS origins

## Docker Commands

### Build and start services

```bash
docker compose up -d --build
```

### View logs

```bash
docker compose logs -f
```

### Stop services

```bash
docker compose down
```

### Remove volumes

```bash
docker compose down -v
```

### Access database

```bash
docker compose exec db psql -U postgres -d cashmeoutside_db
```

## CI/CD

The project includes GitHub Actions workflows for:

- **Linting** - Black, Ruff, MyPy
- **Testing** - Pytest with PostgreSQL
- **Building** - Docker image build
- **Validation** - Docker Compose configuration

## Using Cookiecutter

To create a new project from this template:

```bash
pip install cookiecutter
cookiecutter https://github.com/jochst/CashMeOutside.git
```

Follow the prompts to customize your project.

## Security

- Passwords are hashed using bcrypt
- JWT tokens for authentication
- CORS configured for security
- Environment variables for sensitive data
- Input validation with Pydantic

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues and questions:
- Open an issue on GitHub
- Check the documentation at `/docs` endpoint

## Architecture

### Database

The project supports both **async** and **sync** database connections:

- **Async (AsyncPG)**: Used for all API endpoints for better performance
- **Sync (psycopg2)**: Used for Alembic migrations and development testing

### Authentication Flow

1. User registers via `/api/v1/users/` endpoint
2. User logs in via `/api/v1/auth/login` with credentials
3. Server returns JWT access token
4. Client includes token in `Authorization: Bearer <token>` header
5. Protected endpoints validate token and return user data

### CORS Configuration

CORS is configured in `app/core/config.py` and can be customized via the `CORS_ORIGINS` environment variable. Default allows:
- http://localhost:3000
- http://localhost:8000

## Best Practices

- Use async/await for database operations
- Validate all input with Pydantic schemas
- Follow RESTful API conventions
- Keep dependencies up to date
- Write tests for new features
- Use type hints everywhere
- Follow PEP 8 style guide (enforced by Black and Ruff)

## Troubleshooting

### Database connection issues

- Ensure PostgreSQL is running
- Check connection string in `.env`
- Verify database exists

### Migration issues

- Run `alembic upgrade head` after pulling changes
- Check Alembic version in `alembic/versions/`

### Docker issues

- Rebuild images: `docker compose up -d --build`
- Check logs: `docker compose logs -f api`
- Reset everything: `docker compose down -v && docker compose up -d --build`

## Roadmap

- [ ] WebSocket support
- [ ] Redis caching
- [ ] Email notifications
- [ ] OAuth2 social login
- [ ] Rate limiting
- [ ] GraphQL support
- [ ] Background tasks with Celery
- [ ] Multi-tenancy support

## Credits

Built with ❤️ using:
- FastAPI
- SQLAlchemy
- Pydantic
- Docker
- And many other great open-source projects
