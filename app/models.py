from django.db import models

class Category(models.Model):
    code=models.CharField(max_length=20,unique=True,verbose_name='Ma')
    name=models.CharField(max_length=100,verbose_name="Ten")
    def __str__(self):
        return self.code
class Product(models.Model):
    def __str__(self):
        return self.code
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description=models.CharField(max_length=300,blank=True)
    image=models.ImageField(upload_to='static/images')


