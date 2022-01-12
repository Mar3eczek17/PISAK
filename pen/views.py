from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Memo
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login

# Create your views here.
def memo(request):
    return render(
        request,
        'pen/memo.html'
    )

def add_new_memo(request):
    if request.method == "POST":
        memo = Memo()
        memo.body = request.POST["memo_body"]
        memo.save()
        return redirect('pen:memo')

def show_all_memos(request):
    memo = Memo.objects.all()
    return render(
        request,
        'pen/show_all_memos.html',
        context={
            'memo': memo
        }
    )

# Create your views here.
def login_view(request):

    if request.method == "POST":
        data = request.POST
        user = authenticate(
            username=data.get('user'),
            password=data.get('password')
        )

        if user:
            login(request, user=user)

        return redirect('pen:home')

    return render(
        request,
        "pen/login.html"
    )

def home(request):
    if request.method == "POST":
        logout(request)
        redirect('pen:home')

    return render(
        request,
        'pen/home.html',
    )

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('pen:login-view')

    form = UserCreationForm()


    return render(
        request,
        'pen/register.html',
        context={
            'form': form,

        }
    )