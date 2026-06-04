
# test_connection.py
from connect import execute

result = execute('crm.lead', 'search_read', [[]], {'fields': ['name'], 'limit': 3})
print("✅ Connexion OK !")
for r in result:
    print(f"  - {r['name']}")