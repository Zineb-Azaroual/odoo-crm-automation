from connect import execute
from datetime import datetime

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

import os

from test_contract import fields


def export_employees_pdf():
    #recover employees
    employees = execute('hr.employee', 'search_read', [[]], {
        'fields': ['name', 'job_title', 'department_id', 'work_email', 'work_phone']
    })
    os.makedirs('reports', exist_ok=True)
    #filename
    filename = f"reports/employees_{datetime.now().strftime('%Y%m%d')}.pdf"
    #create pdf document
    doc = SimpleDocTemplate(filename)
    # Table data
    data = [
        ['ID', 'Name', 'Job Title', 'Department', 'Email', 'Phone']
    ]
    # Add employees
    for emp in employees:
        data.append([
            emp['id'],
            emp['name'],
            emp['job_title'] or '',
            emp['department_id'][1] if emp['department_id'] else '',
            emp['work_email'] or '',
            emp['work_phone'] or ''
        ])

    # Create table
    table = Table(data)

    # Table style
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),

        ('GRID', (0, 0), (-1, -1), 1, colors.black),

        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

        ('BACKGROUND', (0, 1), (-1, -1), colors.beige)
    ]))

    # Build PDF
    doc.build([table])

    print(f"Employees exported to: {filename}")


def export_leaves_pdf():
    #recover leaves
    leaves = execute('hr.leave', 'search_read', [[]], {
        'fields' : ['holiday_status_id', 'date_from','date_to', 'notes']
    })
    os.makedirs('reports', exist_ok=True)
    # filename
    filename = f"reports/leaves_{datetime.now().strftime('%Y%m%d')}.pdf"
    # create pdf document
    doc = SimpleDocTemplate(filename)
    # Table data
    data = [
        ['ID', 'Holiday Status', 'Date from', 'Date to', 'Notes']
    ]
    # Add leaves
    for leave in leaves:
        data.append([
            leave['id'],
            leave['holiday_status_id'][1] if leave['holiday_status_id'] else '',
            leave['date_from'] or '',
            leave['date_to'] or '',
            leave['notes'] or '',
        ])

    # Create table
    table = Table(data)
    # Table style
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),

        ('GRID', (0, 0), (-1, -1), 1, colors.black),

        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

        ('BACKGROUND', (0, 1), (-1, -1), colors.beige)
    ]))
    # Build PDF
    doc.build([table])

    print(f"Leaves exported to: {filename}")


def export_recruitments_pdf():
    #recover applicants
    applicants = execute('hr.applicant', 'search_read', [[]], {
        'fields': ['partner_name', 'email_from', 'job_id', 'partner_phone', 'department_id', 'stage_id']
    })
    #filename
    filename = f"reports/recruitment{datetime.now().strftime('%Y%m%d')}.pdf"
    #pdf document
    doc = SimpleDocTemplate(filename)
    # Table data
    data = [
        ['ID', 'Partner Name', 'Email from', 'Job', 'Partner Phone', 'Department', 'Stage']
    ]
    # Add applicants
    for applicant in applicants:
        data.append([
            applicant['id'],
            applicant['partner_name'][1] or '',
            applicant['email_from'] or '',
            applicant['job_id'][1] if applicant['job_id'] else '',
            applicant['partner_phone'] or '',
            applicant['department_id'][1] if applicant['department_id'] else '',
            applicant['stage_id'][1] if applicant['stage_id'] else '',
        ])
        # Create table
        table = Table(data)
        # Table style
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),

            ('GRID', (0, 0), (-1, -1), 1, colors.black),

            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),

            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

            ('BACKGROUND', (0, 1), (-1, -1), colors.beige)
        ]))
        # Build PDF
        doc.build([table])

        print(f"Applicants exported to: {filename}")




if __name__ == "__main__":
    export_recruitments_pdf()