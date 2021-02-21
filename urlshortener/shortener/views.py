from django.shortcuts import render
import uuid
from .models import Url
from django.http import HttpResponse

# Create the views ,and url mapping
def index(request):
    return render(request, 'index.html')

def create(request):
    # pass
    if request.method == 'POST':
        link = request.POST['link'] #the id link from html file
        uid = str(uuid.uuid4())[:5] #shorten to only 5 character
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)