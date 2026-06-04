from connect import execute

def create_allocation(employee_id, holiday_status_id,number_of_days, notes='') :
    allocation_id = execute('hr.leave.allocation', 'create',[{
        'employee_id' : employee_id,
        'holiday_status_id' : holiday_status_id,
        'number_of_days' : number_of_days,
        'notes' : notes
    }])
    print(f"Allocation ceated successufully for the employee's id : {employee_id}")
    return allocation_id


if __name__ == "__main__":
    create_allocation(
        employee_id=2,
        holiday_status_id=1,  # Paid Time Off
        number_of_days=15,
        notes='Allocation annuelle 2026'
    )