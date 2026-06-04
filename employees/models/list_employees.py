
from connect import execute

#list
def list_employees () :
    employees = execute('hr.employee', 'search_read', [[]],{
        'fields' : ['name', 'job_title', 'department_id'],
        'limit' : 20
    })
    print(f"{len(employees)} found")
    #department handling
    for e in employees :
        dept = e['department_id'][1] if e['department_id'] else 'Aucun'
        print(f"  ID: {e['id']} | {e['name']} | {e['job_title']} | Dept: {dept}")
    return employees

#filter by job
def filter_by_job(job_title) :
    employees = execute('hr.employee', 'search_read', [[['job_title', '=', job_title]]],
                        {        'fields' : ['name', 'job_title'],
    })
    print(f"Employees with the job : '{job_title}'")
    for e in employees :
        print(f" {e['name']}")
    return employees

#test
if __name__ == "__main__":
    list_employees()
    print("---")
    filter_by_job("Ingénieure MGSI")

