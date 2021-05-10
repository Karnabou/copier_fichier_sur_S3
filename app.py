#  Transfert bidirectionel local/Bucket S3 - version 1.0
#   Importer les mudules
#  Importer render_template et notre dépendance Bootstrap

from flask import Flask, render_template, request, redirect, url_for, flash, \
    Response, session
from flask_bootstrap import Bootstrap
from filters import datetimeformat, file_type
from resources import get_bucket, get_buckets_list
from flask import json
from werkzeug.exceptions import HTTPException

# Configurer une nouvelle variable  d'application Flask

app = Flask(__name__)
# Création d'une nouvelle instance de bootstrap 
Bootstrap(app)
app.secret_key = 'secret'
# Moteur de modèle Jinja2
app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['file_type'] = file_type

# Mettre en place un chemin vers la page d'index ('/')
# Fonction index qui sera la page d'accueil
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        bucket = request.form['bucket']
        session['bucket'] = bucket
        return redirect(url_for('files'))
    else:
# Rendre index.html modéle avec buckets comme vaiable qui sera disponible pour le modèle 
        buckets = get_buckets_list()
        return render_template("index.html", buckets=buckets)

# Mettre en place une route vers le formulaire d'upload (files)
# Fonction Files pour lister les ficheiers
@app.route('/files')
def files():
    # Configuration d'une nouvelle variable résumés pour appeler les objets bucket
    my_bucket = get_bucket()
    summaries = my_bucket.objects.all()
# Rendre files.html modéle avec buckets et résumés comme vaiables qui seront disponible pour le modèle 
    return render_template('files.html', my_bucket=my_bucket, files=summaries)

#  Fonction gérer l'action du formulaire de téléchargement du local vers S3 (files.html) 
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    my_bucket = get_bucket()
    my_bucket.Object(file.filename).put(Body=file)

    flash('Fichier téléchargé avec succès')
  
    return redirect(url_for('files'))

# fonction de suppression des ficheirs du S3
@app.route('/delete', methods=['POST'])
def delete():
    key = request.form['key']

    my_bucket = get_bucket()
    my_bucket.Object(key).delete()

    flash('Fichier supprimé avec succès')
    return redirect(url_for('files'))

# fonction de téléchargement des fichiers du S3 vers le local.
@app.route('/download', methods=['POST'])
def download():
    key = request.form['key']

    my_bucket = get_bucket()
    file_obj = my_bucket.Object(key).get()

    return Response(
        file_obj['Body'].read(),
        mimetype='text/plain',
        headers={"Content-Disposition": "attachment;filename={}".format(key)}
    )

#fonction d'erreur
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Renvoyer JSON au lieu de HTML pour les erreurs HTTP."""
    # commencez avec les en-têtes et le code d'état corrects de l'erreur
    response = e.get_response()
    # remplacer le body par JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

# Lancer l'application
if __name__ == "__main__":
      app.run()
