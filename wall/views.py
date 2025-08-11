from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required   


# Sticky wall view
def sticky_wall(request):
    notes = Note.objects.filter(deleted=False)
    deleted_notes = Note.objects.filter(deleted=True)
    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sticky_wall')

    return render(request, 'wall/sticky_wall.html', {
        'notes': notes,
        'deleted_notes': deleted_notes,
        'form': form
    })

def complete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.completed = True
    note.save()
    return redirect('sticky_wall')

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.deleted = True
    note.save()
    return redirect('sticky_wall')

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('sticky_wall')
    else:
        form = NoteForm(instance=note)
    return render(request, 'wall/edit_note.html', {'form': form, 'note': note})

# Login view
@login_required
def my_view(request):
    return render(request, 'login.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sticky_wall')
        else:
            return render(request, 'wall/login.html', {'error': 'Invalid username or password'})
    return render(request, 'wall/login.html')
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return render(request, 'wall/register.html', {'error': "Passwords don't match"})
        if User.objects.filter(username=username).exists():
            return render(request, 'wall/register.html', {'error': "Username already taken"})
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        return redirect('login')  # redirect to login after successful registration
    return render(request, 'wall/register.html')

# Home view
def home(request):
    return HttpResponse("Welcome! You are logged in!")

# API views (keep these below)
from rest_framework import generics
from .serializers import NoteSerializer

class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
