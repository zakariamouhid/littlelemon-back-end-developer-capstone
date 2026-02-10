# Little Lemon Backend Developer Capstone (Coursera Meta Back-End Developer Capstone)

A Django REST API project for the Little Lemon restaurant management system. This is a capstone project for the Coursera **Meta Back-End Developer Capstone** course.

## Project Overview

Little Lemon is a restaurant management backend system built with Django. The project provides both a REST API and a frontend interface for managing restaurant operations, including menu items, table bookings, and user management. The system features token-based authentication, comprehensive API endpoints, and a user-friendly web interface.

## Technologies Used

- **Django 4.2** - Web framework
- **Django REST Framework** - REST API toolkit
- **Djoser** - Authentication and user management
- **Python 3.8-3.13** - Programming language (Python 3.13 recommended)
- **MySQL/MariaDB 10.3+** - Database (configured for MySQL with mysqlclient)
- **Pipenv** - Dependency management
- **Token Authentication** - Secure API access

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8-3.13** (Python 3.13 recommended)
  - ⚠️ **Important**: Python 3.14 is NOT supported due to compatibility issues with Django 4.2
  - Check your Python version: `python --version` or `py --version`
  - Download Python 3.13 from [python.org downloads](https://www.python.org/downloads/)
- **Pipenv** (install with `pip install pipenv`)
- **MySQL Server 5.7+ or MariaDB 10.3+** (for database)
- **MySQL client libraries** (mysqlclient package will be installed via Pipenv)
- **Windows users**: If using MariaDB, you may need to install the MariaDB connector and set the DLL path (see `manage.py` for Windows-specific configuration)

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

8. **Populate the menu with sample data (optional)**
   ```bash
   python manage.py populate_menu
   ```
   
   To clear existing items and repopulate:
   ```bash
   python manage.py populate_menu --clear
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
   - API: `http://127.0.0.1:8000/api/`
   - Frontend: `http://127.0.0.1:8000/restaurant/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

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
│   ├── models.py         # Database models (Menu, Booking)
│   ├── views.py          # Frontend view functions
│   ├── admin.py          # Admin configuration
│   ├── apps.py           # App configuration
│   ├── urls.py           # App URL configuration
│   ├── test_models.py    # Model unit tests
│   ├── tests.py          # Additional unit tests
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
  - Database models (`Menu`, `Booking`)
  - Frontend template rendering (`index.html`, `about.html`, `menu.html`, `book.html`)
  - Static files (CSS, images)
  - Admin configuration for models
  - Management command (`populate_menu`) for seeding menu data
- **URLs**: 
  - `/restaurant/` - Homepage
  - `/restaurant/about/` - About page
  - `/restaurant/menu/` - Menu page
  - `/restaurant/book/` - Table booking page (with user registration, login, and authentication support)

### `LittleLemonAPI` App
- **Purpose**: REST API endpoints
- **Contains**:
  - API view classes (MenuViewSet, BookingViewSet, UserViewSet, etc.)
  - DRF serializers (MenuSerializer, BookingSerializer, UserSerializer)
  - API URL routing
- **URLs**: `/api/` (all API endpoints)
- **Note**: Uses models from the `restaurant` app

This separation allows for:
- Clear separation between frontend and API concerns
- Independent scaling of API and frontend
- Better code organization and maintainability

## API Endpoints

All API endpoints are available under the `/api/` prefix:

### Menu
- `GET /api/menu/` - List all menu items
  - Returns: Array of menu items with `id`, `title`, `price`, `inventory`
- `POST /api/menu/` - Create a new menu item
  - Body: `{"title": "string", "price": "decimal", "inventory": integer}`
- `GET /api/menu/<id>/` - Retrieve a specific menu item
- `PUT /api/menu/<id>/` - Update a menu item (full update)
- `PATCH /api/menu/<id>/` - Partially update a menu item
- `DELETE /api/menu/<id>/` - Delete a menu item

**Response Formats**: JSON (default), XML, Browsable API

### Bookings (Tables)
- `GET /api/tables/` - List all bookings for the authenticated user (requires authentication)
  - Returns: Array of bookings (users can only see their own bookings)
- `POST /api/tables/` - Create a new booking (requires authentication)
  - Body: `{"name": "string", "no_of_guests": integer, "booking_date": "ISO datetime"}`
  - Note: The `user` field is automatically set to the authenticated user
- `GET /api/tables/<id>/` - Retrieve a specific booking (requires authentication)
- `PUT /api/tables/<id>/` - Update a booking (requires authentication)
- `PATCH /api/tables/<id>/` - Partially update a booking (requires authentication)
- `DELETE /api/tables/<id>/` - Delete a booking (requires authentication)

**Note**: All booking endpoints require token authentication. Users can only access their own bookings.

### Users
- `GET /api/users/` - List all users
  - Returns: Array of users with `url`, `username`, `email`, `groups`
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

### Frontend Pages
- `GET /restaurant/` - Frontend homepage
- `GET /restaurant/about/` - About page
- `GET /restaurant/menu/` - Menu page
- `GET /restaurant/book/` - Table booking page
  - Supports token-based authentication via session storage
  - User registration form (for new users)
  - Login form (for existing users)
  - Interactive booking form (requires authentication)
  - View and manage user bookings
  - POST endpoint for token management (`store_token`, `clear_token`)

## Authentication

The API uses Token Authentication. To access protected endpoints:

1. **Get an authentication token:**
   ```bash
   # Using curl
   curl -X POST -d "username=your_username&password=your_password" http://127.0.0.1:8000/api-token-auth/
   
   # Or using JSON
   POST /api-token-auth/
   Content-Type: application/json
   
   {
     "username": "your_username",
     "password": "your_password"
   }
   ```

2. **Use the token in requests:**
   ```bash
   # Using curl
   curl -H "Authorization: Token <your_token_here>" http://127.0.0.1:8000/api/tables/
   
   # Or in headers
   Authorization: Token <your_token_here>
   ```

**Alternative: Djoser Authentication**

You can also use Djoser for user management:
- **Register**: `POST /auth/users/`
  ```json
  {
    "username": "newuser",
    "email": "user@example.com",
    "password": "securepassword"
  }
  ```
- **Login**: `POST /auth/token/login/`
- **Logout**: `POST /auth/token/logout/`

**Frontend Token Management**

The booking page (`/restaurant/book/`) supports token management via session storage:
- Store token: `POST /restaurant/book/` with `{"action": "store_token", "token": "your_token"}`
- Clear token: `POST /restaurant/book/` with `{"action": "clear_token"}`

**User Registration on Booking Page**

The booking page (`/restaurant/book/`) includes a user registration form that allows new users to:
- Create an account with username, email, and password
- Automatically log in after successful registration
- Start making bookings immediately

Users can toggle between the login and registration forms. The registration form validates:
- Password confirmation match
- Minimum password length (8 characters)
- Unique username and email (handled by the API)

## Database Models

### Menu
- `id` (AutoField, Primary Key)
- `title` (CharField, max_length=255)
- `price` (DecimalField, max_digits=10, decimal_places=2)
- `inventory` (IntegerField)

### Booking
- `id` (AutoField, Primary Key)
- `user` (ForeignKey to User, CASCADE delete, related_name='bookings')
- `name` (CharField, max_length=255)
- `no_of_guests` (IntegerField)
- `booking_date` (DateTimeField)

**Note**: The Booking model requires a user relationship. When creating bookings via API, the user is automatically set to the authenticated user.

## Management Commands

### populate_menu

Populates the database with sample menu items.

```bash
# Populate menu (creates new items, updates existing ones)
python manage.py populate_menu

# Clear existing items and repopulate
python manage.py populate_menu --clear
```

This command creates 15 sample Mediterranean cuisine items including:
- Greek Salad, Bruschetta, Grilled Fish, Pasta Carbonara
- Lemon Dessert, Mediterranean Pizza, Lamb Kebab
- And more...

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

The project includes comprehensive unit tests for both models and API endpoints.

#### Test Coverage

**Model Tests** (`restaurant/test_models.py`):
- Menu model tests:
  - Creation and field validation
  - String representation
  - Decimal price handling
- Booking model tests:
  - Creation and field validation
  - String representation
  - Various guest count scenarios

**API Endpoint Tests** (`LittleLemonAPI/tests.py`):
- Menu API:
  - GET, POST, PUT, PATCH, DELETE operations
  - Invalid data handling
  - Non-existent resource handling
- Bookings API:
  - Authenticated and unauthenticated access
  - CRUD operations
  - Authentication requirements
- Secured View:
  - Authentication verification
- User ViewSet:
  - User listing and retrieval
  - User creation

#### Running All Tests

```bash
python manage.py test
```

#### Running Tests with Verbose Output

To see detailed test names and results:

```bash
python manage.py test --verbosity=2
```

#### Running Specific Test Suites

```bash
# Run only model tests
python manage.py test restaurant.test_models

# Run only API tests
python manage.py test LittleLemonAPI.tests

# Run a specific test class
python manage.py test restaurant.test_models.MenuTest

# Run a specific test method
python manage.py test restaurant.test_models.MenuTest.test_menu_item_creation
```

#### Test Database

Django automatically creates a separate test database (prefixed with `test_`) when running tests. This ensures:
- Your development database is never modified
- Tests run in isolation
- Each test starts with a clean database state
- The test database is automatically destroyed after tests complete

**Note**: All datetime objects in tests use timezone-aware datetimes to avoid warnings.

### Accessing the Django Admin

1. Create a superuser (if you haven't already):
   ```bash
   python manage.py createsuperuser
   ```

2. Start the development server and navigate to:
   `http://127.0.0.1:8000/admin/`

## Configuration

### Database Configuration

The project is currently configured to use MySQL. The database settings are in `littlelemon/settings.py`:

- **Database Name**: `littlelemon_backend_capstone`
- **Host**: `127.0.0.1`
- **Port**: `3306`
- **User**: `root`
- **Password**: (empty by default)
- **SQL Mode**: `STRICT_TRANS_TABLES` (enforced via init_command)

**Important**: Make sure MySQL/MariaDB is installed and running on your system before running migrations. You may need to create the database manually:

```sql
CREATE DATABASE littlelemon_backend_capstone;
```

**To use SQLite for development instead**, update the `DATABASES` setting in `littlelemon/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Windows-Specific Configuration

The `manage.py` file includes a Windows-specific fix for MariaDB connector DLL loading:

```python
if os.name == 'nt':
    os.add_dll_directory(r"C:\mariadb-connector\lib")
```

If you're using MariaDB on Windows and encounter DLL loading issues, ensure the MariaDB connector is installed at the specified path, or update the path in `manage.py` to match your installation.

### REST Framework Configuration

The project uses Django REST Framework with the following settings:

- **Renderers**: JSON (default), XML, Browsable API
- **Authentication**: Token Authentication, Session Authentication
- **Permissions**: AllowAny (default, can be overridden per view)
- **Pagination**: Not configured (returns all results by default)

### Djoser Configuration

Djoser is configured to use `username` as the user ID field:

```python
DJOSER = {"USER_ID_FIELD": "username"}
```

### Environment Variables

For production, consider using environment variables for sensitive settings like:
- `SECRET_KEY`
- `DEBUG`
- Database credentials
- API keys

Create a `.env` file in the project root (this file should be in `.gitignore`). You can use packages like `python-decouple` or `django-environ` to load environment variables.

**Security Note**: The current `SECRET_KEY` in `settings.py` is for development only. **Never commit production secrets to version control.**

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

### MariaDB/MySQL Connection Issues

If you encounter connection errors:

1. **Verify MySQL/MariaDB is running:**
   ```bash
   # On Windows
   net start MySQL
   # Or check services
   ```

2. **Verify database exists:**
   ```sql
   SHOW DATABASES;
   CREATE DATABASE IF NOT EXISTS littlelemon_backend_capstone;
   ```

3. **Check user permissions:**
   ```sql
   GRANT ALL PRIVILEGES ON littlelemon_backend_capstone.* TO 'root'@'localhost';
   FLUSH PRIVILEGES;
   ```

4. **Windows DLL Issues**: If using MariaDB on Windows, ensure the connector DLL path in `manage.py` is correct.

## API Response Examples

### Get Menu Items
```json
GET /api/menu/

[
  {
    "id": 1,
    "title": "Greek Salad",
    "price": "12.99",
    "inventory": 50
  },
  {
    "id": 2,
    "title": "Bruschetta",
    "price": "8.99",
    "inventory": 40
  }
]
```

### Create Booking (Authenticated)
```json
POST /api/tables/
Authorization: Token <your_token>

{
  "name": "John Doe",
  "no_of_guests": 4,
  "booking_date": "2024-12-31T20:00:00Z"
}
```

### Get User's Bookings
```json
GET /api/tables/
Authorization: Token <your_token>

[
  {
    "id": 1,
    "user": 1,
    "name": "John Doe",
    "no_of_guests": 4,
    "booking_date": "2024-12-31T20:00:00Z"
  }
]
```

## Frontend Features

The project includes a complete frontend interface with:

- **Homepage** (`/restaurant/`): Restaurant introduction and featured content
- **About Page** (`/restaurant/about/`): Information about the restaurant
- **Menu Page** (`/restaurant/menu/`): Display of menu items
- **Booking Page** (`/restaurant/book/`): Interactive table booking form with:
  - User registration form (for new users without accounts)
  - Login form (for existing users)
  - Token-based authentication support
  - Session-based token storage
  - API integration for creating bookings
  - View and manage user's own bookings
  - Automatic login after registration
  - Logout functionality

All pages use Django templates with static file support (CSS, images).

## Dependencies

Key dependencies (see `Pipfile` for complete list):

- `django ~= 4.2.0` - Django web framework
- `djangorestframework` - REST API toolkit
- `djangorestframework-xml` - XML renderer support
- `djoser` - Authentication and user management
- `mysqlclient` - MySQL database connector

## Contributing

1. Create a feature branch
2. Make your changes
3. Test your changes (run `python manage.py test`)
4. Ensure all tests pass
5. Submit a pull request

## License

This project is part of the Coursera **Meta Back-End Developer Capstone** course curriculum.

## Support

For issues and questions, please refer to the course materials or contact your instructor.

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Djoser Documentation](https://djoser.readthedocs.io/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

