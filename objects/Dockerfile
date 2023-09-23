# Base image
FROM python:3.9


# Environemnt varibales

# Set work directory  
ENV DockerHOME=/app
RUN mkdir -p $DockerHOME 
WORKDIR $DockerHOME 
COPY . $DockerHOME 

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements 
RUN pip install --upgrade pip 
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

