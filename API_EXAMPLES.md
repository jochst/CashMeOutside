# API Usage Examples

This document provides examples of how to use the CashMeOutside API.

## Base URL

```
http://localhost:8000
```

## Health Check

Check if the API is running:

```bash
curl http://localhost:8000/health
```

Response:
```json
{
  "status": "healthy"
}
```

## Authentication

### Register a New User

```bash
curl -X POST "http://localhost:8000/api/v1/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john.doe@example.com",
    "username": "johndoe",
    "password": "SecureP@ssw0rd123",
    "full_name": "John Doe"
  }'
```

Response:
```json
{
  "id": 1,
  "email": "john.doe@example.com",
  "username": "johndoe",
  "full_name": "John Doe",
  "is_active": true,
  "is_superuser": false,
  "created_at": "2024-01-01T12:00:00.000000",
  "updated_at": null
}
```

### Login

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=johndoe&password=SecureP@ssw0rd123"
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

Save the `access_token` for subsequent requests.

## User Management

### Get Current User

```bash
curl -X GET "http://localhost:8000/api/v1/users/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Response:
```json
{
  "id": 1,
  "email": "john.doe@example.com",
  "username": "johndoe",
  "full_name": "John Doe",
  "is_active": true,
  "is_superuser": false,
  "created_at": "2024-01-01T12:00:00.000000",
  "updated_at": null
}
```

### Update Current User

```bash
curl -X PUT "http://localhost:8000/api/v1/users/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "John Michael Doe"
  }'
```

### List All Users (Superuser Only)

```bash
curl -X GET "http://localhost:8000/api/v1/users/?skip=0&limit=10" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Get User by ID (Superuser Only)

```bash
curl -X GET "http://localhost:8000/api/v1/users/1" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Update User by ID (Superuser Only)

```bash
curl -X PUT "http://localhost:8000/api/v1/users/1" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "is_active": false
  }'
```

### Delete User (Superuser Only)

```bash
curl -X DELETE "http://localhost:8000/api/v1/users/1" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Using Python Requests

### Install requests library

```bash
pip install requests
```

### Example Python script

```python
import requests

BASE_URL = "http://localhost:8000"

# Register a new user
def register_user():
    response = requests.post(
        f"{BASE_URL}/api/v1/users/",
        json={
            "email": "jane.doe@example.com",
            "username": "janedoe",
            "password": "SecureP@ssw0rd456",
            "full_name": "Jane Doe"
        }
    )
    return response.json()

# Login
def login(username, password):
    response = requests.post(
        f"{BASE_URL}/api/v1/auth/login",
        data={
            "username": username,
            "password": password
        }
    )
    return response.json()["access_token"]

# Get current user
def get_current_user(token):
    response = requests.get(
        f"{BASE_URL}/api/v1/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    return response.json()

# Usage
if __name__ == "__main__":
    # Register
    user = register_user()
    print(f"Registered user: {user['username']}")
    
    # Login
    token = login("janedoe", "SecureP@ssw0rd456")
    print(f"Access token: {token[:20]}...")
    
    # Get current user
    current_user = get_current_user(token)
    print(f"Current user: {current_user}")
```

## Using JavaScript (Node.js)

```javascript
const axios = require('axios');

const BASE_URL = 'http://localhost:8000';

// Register a new user
async function registerUser() {
    const response = await axios.post(`${BASE_URL}/api/v1/users/`, {
        email: 'bob@example.com',
        username: 'bob',
        password: 'SecureP@ssw0rd789',
        full_name: 'Bob Smith'
    });
    return response.data;
}

// Login
async function login(username, password) {
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);
    
    const response = await axios.post(
        `${BASE_URL}/api/v1/auth/login`,
        params
    );
    return response.data.access_token;
}

// Get current user
async function getCurrentUser(token) {
    const response = await axios.get(`${BASE_URL}/api/v1/users/me`, {
        headers: { Authorization: `Bearer ${token}` }
    });
    return response.data;
}

// Usage
(async () => {
    try {
        // Register
        const user = await registerUser();
        console.log('Registered user:', user.username);
        
        // Login
        const token = await login('bob', 'SecureP@ssw0rd789');
        console.log('Access token:', token.substring(0, 20) + '...');
        
        // Get current user
        const currentUser = await getCurrentUser(token);
        console.log('Current user:', currentUser);
    } catch (error) {
        console.error('Error:', error.response?.data || error.message);
    }
})();
```

## Error Responses

### 400 Bad Request

```json
{
  "detail": "Email already registered"
}
```

### 401 Unauthorized

```json
{
  "detail": "Could not validate credentials"
}
```

### 403 Forbidden

```json
{
  "detail": "Not enough permissions"
}
```

### 404 Not Found

```json
{
  "detail": "User not found"
}
```

### 422 Validation Error

```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "value is not a valid email address",
      "type": "value_error.email"
    }
  ]
}
```

## Interactive API Documentation

Access the interactive API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

These interfaces allow you to:
- Browse all available endpoints
- View request/response schemas
- Test API endpoints directly from the browser
- See detailed documentation for each endpoint
