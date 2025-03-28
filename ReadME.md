# Token Authentication in Django Channels and Websockets

This project implements token-based authentication for WebSocket connections using Django Channels. It includes a custom middleware for token validation, a WebSocket consumer for real-time messaging, and a REST endpoint for authentication tokens.

## Features
- Token-based WebSocket authentication.
- Custom middleware for token validation.
- Real-time messaging between authenticated users.
- Secure error handling for authentication failures.

## Prerequisites
- Python 3.8+
- Git
- Virtualenv (recommended)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/AliAffanBajwa/token-authentication.git
cd websocket_project
```

### 2. Set Up a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
```bash
python manage.py createsuperuser
```

## Configuration
- **Settings:** Defined in `websocket_project/settings.py`.
- **Token Middleware:** Validates tokens in `chat/middleware.py`.
- **Consumer:** Handles WebSocket connections in `chat/consumers.py`.

## Running the Project
```bash
# Using Django's development server
python manage.py runserver
```

## Usage

### 1. Create a User in Django Admin Panel
1. Create a super user: `python manage.py createsuperuser`
1. Run the server: `python manage.py runserver`
2. Open your browser and go to `http://localhost:8000/admin/`
3. Log in with the superuser credentials created earlier.
4. Navigate to **Users** and create a new user with a username and password.

### 2. Get an Authentication Token
```bash
curl -X POST -d "username=newuser&password=newpassword" http://localhost:8000/api/api-token-auth/
```
**Response:**
```json
{
    "token": "your-token-here",
    "user_id": 1,
    "username": "newuser"
}
```

### 3. Connect to WebSocket
Use Postman or WebSocket clients to connect:
```
ws://localhost:8000/ws/chat/?token=your-token-here
```
Expected response:
```json
{"message": "Welcome newuser! You are connected."}
```

## License
This project is open for learning purposes.

