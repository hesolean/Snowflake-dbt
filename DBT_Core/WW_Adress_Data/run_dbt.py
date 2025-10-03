from dotenv import load_dotenv
import os
import subprocess

# charge le .env
load_dotenv()

# exécute dbt debug
subprocess.run(["dbt", "debug"])

