from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    mainimglink = models.CharField(max_length=500)
    mainimg = models.FileField(upload_to='blog/images')
    mainalt = models.CharField(max_length=500)
    date = models.DateField()
    authorlink = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    titledesc = models.CharField(max_length=5000)
    firsthead = models.CharField(max_length=500)
    firstpara = models.CharField(max_length=5000)
    list1 = models.CharField(max_length=500)
    list2 = models.CharField(max_length=500)
    list3 = models.CharField(max_length=500)
    list4 = models.CharField(max_length=500)
    list5 = models.CharField(max_length=500)
    list6 = models.CharField(max_length=500)
    listnpara = models.CharField(max_length=5000)
    subhead = models.CharField(max_length=500)
    subpara = models.CharField(max_length=5000)
    imagehead = models.CharField(max_length=500)
    imagepara = models.CharField(max_length=5000)
    imagelinkc =models.CharField(max_length=500)
    imgc = models.FileField(upload_to='blog/images')
    imgcalt = models.CharField(max_length=500)
    centerhead = models.CharField(max_length=500)
    centerpara = models.CharField(max_length=5000)
    lastimglink = models.CharField(max_length=500)
    lastimg = models.FileField(upload_to='blog/images')
    lastimgalt = models.CharField(max_length=500)
    shead1 = models.CharField(max_length=500)
    sdesc1 = models.CharField(max_length=5000)
    shead2 = models.CharField(max_length=500)
    sdesc2 = models.CharField(max_length=5000)
    shead3 = models.CharField(max_length=500)
    sdesc3 = models.CharField(max_length=5000)
    thumbnail = models.FileField(upload_to='blog/images', default="")
    field = models.CharField(max_length=50)


    def __str__(self):
        return self.title



