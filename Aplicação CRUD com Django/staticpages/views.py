from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'staticpages/index.html', context)
# Create your views here.
