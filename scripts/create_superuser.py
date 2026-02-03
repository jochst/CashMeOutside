#!/usr/bin/env python
"""
Script to create a superuser
"""
import asyncio
import sys
import os
from getpass import getpass

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import AsyncSessionLocal
from app.crud import user as crud_user
from app.schemas.user import UserCreate


async def create_superuser():
    """Create a superuser interactively"""
    print("Create Superuser")
    print("=" * 50)
    
    # Get user input
    email = input("Email: ").strip()
    username = input("Username: ").strip()
    password = getpass("Password: ")
    password_confirm = getpass("Confirm Password: ")
    full_name = input("Full Name (optional): ").strip() or None
    
    # Validate input
    if not email or not username or not password:
        print("Error: Email, username, and password are required.")
        sys.exit(1)
    
    if password != password_confirm:
        print("Error: Passwords do not match.")
        sys.exit(1)
    
    # Create user
    async with AsyncSessionLocal() as db:
        try:
            # Check if user already exists
            existing_user = await crud_user.get_user_by_email(db, email=email)
            if existing_user:
                print(f"Error: User with email '{email}' already exists.")
                sys.exit(1)
            
            existing_user = await crud_user.get_user_by_username(db, username=username)
            if existing_user:
                print(f"Error: User with username '{username}' already exists.")
                sys.exit(1)
            
            # Create superuser
            user_in = UserCreate(
                email=email,
                username=username,
                password=password,
                full_name=full_name
            )
            
            user = await crud_user.create_user(db, user_in)
            
            # Make user a superuser
            user.is_superuser = True
            await db.commit()
            await db.refresh(user)
            
            print(f"\n✅ Superuser '{username}' created successfully!")
            print(f"ID: {user.id}")
            print(f"Email: {user.email}")
            print(f"Username: {user.username}")
            print(f"Full Name: {user.full_name}")
            
        except Exception as e:
            print(f"\n❌ Error creating superuser: {e}")
            sys.exit(1)


if __name__ == "__main__":
    asyncio.run(create_superuser())
