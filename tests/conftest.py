"""
Test configuration and fixtures
"""
import pytest
import asyncio
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app.core.config import settings
from app.db.session import Base

# Test database URL
from urllib.parse import urlparse, urlunparse

parsed_url = urlparse(settings.DATABASE_URL)
path_parts = parsed_url.path.rsplit('/', 1)
new_path = f"{path_parts[0]}/test_db" if len(path_parts) > 1 else "/test_db"
TEST_DATABASE_URL = urlunparse((
    parsed_url.scheme,
    parsed_url.netloc,
    new_path,
    parsed_url.params,
    parsed_url.query,
    parsed_url.fragment
))

# Create test engine
test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)

# Create test session factory
TestSessionLocal = async_sessionmaker(
    test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def setup_database():
    """Setup test database"""
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """Get test database session"""
    async with TestSessionLocal() as session:
        yield session
