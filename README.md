
## Setting up a development environment

We assume that you have `git` and `virtualenv` and `virtualenvwrapper` installed.

    # Clone the code repository into whatever app of your choice
    mkdir -p ~/dev
    cd ~/dev
    git clone git@github.com:LeonDante-ctrl/blogger.git my_app

    # Create the virtual environment

    # Install required Python packages
    cd ~dantesblog
    pip install -r requirements.txt


## Initializing the Database

    # Create DB tables and populate the roles and users tables
    python app.py data.db

    # Or if you have Fabric installed:
    fab data.db


## Running the app

    # Start the Flask development web server
    python app.py


Point your web browser to http://localhost:5000/

You can make use of the following users:
- email `user@example.com` with password `Password1`.
- email `admin@example.com` with password `Password1`.


## See also

* [FlaskDash](https://github.com/twintechlabs/flaskdash) is a starter app for Flask
  with [Flask-User](https://readthedocs.org/projects/flask-user/)
  and [CoreUI](https://coreui.io/) (A Bootstrap Admin Template).

## Acknowledgements

With thanks to the following Flask extensions:

* [Alembic](http://alembic.zzzcomputing.com/)
* [Flask](http://flask.pocoo.org/)
* [Flask-Login](https://flask-login.readthedocs.io/)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/)
* [Flask-Script](https://flask-script.readthedocs.io/)
* [Flask-User](http://flask-user.readthedocs.io/en/v0.6/)


## Authors

- Leon Dante -- maxgamerdu@gmail.com