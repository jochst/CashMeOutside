#!/bin/bash
# Development helper script

set -e

show_help() {
    echo "CashMeOutside Development Helper"
    echo ""
    echo "Usage: ./dev.sh [command]"
    echo ""
    echo "Commands:"
    echo "  start         Start all services"
    echo "  stop          Stop all services"
    echo "  restart       Restart all services"
    echo "  logs          View logs"
    echo "  migrate       Run migrations"
    echo "  makemigration Create new migration"
    echo "  test          Run tests"
    echo "  format        Format code"
    echo "  lint          Lint code"
    echo "  shell         Access API container shell"
    echo "  db            Access database shell"
    echo "  clean         Clean up everything"
    echo "  help          Show this help"
    echo ""
}

case "$1" in
    start)
        echo "Starting services..."
        docker compose up -d
        echo "Services started! API at http://localhost:8000"
        ;;
    stop)
        echo "Stopping services..."
        docker compose down
        ;;
    restart)
        echo "Restarting services..."
        docker compose restart
        ;;
    logs)
        docker compose logs -f
        ;;
    migrate)
        echo "Running migrations..."
        docker compose exec api alembic upgrade head
        ;;
    makemigration)
        read -p "Enter migration message: " msg
        docker compose exec api alembic revision --autogenerate -m "$msg"
        ;;
    test)
        echo "Running tests..."
        docker compose exec api pytest tests/ -v
        ;;
    format)
        echo "Formatting code..."
        docker compose exec api black .
        ;;
    lint)
        echo "Linting code..."
        docker compose exec api ruff check .
        ;;
    shell)
        docker compose exec api /bin/bash
        ;;
    db)
        docker compose exec db psql -U postgres -d cashmeoutside_db
        ;;
    clean)
        echo "Cleaning up..."
        docker compose down -v
        find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
        find . -type f -name "*.pyc" -delete 2>/dev/null || true
        echo "Cleanup complete!"
        ;;
    help|*)
        show_help
        ;;
esac
