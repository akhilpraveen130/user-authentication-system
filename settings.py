# auth_project/settings.py
INSTALLED_APPS = [
    ...
    'accounts',  # Your new authentication app
    'django.contrib.auth',  # Handles user authentication
    'django.contrib.contenttypes',  # Required for permissions
    'django.contrib.sessions',  # Handles sessions
    'django.contrib.messages',  # Built-in messaging framework
    'django.contrib.staticfiles',
]