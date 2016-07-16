import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, current_app

from . import settings
from .main import main


def create_app(settings_override=None):

    # Create application.
    app = Flask(
        import_name=__name__,
        static_folder=settings.STATIC_DIR,
        template_folder=settings.TEMPLATES_DIR
    )

    # Load configuration.
    app.config.from_object(settings)
    app.config.from_object(settings_override)

    # Register blueprints.
    app.register_blueprint(main)

    # Configure logging.
    if not app.config['TESTING']:
        configure_logging(app)

    return app


def configure_logging(app):

    # Create a file handler and set its level to DEBUG.
    file_handler = RotatingFileHandler(
        app.config['LOG_FILE'],
        maxBytes=10000,
        backupCount=7
    )
    file_handler.setLevel(logging.DEBUG)

    # Create a log formatter and set it to the file handler.
    format_str = '[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s'
    formatter = logging.Formatter(format_str, '%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger.
    app.logger.addHandler(file_handler)

    # Set the logger's level to DEBUG.
    app.logger.setLevel(logging.DEBUG)


def logger():
    return current_app.logger
