from django.shortcuts import render, redirect
from .models import Memo

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