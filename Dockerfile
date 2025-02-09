# Use an official Python runtime as a base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Expose port 8000 for Django
EXPOSE 8000

# Install flake8 for linting
RUN pip install flake8

# Run flake8 for linting before starting the server
CMD ["sh", "-c", "flake8 && python manage.py runserver 0.0.0.0:8000"]
