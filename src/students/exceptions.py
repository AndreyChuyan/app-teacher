from fastapi import HTTPException, status

exception_student_not_found = HTTPException(status_code=404, detail="Student not found")