Setup
-----

Prerequisites
~~~~~~~~~~~~~

Ensure you have the following setup::

- Python 2.7
- Virtualenv
- Heroku 
- Git/Github

For any help in getting the above setup see::

http://craigekerstiens.com


App Setup
~~~~~~~~~

::

    virtualenv --no-site-packages venv
    source venv/bin/activate
    pip install -r requirements.txt
    python app/manage.py syncdb


Running the app locally
~~~~~~~~~~~~~~~~~~~~~~~

::

    python app/manage.py runserver
    
