#!/bin/bash
# Quick setup script for CashMeOutside

set -e

echo "🚀 CashMeOutside Quick Setup"
echo "=============================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "✅ .env file created. You can edit it to customize your configuration."
else
    echo "ℹ️  .env file already exists"
fi

# Build and start services
echo ""
echo "🔨 Building Docker images..."
docker compose build

echo ""
echo "🚀 Starting services..."
docker compose up -d

echo ""
echo "⏳ Waiting for database to be ready..."
until docker compose exec -T db pg_isready -U postgres > /dev/null 2>&1; do
    echo "Database is not ready yet. Waiting..."
    sleep 2
done
echo "✅ Database is ready!"

# Run migrations
echo ""
echo "🗄️  Running database migrations..."
docker compose exec -T api alembic upgrade head

echo ""
echo "✅ Setup complete!"
echo ""
echo "📍 Your API is now running at:"
echo "   - API: http://localhost:8000"
echo "   - Docs: http://localhost:8000/docs"
echo "   - ReDoc: http://localhost:8000/redoc"
echo ""
echo "🎯 Next steps:"
echo "   - View logs: docker compose logs -f"
echo "   - Access API shell: docker compose exec api /bin/bash"
echo "   - Stop services: docker compose down"
echo "   - Or use 'make' commands (run 'make help' for more info)"
echo ""
echo "Happy coding! 🎉"
