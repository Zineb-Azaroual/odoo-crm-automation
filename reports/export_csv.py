import os

from connect import execute
from datetime import datetime

import csv

def export_employees_csv():
    #recover employees
    employees = execute('hr.employee', 'search_read', [[]], {
        'fields' : ['name', 'job_title','department_id', 'work_email', 'work_phone']
        })
    #create reports file if doesnt exist
    os.makedirs('reports', exist_ok=True)
    #file name
    filename = f"reports/employees_{datetime.now().strftime('%Y%m%d')}.csv"
    #columns
    fieldnames  = ['ID', 'Name' , 'Job Title', 'Department', 'Email', 'Phone']
    #open file
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()

        for emp in employees :
            writer.writerow({
                'ID': emp['id'],
                'Name': emp['name'],
                'Job Title': emp['job_title'] or '',
                'Department': emp['department_id'][1] if emp['department_id'] else '',
                'Email': emp['work_email'] or '',
                'Phone': emp['work_phone'] or ''
            })
        print(f"Employees exported to: {filename}")


def export_leaves_csv():
    #recover leaves
    leaves = execute('hr.leave', 'search_read', [[]], {
        'fields' : ['holiday_status_id', 'date_from','date_to', 'notes']
        })
    # create reports file if doesnt exist
    os.makedirs('reports', exist_ok=True)
    # file name
    filename = f"reports/leaves_{datetime.now().strftime('%Y%m%d')}.csv"
    #coulumns
    fieldnames = ['ID', 'Holiday Status', 'Date from', 'Date to', 'Notes']

    # open file
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()

        for leave in leaves:
            writer.writerow({
                'ID': leave['id'],
                'Holiday Status': leave['holiday_status_id'][1] if leave['holiday_status_id'] else '',
                'Date from': leave['date_from'] or '',
                'Date to': leave['date_to'] or '',
                'Notes': leave['notes'] or '',
            })
        print(f"Leaves exported to: {filename}")

def export_recruitments_csv():
    #recover applicants
    applicants = execute('hr.applicant', 'search_read', [[]], {
        'fields': ['partner_name', 'email_from', 'job_id', 'partner_phone', 'department_id', 'stage_id']
    })
    # create reports file if doesnt exist
    os.makedirs('reports', exist_ok=True)
    # file name
    filename = f"reports/recruitment_{datetime.now().strftime('%Y%m%d')}.csv"
    # coulumns
    fieldnames = ['ID', 'Partner Name', 'Email from', 'Job', 'Partner Phone', 'Department', 'Stage']

    # open file
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()

        for applicant in applicants:
            writer.writerow({
                'ID': applicant['id'],
                'Partner Name': applicant['partner_name'] or '',
                'Email from': applicant['email_from'] or '',
                #Many2one
                'Job': applicant['job_id'][1] if applicant['job_id'] else '',
                'Partner Phone': applicant['partner_phone'] or '',
                'Department': applicant['department_id'][1] if applicant['department_id'] else '',
                'Stage': applicant['stage_id'][1] if applicant['stage_id'] else '',

            })
        print(f"Recruitments exported to: {filename}")



if __name__ == "__main__":
    export_recruitments_csv()