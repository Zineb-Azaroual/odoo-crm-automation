from connect import execute

#hr.applicant : A person's application for a job position

def create_applicant(partner_name, email_from, job_id, partner_phone=None, department_id=None, stage_id=None, user_id=None) :
    data = {
        'partner_name' : partner_name,
        'email_from' : email_from,
        'job_id': job_id,
        'active': True
    }
    if partner_phone:
        data['partner_phone'] = partner_phone
    if department_id:
        data['department_id'] = department_id
    if stage_id:
        data['stage_id'] = stage_id
    if user_id:
        data['user_id'] = user_id

    applicant_id = execute('hr.applicant', 'create', [data])

    print(f"Applicant added succesefully with id : {applicant_id}")
    return applicant_id


if __name__ == "__main__":
    create_applicant(
        "Brahim",
        "brahim@gmail.com",
        1,
        '069893'


    )

