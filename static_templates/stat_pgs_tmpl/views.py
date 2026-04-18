from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    ctx = {
        'name': "Tony",
        'age': 25,
        'gains': 2344.322211
    }
    return render(request, 'home.html', ctx)

@login_required
def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'login.html')
