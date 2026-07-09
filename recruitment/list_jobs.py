from connect import execute

#list
def list_jobs():
    jobs = execute('hr.job', 'search_read', [[]],
                   {'fields': ['name', 'department_id', 'no_of_recruitment']}
                   )

    for job in jobs:
        print(job)


if __name__ == "__main__":
    list_jobs()
