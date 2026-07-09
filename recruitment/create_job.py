from connect import execute

#hr.job : Job Position / Job Opening

def create_job (name, department_id, no_of_recruitment=1) :
    job_id = execute('hr.job', 'create', [{
        'name': name,
        'department_id' : department_id,
        'no_of_recruitment' : no_of_recruitment, #The number of employees the company wants to hire for that job position.
    }]
                    )

    print(f"Job created succesefully with id : {job_id}")
    return job_id


if __name__ == "__main__":
    create_job(
        name='Data Engineer',
        department_id=1,   # ← obligatoire maintenant
        no_of_recruitment=2
    )