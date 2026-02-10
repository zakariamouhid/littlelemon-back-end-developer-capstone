#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# Force Python to look in your connector folder for DLLs
# this is a fix for windows
if os.name == 'nt':
    os.add_dll_directory(r"C:\mariadb-connector\lib")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'littlelemon.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
