FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

RUN python manage.py collectstatic --noinput
RUN chmod -R 755 /app/static
# Expose port 80
EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]