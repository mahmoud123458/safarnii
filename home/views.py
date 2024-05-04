from django.shortcuts import redirect, render
from .  models import Places
from .form import BookForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
     places=Places.objects.all()
     return render(request,'home/index.html',{'places':places})
    

@login_required   
def home_detail(request,slug):
     places_detail=Places.objects.get(slug=slug)

     if request.method=='POST':
          form=BookForm(request.POST,request.FILES)
          if form.is_valid():
               myform=form.save(commit=False)
               myform.total_price=form.cleaned_data['total_price']
               myform.save()

          return redirect('success_page') 

     else:
          form = BookForm()

     context={'place':places_detail,'form':form}
     return render(request,'home/detail.html',context)

