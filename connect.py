import xmlrpc.client
from dotenv import load_dotenv #librairie Python qui lit ce fichier et charge les variables

import os


#configuration
# Force le chemin absolu
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path, override=True)

url = os.getenv("ODOO_URL")
db = os.getenv("ODOO_DB")
username = os.getenv("ODOO_USERNAME")
password = os.getenv("ODOO_PASSWORD")

#connexion
def get_connection():
    common= xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
    uid= common.authenticate(db, username, password, {})

    if not uid:
        raise Exception("Authentification echouce")
    models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
    #debuging
    print(f"Connecting to: {url} | db: {db} | user: {username}")

    return uid, models

def execute(model, method, args=None, kwargs=None):
    args = args or []
    kwargs = kwargs or {}
    uid, models = get_connection()
    return models.execute_kw(db, uid, password, model, method, args, kwargs)
