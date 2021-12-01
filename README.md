# streamlit-template-oss

Made with :heart: by [Intellify](https://intellify.com.au/)


## Running this sample app

### Run with docker-compose (Easiest and Cleanest):

**Pre-requisites**
* Docker installed and running
* docker-compose installed

```bash
$ docker-compose up

# When requirements.txt change and you need to force a rebuild
$ docker-compose up --build

# When finished
$ docker-compose down
```

### Run Natively:

**Pre-requisites**
* pip

```bash
$ pip install -r requirements.txt

$ streamlit run app.py
```

### Run with virtualenv:

**Pre-requisites**
* pip
* virtualenv

```bash
# first time only
$ virtualenv venv

$ source ./venv/bin/activate

$ pip install -r requirements.txt

$ streamlit run app.py
```

### Run with docker:
* Docker installed and running

```bash
# First build
$ docker build -t streamlit-app:latest .

# Subsequent builds
$ docker build --cache-from streamlit-app:latest -t streamlit-app:latest .

# To run as docker container with default streamlit port
$ docker run -p 8501:8501 streamlit-app:latest
```

You should be able to visit the app at http://localhost:8501

