from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Memo
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required


@login_required
def memo(request):
    author = request.user
    memo = Memo.objects.filter(author_id=author.id).first()
    body = memo.body if memo else ''
    return render(
        request,
        'pen/memo.html',
        context={
            'body': body
        }
    )


@require_http_methods(["POST"])
def add_new_memo(request):
    author = request.user
    memo = Memo.objects.filter(author_id=author.id).first()
    if memo:
        memo.body = request.POST["memo_body"]
    else:
        memo = Memo()
        memo.body = request.POST["memo_body"]
        memo.author = request.user
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


def login_view(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(
            username=data.get('user'),
            password=data.get('password')
        )

        if user:
            login(request, user=user)
        return redirect('pen:memo')
    return render(
        request,
        "pen/login.html"
    )


@login_required
@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    return redirect("pen:login-view")


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
