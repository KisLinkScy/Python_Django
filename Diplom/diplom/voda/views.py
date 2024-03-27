from django.shortcuts import render

# Create your views here.
def voda(request):
    return render(request, 'main/voda.html')