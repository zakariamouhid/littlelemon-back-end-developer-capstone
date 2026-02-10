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
   - API: http://127.0.0.1:8000/restaurant/
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
├── restaurant/           # Restaurant app
│   ├── __init__.py
│   ├── models.py         # Database models
│   ├── views.py          # View functions/classes
│   ├── admin.py          # Admin configuration
│   ├── apps.py           # App configuration
│   ├── urls.py           # App URL configuration
│   ├── tests.py          # Unit tests
│   └── migrations/       # Database migrations
├── manage.py             # Django management script
├── Pipfile               # Pipenv dependencies
├── Pipfile.lock          # Locked dependencies
├── TODO.md               # Project TODO list
└── README.md             # This file
```

## Current API Endpoints

- `GET /restaurant/` - Returns "Hello World" (basic test endpoint)

## Planned Features

See `TODO.md` for the current development roadmap. Planned features include:
- Food ordering API using the Menu API
- Table booking API for reserving tables on specific dates

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

