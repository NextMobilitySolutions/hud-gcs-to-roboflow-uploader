# Example script to upload images from Google Cloud Storage to Roboflow.
# This script retrieves images from a specified GCS bucket, generates signed URLs for them,
# and uploads them to a specified Roboflow project.
## URL: https://docs.roboflow.com/datasets/adding-data/upload-data-from-aws-gcp-and-azure/google-cloud-storage

from google.cloud import storage
import requests
import urllib.parse

# ************* SET THESE VARIABLES *************
GCS_BUCKET_NAME = "YOUR_GCS_BUCKET_NAME"
ROBOFLOW_API_KEY = "YOUR_ROBOFLOW_API_KEY"
ROBOFLOW_PROJECT_NAME = "YOUR_ROBOFLOW_PROJECT_NAME"
GOOGLE_APPLICATION_CREDENTIALS = "path/to/your-service-account-file.json"
# ***********************************************

def get_gcs_signed_url(bucket_name: str, blob_name: str) -> str:
    """Generates a signed URL for a blob in Google Cloud Storage.
    Args:
        bucket_name (str): The name of the GCS bucket.
        blob_name (str): The name of the blob in the bucket.
    Returns:
        str: A signed URL that allows access to the blob.
    """
    storage_client = storage.Client.from_service_account_json(GOOGLE_APPLICATION_CREDENTIALS)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    url = blob.generate_signed_url(
        version="v4",
        expiration=3600, # 1 hour in seconds
        method="GET"
    )
    return url

def get_gcs_objects(bucket_name: str) -> list:
    '''
    Fetch the list of objects keys in the given GCS bucket.
    Args:
        bucket_name (str): The name of the GCS bucket.
    Returns:
        list: A list of blob names in the bucket.
    '''
    storage_client = storage.Client.from_service_account_json(GOOGLE_APPLICATION_CREDENTIALS)
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
    return [blob.name for blob in blobs]

def upload_to_roboflow(api_key: str, project_name: str, presigned_url: str, img_name='', split="train"):
    """Uploads an image to a Roboflow project using a presigned URL.
    Args:
        api_key (str): The API key for Roboflow.
        project_name (str): The name of the Roboflow project.
        presigned_url (str): The presigned URL of the image to upload.
        img_name (str, optional): The name to give the uploaded image. Defaults to the last part of the URL.
        split (str, optional): The dataset split to use (e.g., "train", "valid", "test"). Defaults to "train".
    Returns:
        bool: True if the upload was successful, False otherwise.
    """
    API_URL = "https://api.roboflow.com"
    if img_name == '':
        img_name = presigned_url.split("/")[-1]
    upload_url = "".join([
        API_URL + "/dataset/" + project_name + "/upload",
        "?api_key=" + api_key,
        "&name=" + img_name,
        "&split=" + split,
        "&image=" + urllib.parse.quote_plus(presigned_url),
    ])
    response = requests.post(upload_url)

    # Check if the upload was successful
    if response.status_code == 200:
        print(f"Successfully uploaded {img_name} to {project_name}")
        return True
    else:
        print(f"Failed to upload {img_name}. Error: {response.content.decode('utf-8')}")
        return False

if __name__ == "__main__":
    # Fetch the list of blobs in the GCS bucket
    available_blobs = get_gcs_objects(GCS_BUCKET_NAME)

    # Optional: Filter blobs if needed (e.g., by prefix)
    # available_blobs = [blob for blob in available_blobs if blob.startswith(PREFIX_FILTER)]

    # Upload each blob to Roboflow
    for blob in available_blobs:
        blob_url = get_gcs_signed_url(GCS_BUCKET_NAME, blob)
        upload_to_roboflow(ROBOFLOW_API_KEY, ROBOFLOW_PROJECT_NAME, blob_url)
