from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import render, get_object_or_404, redirect

from .models import Student
from .forms import StudentForm


@login_required
def dashboard(request):

    students = Student.objects.all()

    total_students = students.count()

    total_male = students.filter(
        gender="Male"
    ).count()

    total_female = students.filter(
        gender="Female"
    ).count()

    average_marks = students.aggregate(
        avg=Avg("marks")
    )["avg"]

    if average_marks is None:
        average_marks = 0

    recent_students = students.order_by("-id")[:5]

    context = {
        "total_students": total_students,
        "total_male": total_male,
        "total_female": total_female,
        "average_marks": round(average_marks, 2),
        "recent_students": recent_students,
    }

    return render(
        request,
        "student/dashboard.html",
        context
    )


@login_required
def student_list(request):

    students = Student.objects.all().order_by("-id")

    return render(
        request,
        "student/student_list.html",
        {
            "students": students
        }
    )


@login_required
def student_detail(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    return render(
        request,
        "student/student_detail.html",
        {
            "student": student
        }
    )


@login_required
def student_create(request):

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect("student_list")

    else:

        form = StudentForm()

    return render(
        request,
        "student/student_form.html",
        {
            "form": form,
            "page_title": "Add Student",
            "button_text": "Save Student",
        }
    )


@login_required
def student_update(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():

            form.save()

            return redirect(
                "student_detail",
                pk=student.pk
            )

    else:

        form = StudentForm(
            instance=student
        )

    return render(
        request,
        "student/student_form.html",
        {
            "form": form,
            "page_title": "Edit Student",
            "button_text": "Update Student",
        }
    )


@login_required
def student_delete(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    if request.method == "POST":

        student.delete()

        return redirect("student_list")

    return render(
        request,
        "student/student_confirm_delete.html",
        {
            "student": student
        }
    )