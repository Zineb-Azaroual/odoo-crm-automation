
from connect import execute

def update_employee (employee_id, new_data) :
    result = execute('hr.employee', 'write',[
        [employee_id],
        new_data
    ])
    print(f" Employee updated with id : {employee_id}")
    return result

def archive_employee(employee_id) :
    result = execute('hr.employee', 'write', [
        [employee_id],
        {'active' : False}
    ])
    print(f" Employee {employee_id} is archived")
    return result

#test
if __name__ == "__main__":
    # Modifier le titre du poste
    update_employee(3, {'job_title': 'Développeuse ERP'})

    # Archiver un employé
    # archive_employee(1)