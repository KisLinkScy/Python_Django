from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')
def loging(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return redirect("login")
    else:
        return render(request, "main/login.html")
    
def logout_user(request):
    logout(request)
    return redirect("login")

def registr_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
    return render(request, "main/registr.html", {"form": form})