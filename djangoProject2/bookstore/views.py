import time
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import BookForm
from .models import Book
from django.shortcuts import render, get_object_or_404

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = BookForm()

    # Получаем все модели авто для отображения на странице
    books = Book.objects.all()

    return render(request, 'add_book.html', {'form': form})

def catalog(request):
    books = Book.objects.all()
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(model__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'catalog.html', {'books': books})


def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            version = int(time.time())  # Генерация версии из текущего времени
            return redirect('catalog')
    else:
        form = BookForm(instance=book)

    version = int(time.time())  # Генерация версии из текущего времени
    return render(request, 'edit_book.html', {'form': form, 'version': version})

@login_required
def personal_cabinet(request):
    return render(request, 'personal_cabinet.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('personal_cabinet'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('personal_cabinet'))
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

