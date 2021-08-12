from django.db import models




class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    Offer=models.BooleanField(default=False)

class nature(models.Model):
     month=models.CharField(max_length=150)
     img=models.ImageField(upload_to='picture')
     desc=models.TextField()
     heading=models.CharField(max_length=100)




