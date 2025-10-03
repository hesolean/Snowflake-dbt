from dotenv import load_dotenv
import os
import subprocess

# charge le .env
load_dotenv()

# exécute dbt build
subprocess.run(["dbt", "build"])

