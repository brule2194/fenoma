# Dockerfile

# pull the official docker image
FROM python:3.11.5

# Set the working directory inside the container
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# Copy the requirements file to the working directory
COPY ./requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the application code to the working directory
COPY . .

# Run the FastAPI application using uvicorn server
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

