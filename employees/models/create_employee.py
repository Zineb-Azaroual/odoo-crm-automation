
from connect import execute

def create_employee(name, job_title, department) :
    employee_id = execute('hr.employee', 'create', [{
        'name' : name,
        'job_title' : job_title,
        'department_id' : department
    }])
    print(f"Employee with id : {employee_id} is added successefully")
    return employee_id

# Test
if __name__ == "__main__":
    create_employee("Brahim Azraoual", "Consultant IT", False)