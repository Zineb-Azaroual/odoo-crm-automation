from connect import execute

def create_leave(employee_id,holiday_status_id, date_from, date_to,notes="", validation_type="no_validation"):
    leave_id = execute('hr.leave', 'create', [{
        'employee_id' : employee_id,
        'holiday_status_id' : holiday_status_id,
        'date_from' : date_from,
        'date_to' : date_to,
        'notes': notes,

    }])
    print(f"Leave created succesefully for employee with id : {employee_id}")
    return leave_id

if __name__ == "__main__":
    create_leave(
        employee_id=2,
        holiday_status_id=1,  # ID du type de congé
        date_from='2026-06-10 08:00:00',
        date_to='2026-06-12 17:00:00',
        notes='Congé annuel'
    )