# Importer le modèle os
#  Identification sur Bucket S3 - version 1.0
# Importer le modèle os
import os
# Récupérer les variables d'environnement liées à S3
S3_BUCKET = os.environ.get("S3_BUCKET")
S3_KEY = os.environ.get("S3_KEY")
S3_SECRET = os.environ.get("S3_SECRET")
