# Base image
FROM python:3.12-slim

# Working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy entire project
COPY . /app/

# Collect static files (for production)
RUN python manage.py collectstatic --noinput

# Expose the port
EXPOSE 8000

# Run the application
CMD ["gunicorn", "TechBridge.wsgi:application", "--bind", "0.0.0.0:8000"]
