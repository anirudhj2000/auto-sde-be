# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /usr/src/app

# Install dependencies
RUN apt-get update && apt-get install -y netcat-openbsd pkg-config default-libmysqlclient-dev build-essential
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app/
COPY . /usr/src/app/

# Expose the port the app runs on
EXPOSE 8000

# Run the command to start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
