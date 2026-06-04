from connect import execute

result = execute('ir.model', 'search_read',
    [[['model', '=', 'hr.contract']]],
    {'fields': ['model', 'name']}
)
print(result)


#types = execute('hr.leave.type', 'search_read', [[]], {'fields': ['id', 'name']})
#for t in types:
    #print(t['id'], '-', t['name'])

#fields = execute('hr.leave', 'fields_get', [], {'attributes': ['string', 'type']})
#for f, v in fields.items():
    #print(f, '-', v['string'], '-', v['type'])

execute('hr.leave.allocation', 'action_approve', [[1]])
print("Allocation validée !")