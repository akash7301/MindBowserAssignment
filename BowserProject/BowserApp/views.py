from django.shortcuts import render,redirect

# Create your views here.
from .models import Manager
from .forms import SignUpForm

def signup(request):
    form = SignUpForm()
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('login')
        else:
            return render(request,'BowserApp/sign_up.html',locals())
    return render(request,'BowserApp/sign_up.html',locals())

def home_page(request):
    return render(request,'BowserApp/home_page.html')
