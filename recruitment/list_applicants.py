from connect import execute


def list_applicant() :
    applicants = execute('hr.applicant', 'search_read', [[]], {
        'fields': ['partner_name', 'email_from', 'partner_phone', 'job_id', 'stage_id']
    })

    for e in applicants:
        job = e['job_id'][1] if e['job_id'] else ''
        stage = e['stage_id'][1] if e['stage_id'] else ''

        print(f"ID: {e['id']} | {e['partner_name']} | {e['email_from']} | "
              f"{e['partner_phone']} | {job} | {stage} ")

    return applicants


if __name__ == "__main__":
    list_applicant()