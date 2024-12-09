from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'shop/index.html')

def menu(request):
    return render(request,'shop/menu.html')