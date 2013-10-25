# site

This project houses the main django website.

## Installation

### Requirements

To install the required python modules using pypi:
    
    $ sudo pip install django boto python-social-auth

If we come across problematic versions of any required projects in the future, a virtualenv configuration will be required.

### Configuration

All settings for development purposes should go in    traded_io/traded_io/local_settings.py - the most important of which will be database and AWS-related.  Boto will naturally use whatever credentials are in ~/.boto but we should write the code based around the project-specific settings.

The main project settings file    traded_io/traded_io/settings.py will have empty string defaults and comments about what needs to be set in local_settings.

## Launching

The manage.py file is +x, so starting a development instance on your local machine should be as straightforward as

    $ cd traded_io
    $ ./manage.py runserver
