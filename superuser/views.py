from django.shortcuts import render

# Create your views here.
def superuser(request):
    return render(request,'user.html')