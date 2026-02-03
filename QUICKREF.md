# Quick Reference Guide

## Common Commands

### Docker

```bash
# Start services
docker compose up -d

# Stop services
docker compose down

# View logs
docker compose logs -f api

# Rebuild and start
docker compose up -d --build

# Execute command in container
docker compose exec api bash
```

### Database

```bash
# Run migrations
docker compose exec api alembic upgrade head

# Create new migration
docker compose exec api alembic revision --autogenerate -m "description"

# Access database
docker compose exec db psql -U postgres -d cashmeoutside_db

# Backup database
docker compose exec db pg_dump -U postgres cashmeoutside_db > backup.sql

# Restore database
docker compose exec -T db psql -U postgres cashmeoutside_db < backup.sql
```

### Development

```bash
# Format code
black .

# Lint code
ruff check .

# Type check
mypy app/

# Run tests
pytest

# Install pre-commit hooks
pre-commit install

# Run pre-commit hooks manually
pre-commit run --all-files
```

### Make Commands

```bash
make help          # Show available commands
make setup         # Initial setup
make up            # Start services
make down          # Stop services
make logs          # View logs
make shell         # API container shell
make db-shell      # Database shell
make migrate       # Run migrations
make revision      # Create new migration
make test          # Run tests
make lint          # Run linters
make format        # Format code
make clean         # Clean up
```

### API Endpoints

```bash
# Health check
curl http://localhost:8000/health

# Register user
curl -X POST http://localhost:8000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","username":"user","password":"password123"}'

# Login
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user&password=password123"

# Get current user (with token)
curl -X GET http://localhost:8000/api/v1/users/me \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Useful Scripts

```bash
# Create superuser
docker compose exec api python scripts/create_superuser.py

# Quick setup
./setup.sh

# Development helper
./dev.sh start
./dev.sh logs
./dev.sh test
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `POSTGRES_USER` | Database user | postgres |
| `POSTGRES_PASSWORD` | Database password | postgres |
| `POSTGRES_DB` | Database name | cashmeoutside_db |
| `JWT_SECRET_KEY` | JWT secret | changeme... |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry | 30 |
| `CORS_ORIGINS` | Allowed origins | localhost |

## File Structure

```
.
├── app/                    # Application code
│   ├── api/               # API routes
│   ├── core/              # Core config
│   ├── crud/              # Database operations
│   ├── db/                # Database session
│   ├── models/            # SQLAlchemy models
│   ├── schemas/           # Pydantic schemas
│   └── main.py            # Entry point
├── alembic/               # Migrations
├── tests/                 # Tests
├── scripts/               # Utility scripts
├── docker-compose.yml     # Docker config
├── Dockerfile             # Docker image
├── requirements.txt       # Dependencies
└── .env                   # Environment vars
```

## Troubleshooting

### Container won't start
```bash
docker compose down -v
docker compose up -d --build
```

### Database connection error
```bash
# Check database is running
docker compose ps

# Check logs
docker compose logs db
```

### Migration errors
```bash
# Reset database (warning: deletes data)
docker compose down -v
docker compose up -d
docker compose exec api alembic upgrade head
```

### Permission issues
```bash
sudo chown -R $USER:$USER .
```

## URLs

- API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- PostgreSQL: localhost:5432

## Port Numbers

- API: 8000
- PostgreSQL: 5432

## Default Credentials

**Database:**
- User: postgres
- Password: postgres
- Database: cashmeoutside_db

**⚠️ Change these in production!**

## Git Workflow

```bash
# Create feature branch
git checkout -b feature/your-feature

# Make changes and commit
git add .
git commit -m "feat: your feature"

# Push
git push origin feature/your-feature

# Create pull request on GitHub
```

## Testing

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_users.py

# Run with coverage
pytest --cov=app tests/

# Run with verbose output
pytest -v
```

## Monitoring

```bash
# Container stats
docker stats

# Container resource usage
docker compose ps

# View container logs
docker compose logs -f
```

## Security Notes

- Always change default passwords
- Generate new JWT secret key
- Use HTTPS in production
- Set specific CORS origins
- Keep dependencies updated
- Enable database SSL
- Use environment variables for secrets

## Performance Tips

- Use connection pooling
- Enable query caching
- Use indexes on frequently queried columns
- Monitor slow queries
- Use async operations
- Scale horizontally for high load

## Support

- Documentation: `/docs` endpoint
- GitHub Issues: Create an issue
- Email: support@example.com

## Version Info

Check versions:
```bash
# Python version
python --version

# FastAPI version
pip show fastapi

# Docker version
docker --version
```
