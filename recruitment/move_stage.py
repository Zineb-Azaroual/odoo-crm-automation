from connect import execute

#voir stages disponibles
def available_intenships():
    stages = execute('hr.recruitment.stage', 'search_read', [[]],
                    {'fields' : ['id', 'name']})
    return stages

def current_stage(applicant_id):
    current = execute('hr.applicant', 'search_read', [[('id', '=', applicant_id)]],
                      {'fields' : ['partner_name', 'stage_id']})
    return current

def move_stage(applicant_id):
    current = current_stage(applicant_id)
    current_stage_id = current[0]['stage_id'][0]
    stages = available_intenships()
    for index, stage in enumerate(stages):
        if stage['id'] == current_stage_id:
            if index + 1 < len(stages):
                next_stage_id = stages[index+1]['id']
                execute('hr.applicant', 'write', [[applicant_id], {'stage_id':next_stage_id}])
                print(f"The Applicant with id : {applicant_id} is moved to the stage : {next_stage_id} successefully")
            else:
                print("Applicant is already at the last stage !")

if __name__ == "__main__":
    move_stage(1)