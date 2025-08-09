
from django.shortcuts import render

def index(request):
    return render(request, 'monitor/index.html')
def detection_view(request):
    return render(request, 'monitor/detection.html')

def detect_view(request):
    return render(request, 'detect.html')  # or whatever template you use

def about(request):
    return render(request, 'monitor/about.html')
