
from connect import execute

def create_contract(employee_id, date_start, wage):
    contract_id = execute('hr.version', 'create', [{
        'name' : f'Contract employee {employee_id}',
        'employee_id' : employee_id,
        'date_start' : date_start,
        'wage' : wage,
        #'contract_type' : contract_type
        'contract_type_id' : 1,
    }])

    print(f"Contract created successefully with id : '{contract_id}")
    return contract_id

#test
if __name__ == "__main__":
    create_contract(
        employee_id=2,
        date_start='2026-07-15',  # date future
        wage=9000.00,
        #contract_type='CDI'
    )