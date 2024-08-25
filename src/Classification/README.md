Classification/: Main directory containing all files related to the classification feature.

static/: Contains static files like the background image used in the web interface.

templates/: HTML template used for rendering the web pages.

index.html: The main page where users can input data for single record classification.
Dockerfile: This file contains the instructions to build a Docker image for deployment. It ensures the application can be easily deployed across different environments with consistent behavior.

Mushroom_Classification_220679Y: This is the notebook related to mushroom classification containing code related to creating a model

app.py: The main Flask application script. It handles routing, processing input data, calling the classification model, and rendering the appropriate HTML templates.

logs.log: A log file that records application logs, which is useful for debugging and monitoring the app's performance.

requirements.txt: This file lists all the Python dependencies required to run the application. Use it to set up your environment with the necessary packages.
