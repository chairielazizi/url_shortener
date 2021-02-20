from django.shortcuts import render

# Create the views ,and url mapping
def index(request):
    return render(request, 'index.html')
