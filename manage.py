#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import ssl

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'subscription_manager.settings')
    try:
        from django.core.management import execute_from_command_line
        from django.core.management.commands.runserver import Command as RunserverCommand
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Add HTTPS support for the development server
    if "runserver" in sys.argv:
        cert_file = "cert.pem"
        key_file = "key.pem"
        if os.path.exists(cert_file) and os.path.exists(key_file):
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ssl_context.load_cert_chain(certfile=cert_file, keyfile=key_file)
            RunserverCommand.default_ssl_context = ssl_context
        else:
            print("Warning: SSL certificates not found. Run the following to generate them:")
            print("openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes")

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
