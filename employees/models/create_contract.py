
from connect import execute

def create_contract(employee_id, date_version, wage, contract_type='CDI'):
    contract_id = execute('hr.version', 'create', [{
        'name' : f'Contract {contract_type}',
        'employee_id' : employee_id,
        'date_version' : date_version,
        'wage' : wage,
        'contract_type' : contract_type
    }])

    print(f"Contract created successefully with id : '{contract_id}")
    return contract_id

#test
if __name__ == "__main__":
    create_contract(
        employee_id=4,
        date_version='2026-06-01',  # date future
        wage=8500.00,
        contract_type='CDI'
    )