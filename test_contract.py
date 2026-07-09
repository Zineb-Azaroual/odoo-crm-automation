# colle ça dans check_models.py et lance
from connect import execute

fields = execute('hr.version', 'fields_get', [], {'attributes': ['string', 'type']})
for name, info in fields.items():
    print(f"  {name}: {info['type']} — {info['string']}")