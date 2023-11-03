
from django.core.paginator import Paginator
from django.db.models import F
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.db import models
from django.db.models import Q


@api_view(['POST', 'GET'])
def create_student(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('home')
        else:
            if 'roll_no' in serializer.errors:
                error_message = serializer.errors['roll_no'][0]
            else:
                error_message = "An error occurred while saving the student."
            return render(request, 'create_student.html', {'error_message': error_message})
    else:
        return render(request, 'create_student.html')


@login_required
@api_view(['GET'])
def get_students(request):
    class_name = request.GET.get('class_name')
    data_selection = request.GET.get('data', None)
    name_filter = request.GET.get('name')

    students = Student.objects.all()

    if name_filter:
        students = students.filter(name__icontains=name_filter)
    if class_name:
        students = students.filter(class_name=class_name)

    if name_filter and class_name:
        students = students.filter(name__icontains=name_filter, class_name=class_name)

    students = students.annotate(total_score=F(
        'score1') + F('score2') + F('score3') + F('score4') + F('score5')).order_by('-total_score')

    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if data_selection:
        data_selection = data_selection.split(',')
        if 'roll' not in data_selection:
            data_selection.append('roll')
        serializer = StudentSerializer(
            page_obj, many=True, fields=data_selection)
    else:
        serializer = StudentSerializer(page_obj, many=True)

    context = {
        'students': serializer.data,
        'class_name': class_name,
        'data_selection': data_selection,
        'name_filter': name_filter,
    }

    return render(request, 'student_data.html', context)


@login_required
def display_students(request):
    students = Student.objects.annotate(total_score=F(
        'score1') + F('score2') + F('score3') + F('score4') + F('score5')).order_by('-total_score')
    return render(request, 'student_data.html', {'students': students})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials. Please try again.'})
    else:
        return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
