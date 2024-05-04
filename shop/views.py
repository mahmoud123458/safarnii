from django.shortcuts import render
from home.models import Places
# Create your views here.
def shop(request):
     places=Places.objects.all()
     return render(request,'shop.html',{'places':places})