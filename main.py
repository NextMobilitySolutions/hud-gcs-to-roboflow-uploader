from google.cloud import storage
import requests
import urllib.parse
from config import *

def get_gcs_signed_url(bucket_name, blob_name):
    """Genera una URL firmada para acceder temporalmente a una imagen en GCS.
    Args:
        bucket_name (str): Nombre del bucket de GCS.
        blob_name (str): Nombre del blob (archivo) en el bucket.
    Returns:
        str: URL firmada que permite acceder al blob.
    """
    storage_client = storage.Client.from_service_account_json(GOOGLE_APPLICATION_CREDENTIALS)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    if blob is None:
        raise FileNotFoundError(f"Blob no encontrado: {blob_name}")

    return blob.generate_signed_url(version="v4", expiration=3600, method="GET")

def get_gcs_objects(bucket_name, prefix):
    """Obtiene los nombres de blobs dentro de un prefijo concreto.
    Args:
        bucket_name (str): Nombre del bucket de GCS.
        prefix (str): Prefijo para filtrar los blobs.
    Returns:
        list: Lista de nombres de blobs que terminan en .jpg, .jpeg o .png.
    """
    storage_client = storage.Client.from_service_account_json(GOOGLE_APPLICATION_CREDENTIALS)
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)

    return [blob.name for blob in blobs if blob.name.lower().endswith((".jpg", ".jpeg", ".png"))]

def upload_to_roboflow(api_key, project_name, presigned_url, img_name='', split="train"):
    """Sube una imagen a Roboflow usando su URL firmada.
    Args:
        api_key (str): Clave API de Roboflow.
        project_name (str): Nombre del proyecto en Roboflow.
        presigned_url (str): URL firmada de la imagen en GCS.
        img_name (str, optional): Nombre de la imagen a subir. Si no se proporciona, se usa el nombre del archivo de la URL.
        split (str, optional): Subconjunto al que se sube la imagen (train, valid, test). Por defecto es "train".
    Returns:
        bool: True si la subida fue exitosa, False en caso contrario.
        """
    API_URL = "https://api.roboflow.com"
    if not img_name:
        img_name = presigned_url.split("/")[-1]

    upload_url = "".join([
        f"{API_URL}/dataset/{project_name}/upload",
        "?api_key=" + api_key,
        "&name=" + img_name,
        "&split=" + split,
        "&image=" + urllib.parse.quote_plus(presigned_url),
    ])

    response = requests.post(upload_url)
    if response.status_code == 200:
        print(f"Subido: {img_name}")
        return True
    else:
        print(f"Error al subir {img_name}: {response.content.decode('utf-8')}")
        return False

if __name__ == "__main__":
    print("Buscando imágenes en GCS...")
    blobs = get_gcs_objects(GCS_BUCKET_NAME, GCS_PREFIX) # Filtra los blobs por el prefijo especificado.
    print(f"{len(blobs)} imágenes encontradas para subir.")
    for blob in blobs:
        try:
            url = get_gcs_signed_url(GCS_BUCKET_NAME, blob)
            upload_to_roboflow(ROBOFLOW_API_KEY, ROBOFLOW_PROJECT_NAME, url, img_name=blob, split=DEFAULT_SPLIT)
        except Exception as e:
            print(f"Error al procesar {blob}: {e}")
