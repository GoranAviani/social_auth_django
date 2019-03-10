from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return render(request,'login1.html')
    else:

        return redirect('index')
