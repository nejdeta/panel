# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local code to the container image
COPY . /app/

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run script.py when the container launches
CMD ["python", "script.py"]
