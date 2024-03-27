from django.shortcuts import render

# Create your views here.
def gaz(request):
    return render(request, 'main/gaz.html')