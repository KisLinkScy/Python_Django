from django.shortcuts import render

# Create your views here.
def svet(request):
    return render(request, 'main/svet.html')