

# Create your views here.


# views.py

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Professor, Rating
from .forms import ProfessorForm,RatingForm
import uuid


def index(request):
   professors=Professor.objects.all
   return render(request,"index.html",{'professors':professors})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')



def professor_detail(request, professor_id):
    professor = Professor.objects.get(id=professor_id)
    average_rating = professor.get_average_rating()
    print('average rating')
    if request.method == 'POST':
        rating = int(request.POST['rating'])
        user_id = request.POST['user_id']
        try:
            existing_rating = Rating.objects.get(user_id=user_id, professor=professor)
            existing_rating.rating = rating
            existing_rating.save()
        except Rating.DoesNotExist:
            Rating.objects.create(user_id=user_id, professor=professor, rating=rating)
        return redirect('professor_detail', professor_id=professor_id)
    else:
        user_id = str(uuid.uuid4())
        try:
            rating = Rating.objects.get(user_id=user_id, professor=professor)
        except Rating.DoesNotExist:
            rating = None
            ratings = Rating.objects.filter(professor=professor)  
            print(ratings) 
        return render(request, 'professor_detail.html', {'professor': professor, 'rating': rating, 'user_id': user_id,'ratings': ratings,'average_rating':average_rating})

    
def create_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            professor=form.save()
            return redirect(reverse('add_rating', args=[professor.id]))
    else:
        form = ProfessorForm()
    return render(request, 'create_professor.html', {'form': form})


def add_rating(request, professor_id):
    professor = Professor.objects.get(id=professor_id)

    if request.method == 'POST':
        user_id = request.user.id
        try:
            existing_rating = Rating.objects.get(user_id=user_id, professor=professor)
            form = RatingForm(request.POST, instance=existing_rating)
        except Rating.DoesNotExist:
            form = RatingForm(request.POST)

        if form.is_valid():
            rating = form.save(commit=False)
            rating.user_id = user_id
            rating.professor = professor
            rating.save()
            return redirect('professor_detail', professor_id=professor_id)
    else:
        form = RatingForm()

    return render(request, 'add_rating.html', {'form': form, 'professor': professor})

def professor_list(request):
     professors=Professor.objects.all()
     return render(request, 'professor_list.html',{"professors":professors})


# def professor_detail(request, professor_id):
#     professor = Professor.objects.get(id=professor_id)
#     if request.method == 'POST':
#         rating = int(request.POST['rating'])
#         user_id = request.POST['user_id']
#         try:
#             existing_rating = Rating.objects.get(user_id=user_id, professor=professor)
#             existing_rating.rating = rating
#             existing_rating.save()
#         except Rating.DoesNotExist:
#             Rating.objects.create(user_id=user_id, professor=professor, rating=rating)
#         return redirect('professor_detail', professor_id=professor_id)
#     else:
#         user_id = str(uuid.uuid4())
#         try:
#             rating = Rating.objects.get(user_id=user_id, professor=professor)
#         except Rating.DoesNotExist:
#             rating = None
#         return render(request, 'ratings/professor_detail.html', {'professor': professor, 'rating': rating, 'user_id': user_id})
    
    
# def create_professor(request):
#     if request.method == 'POST':
#         form = ProfessorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = ProfessorForm()
#     return render(request, 'create_professor.html', {'form': form})
