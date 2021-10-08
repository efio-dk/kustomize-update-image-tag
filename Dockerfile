# Container image that runs your code
FROM python:3

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY action.py /action.py
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

# Code file to execute when the docker container starts up (`entrypoint.sh`)
CMD [ "python", "./action.py" ]