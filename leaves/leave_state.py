from connect import execute

def get_leave_state(leave_id):
    result = execute('hr.leave', 'search_read',
        [[['id', '=', leave_id]]],
        {'fields': ['id', 'name', 'employee_id', 'state', 'date_from', 'date_to']}
    )
    if result:
        leave = result[0]
        emp = leave['employee_id'][1] if leave['employee_id'] else 'Inconnu'
        print(f"📋 Congé ID  : {leave['id']}")
        print(f"   Employé   : {emp}")
        print(f"   Du        : {leave['date_from']}")
        print(f"   Au        : {leave['date_to']}")
        print(f"   State     : {leave['state']}")
    else:
        print(f"Aucun congé trouvé avec ID {leave_id}")

if __name__ == "__main__":
    get_leave_state(3)  # remplace par ton ID