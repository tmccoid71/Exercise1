# Use an official Python runtime as a base image
FROM python:3.11
FROM postgres:17

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port Django will be running on
EXPOSE 8000

# Set environment variables to configure Django to run inside Docker
ENV PYTHONUNBUFFERED=1

