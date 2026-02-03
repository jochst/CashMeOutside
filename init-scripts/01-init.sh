#!/bin/bash
# Database initialization script

set -e

echo "Creating database schema..."
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    -- Create extensions if needed
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    
    -- Add any initial schema here
    
EOSQL

echo "Database initialization completed!"
