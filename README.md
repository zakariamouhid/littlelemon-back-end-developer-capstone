# Little Lemon Backend Developer Capstone

A Django REST API project for the Little Lemon restaurant management system. This is a capstone project for the Meta Front-End Developer course.

## Project Overview

Little Lemon is a restaurant management backend system built with Django. The project provides API endpoints for managing restaurant operations, including menu items, orders, and user management.

## Technologies Used

- **Django 4.2** - Web framework
- **Python 3** - Programming language
- **MySQL** - Database (configured for MySQL with mysqlclient)
- **Pipenv** - Dependency management

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Pipenv (install with `pip install pipenv`)
- MySQL Server (for database)
- MySQL client libraries (mysqlclient package will be installed via Pipenv)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd littlelemon-back-end-developer-capstone
   ```

2. **Install dependencies using Pipenv**
   ```bash
   pipenv install
   ```

3. **Activate the virtual environment**
   ```bash
   pipenv shell
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
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

## Contributing

1. Create a feature branch
2. Make your changes
3. Test your changes
4. Submit a pull request

## License

This project is part of the Meta Front-End Developer course curriculum.

## Support

For issues and questions, please refer to the course materials or contact your instructor.

