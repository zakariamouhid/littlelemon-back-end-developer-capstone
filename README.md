# Little Lemon Backend Developer Capstone

A Django REST API project for the Little Lemon restaurant management system. This is a capstone project for the Meta Front-End Developer course.

## Project Overview

Little Lemon is a restaurant management backend system built with Django. The project provides API endpoints for managing restaurant operations, including menu items, orders, and user management.

## Technologies Used

- **Django 4.2** - Web framework
- **Python 3.8-3.13** - Programming language (Python 3.13 recommended)
- **MySQL/MariaDB 10.3+** - Database (configured for MySQL with mysqlclient)
- **Pipenv** - Dependency management

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8-3.13** (Python 3.13 recommended)
  - ⚠️ **Important**: Python 3.14 is NOT supported due to compatibility issues with Django 4.2
  - Check your Python version: `python --version` or `py --version`
  - Download Python 3.13 from https://www.python.org/downloads/
- Pipenv (install with `pip install pipenv`)
- MySQL Server 5.7+ or MariaDB 10.3+ (for database)
- MySQL client libraries (mysqlclient package will be installed via Pipenv)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd littlelemon-back-end-developer-capstone
   ```

2. **Verify Python version**
   ```bash
   python --version
   # Should show Python 3.8.x through 3.13.x (NOT 3.14+)
   ```
   
   On Windows, you can also use:
   ```bash
   py --list
   # This shows all installed Python versions
   ```

3. **Install dependencies using Pipenv**
   
   If you have Python 3.13 installed and it's in your PATH:
   ```bash
   pipenv install
   ```
   
   If Python 3.13 is installed but not in PATH, specify the full path:
   ```bash
   # On Windows, find the path first:
   py -3.13 -c "import sys; print(sys.executable)"
   
   # Then use that path:
   pipenv install --python "C:\Path\To\Python313\python.exe"
   ```
   
   **Note**: The `Pipfile` specifies `python_version = "3.13"`, but pipenv will use any compatible Python 3.8-3.13 version if 3.13 is not available.

4. **Activate the virtual environment**
   ```bash
   pipenv shell
   ```

5. **Verify the Python version in the virtual environment**
   ```bash
   python --version
   # Should show Python 3.13.x (or 3.8-3.12 if that's what was used)
   ```

6. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

## Running the Development Server

1. **Activate the virtual environment** (if not already activated)
   ```bash
   pipenv shell
   ```

2. **Start the development server**
   ```bash
   python manage.py runserver
   ```

3. **Access the application**
   - API: http://127.0.0.1:8000/api/
   - Frontend: http://127.0.0.1:8000/restaurant/
   - Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
littlelemon-back-end-developer-capstone/
├── littlelemon/          # Main project directory
│   ├── __init__.py
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main URL configuration
│   ├── wsgi.py           # WSGI configuration
│   └── asgi.py           # ASGI configuration
├── restaurant/           # Restaurant app (frontend views)
│   ├── __init__.py
│   ├── models.py         # Database models (MenuItem, Booking)
│   ├── views.py          # Frontend view functions
│   ├── admin.py          # Admin configuration
│   ├── apps.py           # App configuration
│   ├── urls.py           # App URL configuration
│   ├── tests.py          # Unit tests
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates
│   └── static/           # Static files (CSS, images)
├── LittleLemonAPI/       # API app (REST API endpoints)
│   ├── __init__.py
│   ├── models.py         # (empty - uses restaurant models)
│   ├── views.py          # API view classes
│   ├── serializers.py    # DRF serializers
│   ├── urls.py           # API URL configuration
│   ├── admin.py          # Admin configuration
│   ├── apps.py           # App configuration
│   └── tests.py          # Unit tests
├── manage.py             # Django management script
├── Pipfile               # Pipenv dependencies
├── Pipfile.lock          # Locked dependencies
├── TODO.md               # Project TODO list
└── README.md             # This file
```

## App Architecture

The project is organized into two main Django apps:

### `restaurant` App
- **Purpose**: Frontend views and database models
- **Contains**: 
  - Database models (`MenuItem`, `Booking`)
  - Frontend template rendering (`index.html`)
  - Static files (CSS, images)
  - Admin configuration for models
- **URLs**: `/restaurant/` (frontend homepage)

### `LittleLemonAPI` App
- **Purpose**: REST API endpoints
- **Contains**:
  - API view classes (MenuItemsView, BookingViewSet, UserViewSet, etc.)
  - DRF serializers (MenuItemSerializer, BookingSerializer, UserSerializer)
  - API URL routing
- **URLs**: `/api/` (all API endpoints)
- **Note**: Uses models from the `restaurant` app

This separation allows for:
- Clear separation between frontend and API concerns
- Independent scaling of API and frontend
- Better code organization and maintainability

## API Endpoints

All API endpoints are available under the `/api/` prefix:

### Menu Items
- `GET /api/menu-items/` - List all menu items
- `POST /api/menu-items/` - Create a new menu item
- `GET /api/menu-items/<id>/` - Retrieve a specific menu item
- `PUT /api/menu-items/<id>/` - Update a menu item (full update)
- `PATCH /api/menu-items/<id>/` - Partially update a menu item
- `DELETE /api/menu-items/<id>/` - Delete a menu item

### Bookings (Tables)
- `GET /api/tables/` - List all bookings (requires authentication)
- `POST /api/tables/` - Create a new booking (requires authentication)
- `GET /api/tables/<id>/` - Retrieve a specific booking (requires authentication)
- `PUT /api/tables/<id>/` - Update a booking (requires authentication)
- `PATCH /api/tables/<id>/` - Partially update a booking (requires authentication)
- `DELETE /api/tables/<id>/` - Delete a booking (requires authentication)

### Users
- `GET /api/users/` - List all users
- `POST /api/users/` - Create a new user
- `GET /api/users/<id>/` - Retrieve a specific user
- `PUT /api/users/<id>/` - Update a user (full update)
- `PATCH /api/users/<id>/` - Partially update a user
- `DELETE /api/users/<id>/` - Delete a user

### Authentication & Security
- `GET /api/secured-view/` - Protected view (requires authentication)
- `POST /api-token-auth/` - Obtain authentication token
- `POST /auth/users/` - User registration (Djoser)
- `POST /auth/token/login/` - Login and get token (Djoser)
- `POST /auth/token/logout/` - Logout (Djoser)

### Frontend
- `GET /restaurant/` - Frontend homepage

## Authentication

The API uses Token Authentication. To access protected endpoints:

1. **Get an authentication token:**
   ```bash
   POST /api-token-auth/
   Content-Type: application/json
   
   {
     "username": "your_username",
     "password": "your_password"
   }
   ```

2. **Use the token in requests:**
   ```bash
   Authorization: Token <your_token_here>
   ```

Alternatively, you can use Djoser for user management:
- Register: `POST /auth/users/`
- Login: `POST /auth/token/login/`
- Logout: `POST /auth/token/logout/`

## Planned Features

See `TODO.md` for the current development roadmap. Additional features may include:
- Enhanced food ordering functionality
- Advanced table booking features
- Order management system

## Development

### Creating Migrations

When you modify models, create migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Running Tests

```bash
python manage.py test
```

### Accessing the Django Admin

1. Create a superuser (if you haven't already):
   ```bash
   python manage.py createsuperuser
   ```

2. Start the development server and navigate to:
   http://127.0.0.1:8000/admin/

## Configuration

### Database Configuration

The project is currently configured to use MySQL. The database settings are in `littlelemon/settings.py`:

- **Database Name**: `littlelemon_backend_capstone`
- **Host**: `127.0.0.1`
- **Port**: `3306`
- **User**: `root`
- **Password**: (empty by default)

**Important**: Make sure MySQL is installed and running on your system before running migrations. You may need to create the database manually:

```sql
CREATE DATABASE littlelemon_backend_capstone;
```

To use SQLite for development instead, update the `DATABASES` setting in `littlelemon/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Environment Variables

For production, consider using environment variables for sensitive settings like:
- `SECRET_KEY`
- `DEBUG`
- Database credentials
- API keys

Create a `.env` file in the project root (this file is already in `.gitignore`).

## Troubleshooting

### Python Version Issues

If you encounter the error: `'super' object has no attribute 'dicts'`

This indicates you're using Python 3.14, which is incompatible with Django 4.2. 

**Solution**: 
1. Install Python 3.13 (or use Python 3.8-3.12 if already installed)
2. Remove the existing virtual environment:
   ```bash
   pipenv --rm
   # Or manually delete: C:\Users\YourName\.virtualenvs\littlelemon-back-end-developer-capstone-*
   ```
3. Create a new virtual environment with Python 3.13:
   ```bash
   pipenv install --python "C:\Path\To\Python313\python.exe"
   ```

### Database Version Issues

If you see: `MariaDB 10.5 or later is required`

Django 4.2 supports MariaDB 10.3+, so this error typically means you're using Django 5.2+ which requires MariaDB 10.5+. Ensure your `Pipfile` specifies `django = "~=4.2.0"`.

### Virtual Environment Issues

If pipenv says it didn't create the virtual environment:

1. Exit the current virtual environment:
   ```bash
   deactivate
   ```

2. Manually remove the virtual environment folder, then recreate it:
   ```bash
   pipenv install --python "C:\Path\To\Python313\python.exe"
   ```

## Contributing

1. Create a feature branch
2. Make your changes
3. Test your changes
4. Submit a pull request

## License

This project is part of the Meta Front-End Developer course curriculum.

## Support

For issues and questions, please refer to the course materials or contact your instructor.

