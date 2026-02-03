# Django Project Setup

## Project Structure

```
.
├── config/              # Project settings and configuration
├── core/                # Main Django app
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
└── .gitignore          # Git ignore file
```

## Setup Instructions

### 1. Virtual Environment (Already Created)
A Python virtual environment has been created at `.venv/`

### 2. Install Dependencies
If setting up on a new machine:
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Edit the `.env` file with your settings:
- `DEBUG`: Set to `False` in production
- `SECRET_KEY`: Generate a new one for production
- `ALLOWED_HOSTS`: Add your domain names

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

The server will be available at `http://localhost:8000/`
Admin panel at `http://localhost:8000/admin/`

## Common Django Commands

- `python manage.py makemigrations` - Create migrations for model changes
- `python manage.py migrate` - Apply migrations
- `python manage.py startapp <app_name>` - Create a new app
- `python manage.py shell` - Open Python shell with Django context
- `python manage.py collectstatic` - Collect static files for production

## Adding the Core App to Settings

The `core` app has been created but needs to be added to `INSTALLED_APPS` in `config/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # Add this line
]
```

## Next Steps

1. Create models in `core/models.py`
2. Create views in `core/views.py`
3. Create URL patterns in `core/urls.py`
4. Update `config/urls.py` to include your app URLs
