from connect import execute

#list
def list_leaves (employee_id = None) :
    domain = []
    if employee_id :
        domain = [[['employee_id', '=', employee_id]]]
    leaves = execute('hr.leave', 'search_read', domain, {
        'fields' : [
            'employee_id',
            'holiday_status_id',
            'date_from',
            'date_to',
            'notes',
            'state',
            'number_of_days'
        ],
        'limit' : 20,
    })

    #affichage
    print(f"{len(leaves)} leave found :\n")
    for leave in leaves :
        empl = leave['employee_id'][1] if leave['employee_id'] else 'Inconnu'
        type_leave = leave['holiday_status_id'][1] if leave['holiday_status_id'] else 'N/A'
        print(f"  ID: {leave['id']} | {empl} | {type_leave} | "
              f"{leave['date_from']} → {leave['date_to']} | "
              f"Statut: {leave['state']} | Jours: {leave['number_of_days']}")
    return leaves

if __name__ == "__main__":
    # Tous les congés
    list_leaves()

    # Congés d'un employé spécifique (remplace 1 par l'ID réel)
    # list_leaves(employee_id=1)