# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose the port the application runs on
EXPOSE 5000

# Define environment variables
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432
ENV POSTGRES_DB=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=Jexon192005

# Run the application
CMD ["python", "main.py"]
