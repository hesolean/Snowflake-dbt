import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# Charger les variables du .env
load_dotenv()

container_name = os.getenv("CONTENER_NAME")
base_url = os.getenv("URL")
connect_str = os.getenv("CONNECT_STR")

# Connexion Blob
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Période : janvier 2024 -> mois en cours
start = datetime(2024, 1, 1)
now = datetime.now()

# Boucle sur chaque mois
year, month = start.year, start.month
while (year < now.year) or (year == now.year and month <= now.month):
    file_name = f"yellow_tripdata_{year}-{month:02d}.parquet"
    url = f"{base_url}{file_name}"
    print(f"🔎 Vérification : {url}")

    response = requests.get(url)

    if response.status_code == 200:
        print(f"⬇️ Téléchargement réussi pour {file_name}")
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
        blob_client.upload_blob(response.content, overwrite=True)
        print(f"✅ Upload terminé : {file_name} → {container_name}")
    else:
        print(f"⚠️ Fichier non trouvé ({response.status_code}) : {file_name}")

    # Avancer au mois suivant
    month += 1
    if month > 12:
        month = 1
        year += 1
