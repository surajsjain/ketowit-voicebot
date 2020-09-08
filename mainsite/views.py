from django.shortcuts import render

# Create your views here.
def getLandingPage(request):
    return render(request, 'mainsite/index.html')