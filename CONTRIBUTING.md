# Contributing to CashMeOutside

Thank you for your interest in contributing to CashMeOutside! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:
- A clear description of the bug
- Steps to reproduce the issue
- Expected vs actual behavior
- Your environment (OS, Python version, Docker version, etc.)

### Suggesting Features

We welcome feature suggestions! Please create an issue with:
- A clear description of the feature
- Use cases and benefits
- Any implementation ideas you might have

### Pull Requests

1. **Fork the repository** and create your branch from `main`

2. **Set up your development environment**
   ```bash
   git clone https://github.com/YOUR_USERNAME/CashMeOutside.git
   cd CashMeOutside
   make setup
   ```

3. **Make your changes**
   - Write clean, readable code
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

4. **Test your changes**
   ```bash
   # Run tests
   make test
   
   # Run linters
   make lint
   
   # Format code
   make format
   ```

5. **Commit your changes**
   - Use clear, descriptive commit messages
   - Follow conventional commits format:
     - `feat:` for new features
     - `fix:` for bug fixes
     - `docs:` for documentation changes
     - `test:` for test changes
     - `refactor:` for code refactoring
     - `chore:` for maintenance tasks

6. **Push to your fork and submit a pull request**

## Development Guidelines

### Code Style

- Follow PEP 8 style guide
- Use type hints wherever possible
- Write docstrings for all functions and classes
- Keep functions small and focused
- Use meaningful variable and function names

### Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for high test coverage
- Use pytest fixtures for common test setup

### Documentation

- Update README.md if needed
- Update DOCUMENTATION.md for significant changes
- Add docstrings to all new functions
- Update API_EXAMPLES.md for new endpoints

### Pre-commit Hooks

We use pre-commit hooks to ensure code quality. These will run automatically before each commit:

- **Black**: Code formatting
- **Ruff**: Linting
- **MyPy**: Type checking
- Various file checks

Install hooks with:
```bash
pre-commit install
```

Run manually with:
```bash
pre-commit run --all-files
```

## Project Structure

```
app/
├── api/          # API endpoints
├── core/         # Core functionality
├── crud/         # Database operations
├── db/           # Database connection
├── models/       # SQLAlchemy models
├── schemas/      # Pydantic schemas
└── utils/        # Utility functions

tests/            # Test suite
alembic/          # Database migrations
```

## Database Migrations

When making database changes:

1. Create a new migration:
   ```bash
   make revision
   ```

2. Review the generated migration file in `alembic/versions/`

3. Test the migration:
   ```bash
   make migrate
   ```

4. Include the migration file in your PR

## Running Tests

```bash
# Run all tests
make test

# Run specific test file
pytest tests/test_users.py -v

# Run with coverage
pytest --cov=app tests/
```

## Code Review Process

1. All PRs require at least one review
2. CI/CD checks must pass
3. Code must be formatted and linted
4. Tests must pass
5. Documentation must be updated

## Questions?

If you have questions, feel free to:
- Open an issue for discussion
- Reach out to the maintainers
- Check existing issues and PRs

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🎉
