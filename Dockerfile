FROM python:alpine

# Set the APP_HOME environment variable and
# update the PATH to include the directory for locally installed Python packages
ENV APP_HOME=/home/app PATH="/home/app/.local/bin:${PATH}"

# Create group "app" and user "app"
RUN addgroup -S app && adduser -S -G app -h ${APP_HOME} -s /bin/bash app

# Set the working directory in the container
WORKDIR $APP_HOME

# Switch to application user
USER app

# Copy the dependencies file to the working directory
COPY --chown=app:app requirements.txt $APP_HOME/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY --chown=app:app . .

# Specify the command to run the application
CMD ["python", "main.py"]
