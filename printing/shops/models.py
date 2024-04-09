from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class clients(models.Model):
    def __str__(self):
        return self.shop_name    
    shop_id=models.IntegerField(primary_key=True)
    shop_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    email = models.EmailField(unique=False, null= True )
    image=models.CharField(max_length=1000,default='https://th.bing.com/th/id/OIP.kqT6XFsG2BTW22Y4st2-KAHaHa?pid=ImgDet&rs=1')
    balance=models.IntegerField(default=0)
    transactions = models.TextField(default='')
    amounts = models.TextField(default='') 
    
    
