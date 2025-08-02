from django.http import HttpResponse
from .models import Student

def add_and_show_student(request):
    student = Student(name="Raj", age=22)
    student.save()
    students = Student.objects.all()
    output = "<h2>Students List</h2><ul>"
    for s in students:
        output += f"<li>{s.name} - {s.age}</li>"
    output += "</ul>"
    return HttpResponse(output)
