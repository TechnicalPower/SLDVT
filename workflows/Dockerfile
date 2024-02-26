# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /SLDVT

# Copy the current directory contents into the container at /app
COPY . /SLDVT

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Change the working directory to /app/src
WORKDIR /SLDVT/src

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run motion_capture.py when the container launches
CMD ["python", "motion_capture.py"]