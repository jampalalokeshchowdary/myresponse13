from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')
