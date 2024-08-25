# Flask PyCaret Anomaly Detection App

## Overview

This application provides anomaly detection for transactions using a PyCaret model. You can either input a single transaction or upload a CSV file with multiple transactions to get predictions. Developers can also access API documentation to integrate the service into their own applications.

## Project Structure

- **`Anomaly Detection`**: Main directory for anomaly detection features.
- **`static`**: Contains static files such as images.
- **`templates`**: HTML templates with CSS and Javascript used for rendering web pages.
  - **`api_doc.html`**: API documentation page (still in progress).
  - **`home.html`**: Home page for single transaction details.
  - **`multi.html`**: Page for uploading CSV files.
  - **`result.html`**: Page for displaying results and predictions.
- **`Dockerfile`**: Dockerfile used to build the Docker image for deployment.
- **`app.py`**: Flask application script.
- **`logs.log`**: Log file for application logs.
- **`runtime.txt`**: Specifies the runtime environment for the application.

## Deployment

The application is deployed on Google Cloud Platform's Cloud Run. You can access the live application at the following URL:

[https://flask-pycaret-app-fsdsx42qqq-as.a.run.app/](https://flask-pycaret-app-fsdsx42qqq-as.a.run.app/)

## Usage

### Single Transaction Prediction

1. Go to the [home page](https://flask-pycaret-app-fsdsx42qqq-as.a.run.app/).
2. Input your transaction details into the form.
3. Click the submit button to receive a prediction.

### CSV File Prediction

1. Navigate to the [CSV upload page](https://flask-pycaret-app-fsdsx42qqq-as.a.run.app/multi).
2. Upload your CSV file containing transaction details.
3. Download the processed file with an appended prediction column.

### API Documentation (For Developers)

- The API documentation is available at [api_doc.html](https://flask-pycaret-app-fsdsx42qqq-as.a.run.app/api_doc.html). Note that it is still in progress.

## Local Development

To run the application locally, follow these steps:

1. Build the Docker image:

   ```bash
   docker build -t flask-pycaret-app .
