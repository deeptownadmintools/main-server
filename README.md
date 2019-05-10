# Main server
[![Build Status](https://www.travis-ci.org/deeptownadmintools/main-server.svg?branch=master)](https://www.travis-ci.org/deeptownadmintools/main-server)


## Running the server
1) To run this application, you will need an API key for Rockbite's API. You can get one by contacting one of Rockbite's representatives on [Discord](https://discord.gg/jm6vJqG), or [Reddit](https://www.reddit.com/r/deeptown/).
1) Create a [virtual environment](https://docs.python.org/3/library/venv.html) with Python>=3.7 (older versions might work as well, but it was not tested)
1) Add these lines at the end of the activation script:
    ```
    export FLASK_APP=dtat
    export FLASK_DEBUG=1
    ```
1) Enter into virtual environment
1) Install requirements `pip install -e .`
1) Create a file named "privateConfig.py" within the "dtat" directory, and insert following line into this file:
    ```
    ROCKBITE_TOKEN = "Token you gained from Rockbite"
    ```
    You can also insert any other variables, which will rewrite the values in the defaultConfig.py.    
1) You will also need setup your database with:
    ```
    flask db upgrade
    ```
    If you are using the default SQLite DB it will be created implicitly. Otherwise, for example if you are using PostgreSQL, you will need to create the DB first.
1) You are now all set and you can start the server with following command:
    ```
    flask run
    ```
    This server will be running on default Flask port 5000 and it will be accessible only from localhost, which you can change by using `--port=5001` and `--host=0.0.0.0`

## Contributing
1) If you want to contribute to the main repository please ensure, that your code is following the PEP8 convention. You can do that with the use of flake8 and autopep8, which you can install using `pip install -r dev-requirements.txt`, after activating your virtual environment.
2) Also please make sure, that your code passes all current tests by running `python setup.py pytest`
3) If you create any new functionality please write tests for it

## Documentation
1) To generate documentation you will need to install requirements by `pip install -e .` and `pip install sphinx`.
1) Move into the `docs` directory and use `make html`
1) Your documentation is now generated in the `docs/build/html` directory

## API
If you would like to use current API methods or just view them, you can do so [here](https://documenter.getpostman.com/view/5414817/S1LsXq6g).

## Bugs & Improvements
If you have found a bug, or you have an idea for new feature please create an issue here on github. You can also contact me using email: [dtat@hampl.space](mailto:dtat@hampl.space)