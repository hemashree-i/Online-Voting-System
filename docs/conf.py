import os
import sys

# Add your Django project's directory to the Python path
sys.path.insert(0, os.path.abspath('../'))

# Import your Django project's settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'electionproject.settings'
from django.conf import settings

# Configure Sphinx to use the django-sphinxdoc extension
extensions = ['sphinxdoc']

# Set the project and author information
project = 'Votecast'
author = 'Pranav S L'

# Set the output directory for the generated documentation
html_output_dir = '_build/html'

# Set the location of your project's source code
source_dir = 'C:\\Users\\prana\\OneDrive\\Votecast\\env'

# Set the location of your project's static files (e.g., CSS, JS, images)
static_dir = 'C:\\Users\\prana\\OneDrive\\Votecast\\env\\electionproject\\electionapp\\static'

# Set the master document
master_doc = 'index'

# Exclude the migrations directory from the documentation
exclude_patterns = ['*/migrations/*']
