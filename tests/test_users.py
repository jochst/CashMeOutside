"""
Test user CRUD operations
"""
import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import user as crud_user
from app.schemas.user import UserCreate


@pytest.mark.asyncio
async def test_create_user(db_session: AsyncSession):
    """Test creating a user"""
    user_in = UserCreate(
        email="test@example.com",
        username="testuser",
        password="testpassword123",
        full_name="Test User"
    )
    
    user = await crud_user.create_user(db_session, user_in)
    
    assert user.email == "test@example.com"
    assert user.username == "testuser"
    assert user.full_name == "Test User"
    assert user.is_active is True
    assert user.is_superuser is False
    assert user.id is not None


@pytest.mark.asyncio
async def test_get_user_by_email(db_session: AsyncSession):
    """Test getting user by email"""
    user_in = UserCreate(
        email="test2@example.com",
        username="testuser2",
        password="testpassword123"
    )
    
    created_user = await crud_user.create_user(db_session, user_in)
    fetched_user = await crud_user.get_user_by_email(db_session, "test2@example.com")
    
    assert fetched_user is not None
    assert fetched_user.id == created_user.id
    assert fetched_user.email == "test2@example.com"


@pytest.mark.asyncio
async def test_authenticate_user(db_session: AsyncSession):
    """Test user authentication"""
    user_in = UserCreate(
        email="test3@example.com",
        username="testuser3",
        password="testpassword123"
    )
    
    await crud_user.create_user(db_session, user_in)
    
    # Test with correct password
    authenticated_user = await crud_user.authenticate_user(
        db_session,
        "testuser3",
        "testpassword123"
    )
    assert authenticated_user is not None
    assert authenticated_user.username == "testuser3"
    
    # Test with wrong password
    wrong_auth = await crud_user.authenticate_user(
        db_session,
        "testuser3",
        "wrongpassword"
    )
    assert wrong_auth is None
