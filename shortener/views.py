from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5] #shorten generated unique id to 5 chars
        new_url = Url(link=url,uuid=uid)
        new_url.save() #save to database
        return HttpResponse(uid)

def go(request,pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)