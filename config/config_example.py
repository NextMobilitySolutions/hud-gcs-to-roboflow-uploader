# This file is an example configuration file for the GCS to Roboflow uploader script.
# Replace the placeholder values with your actual configuration.
# This file should be renamed to `config.py` and placed in the same directory as the main script.

GCS_BUCKET_NAME = "your_bucket"
GCS_PREFIX = "silver/public/"
ROBOFLOW_API_KEY = "your_roboflow_api_key"
ROBOFLOW_PROJECT_NAME = "your_project_name"
DEFAULT_SPLIT = "train"
GOOGLE_APPLICATION_CREDENTIALS = "roboflow-gcs-key.json"
BATCH_NAME = "Uploaded via API"
