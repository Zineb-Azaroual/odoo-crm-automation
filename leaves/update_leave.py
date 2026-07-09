from connect import execute

def approve_leave(leave_id) :
    result = execute('hr.leave', 'action_approve', [[leave_id]])
    print(f"Leave with id : {leave_id} is approved")
    return result

def refuse_leave(leave_id) :
    result = execute('hr.leave', 'action_refuse', [[leave_id]])
    print(f"Leave with id : {leave_id} is refused")
    return result

# resets a leave request back to draft status
def draft_leave(leave_id) :
    result = execute('hr.leave', 'write', [[leave_id], {'state': 'draft'}])
    print(f"Leave with id : {leave_id} reset to draft")
    return result

if __name__ == "__main__":
    # Remplace 1 par l'ID réel de ta demande de congé
    draft_leave(3)