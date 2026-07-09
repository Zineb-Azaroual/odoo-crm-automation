from connect import execute

def search_job(job_id):
    result = execute(
        'hr.job',
        'search',
        [[('id', '=', job_id)]]
    )
    return result

def update_job(job_id, data) :
    r = search_job(job_id)
    if r:
        result = execute('hr.job', 'write', [r, data])
        print(f" Job updated with id : {r}")
        return result
    else :
        print("JOB NOT FOUND !")


if __name__ == "__main__":
    # Test 1 — job qui existe
    print("=== Test update job existant ===")
    update_job(1, {'name': 'Data Engineer', 'no_of_recruitment': 3})

    # Test 2 — job qui n'existe pas
    print("\n=== Test update job inexistant ===")
    update_job(999, {'name': 'Ghost Job'})