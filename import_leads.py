import xmlrpc.client

#configuration
url= "http://localhost:8069"
db= "crm"
username= "azaroualzineb07@gmail.com"
password= "Heerre--21 admin"

#connexion
common= xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid= common.authenticate(db, username, password, {})
models= xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

#creer un lead
lead_id= models.execute_kw(db, uid, password, 'crm.lead', 'create', [{
    'name': 'Atlas Distribution - ERP License',
    'contact_name': 'Youssef Benali',
    'email_from': 'y.benali@atlas-dist.ma',
    'phone': '+212 6 12 34 56 78',
    'expected_revenue': 120000,
    'probability': 30,

}])

