from django.shortcuts import render

# Create your views here.
def memo(request):
    return render(
        request,
        'pen/memo.html'
    )