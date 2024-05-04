from django.db import models
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.

continents = [
    ('Asia','Asia'),  
    ('Africa','Africa'),
    ('Europe','Europe'),
    ('America','America'),

]
period =[
    ('Days','Days'),
    ('Weeks','Weeks'),
    ('Months','Months'),

]
def image_upload(instance,filename):
    imagename,extension=filename.split(".")
    return "imagehome/%s.%s"%(instance.id,extension)


class Places(models.Model):
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    continent = models.CharField(max_length=10,choices=continents)
    image=models.ImageField(upload_to=image_upload)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    description=models.TextField()
    discount = models.DecimalField(max_digits=8,decimal_places=2)
    period =models.CharField(max_length=6,choices=period)
    duration = models.IntegerField()
    date=models.DateField(default=timezone.now)

    slug = models.SlugField(null=True,blank=True)


    def save(self,*args,**kwargs):
        self.slug =slugify (self.city)
        super(Places,self).save(*args, **kwargs)
        

    def __str__(self):
        return self.city
    
    def child_price(self):
        return self.price / 2

    


class Booking(models.Model):
    trip= models.ForeignKey(Places, related_name='Book_trip', on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    date = models.DateField(default=timezone.now)
    adults = models.IntegerField()
    children = models.IntegerField()
    total_price=models.DecimalField(max_digits=8,decimal_places=2)
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Booking for {self.trip}" 