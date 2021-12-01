FROM python:3.8-slim

WORKDIR /app

# Copy data, app and dependencies
COPY ./data/ ./data
COPY ./app.py ./app.py
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

ENTRYPOINT [ "streamlit", "run", "app.py" ] 


