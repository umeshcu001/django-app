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
    firsthead1 = models.CharField(max_length=500, default="")
    firstpara1 = models.CharField(max_length=5000, default="")
    list11 = models.CharField(max_length=500, default="")
    list21 = models.CharField(max_length=500, default="")
    list31 = models.CharField(max_length=500, default="")
    list41 = models.CharField(max_length=500, default="")
    list51 = models.CharField(max_length=500, default="")
    list61 = models.CharField(max_length=500, default="")
    listnpara1 = models.CharField(max_length=5000, default="")
    subhead1 = models.CharField(max_length=500, default="")
    subpara1 = models.CharField(max_length=5000, default="")
    imagehead1 = models.CharField(max_length=500, default="")
    imagepara1 = models.CharField(max_length=5000, default="")
    imagelinkc1 =models.CharField(max_length=500, default="")
    imgc1 = models.FileField(upload_to='blog/images', default="")
    imgcalt1 = models.CharField(max_length=500, default="")
    centerhead1 = models.CharField(max_length=500, default="")
    centerpara1 = models.CharField(max_length=5000, default="")
    lastimglink1 = models.CharField(max_length=500, default="")
    lastimg1 = models.FileField(upload_to='blog/images', default="")
    lastimgalt1 = models.CharField(max_length=500, default="")
    keywords = models.CharField(max_length=5000, default="")
    metadesc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.title


class Blogsec(models.Model):
    post_id1 = models.AutoField(primary_key=True)
    title1 = models.CharField(max_length=500)
    mainimglink1 = models.CharField(max_length=500)
    mainimg1 = models.FileField(upload_to='blog/images')
    mainalt1 = models.CharField(max_length=500)
    date1 = models.DateField()
    authorlink1 = models.CharField(max_length=500)
    author1 = models.CharField(max_length=500)
    titledesc1 = models.CharField(max_length=5000)
    firsthead11 = models.CharField(max_length=500)
    firstpara11 = models.CharField(max_length=5000)
    list111 = models.CharField(max_length=500)
    list211 = models.CharField(max_length=500)
    list311 = models.CharField(max_length=500)
    list411 = models.CharField(max_length=500)
    list511 = models.CharField(max_length=500)
    list611 = models.CharField(max_length=500)
    listnpara11 = models.CharField(max_length=5000)
    subhead111 = models.CharField(max_length=500, default="")
    subpara111 = models.CharField(max_length=5000, default="")
    chead1 = models.CharField(max_length=500, default="")
    cpara1 = models.CharField(max_length=5000, default="")
    img1link = models.CharField(max_length=500, default="")
    img1 = models.FileField(upload_to='blog/images', default="")
    img1alt = models.CharField(max_length=500, default="")
    imghead1 = models.CharField(max_length=500, default="")
    img1para = models.CharField(max_length=5000, default="")
    img2link = models.CharField(max_length=500, default="")
    img2 = models.FileField(upload_to='blog/images', default="")
    img2alt = models.CharField(max_length=500, default="")
    imghead2 = models.CharField(max_length=500, default="")
    img2para = models.CharField(max_length=5000, default="")
    img3link = models.CharField(max_length=500, default="")
    img3 = models.FileField(upload_to='blog/images', default="")
    img3alt = models.CharField(max_length=500, default="")
    imghead3 = models.CharField(max_length=500, default="")
    img3para = models.CharField(max_length=5000, default="")
    sihead = models.CharField(max_length=500, default="")
    sipara = models.CharField(max_length=5000, default="")
    siimglink = models.CharField(max_length=500, default="")
    siimg = models.FileField(upload_to='blog/images', default="")
    siimgalt = models.CharField(max_length=500, default="")
    chead2 = models.CharField(max_length=500, default="")
    cpara2 = models.CharField(max_length=5000, default="")
    img11link = models.CharField(max_length=500, default="")
    img11 = models.FileField(upload_to='blog/images', default="")
    img11alt = models.CharField(max_length=500, default="")
    imghead11 = models.CharField(max_length=500, default="")
    img11para = models.CharField(max_length=5000, default="")
    img21link = models.CharField(max_length=500, default="")
    img21 = models.FileField(upload_to='blog/images', default="")
    img21alt = models.CharField(max_length=500, default="")
    imghead21 = models.CharField(max_length=500, default="")
    img21para = models.CharField(max_length=5000, default="")
    img31link = models.CharField(max_length=500, default="")
    img31 = models.FileField(upload_to='blog/images', default="")
    img31alt = models.CharField(max_length=500, default="")
    imghead31 = models.CharField(max_length=500, default="")
    img31para = models.CharField(max_length=5000, default="")
    firsthead1 = models.CharField(max_length=500, default="")
    firstpara1 = models.CharField(max_length=5000, default="")
    list11 = models.CharField(max_length=500, default="")
    list21 = models.CharField(max_length=500, default="")
    list31 = models.CharField(max_length=500, default="")
    list41 = models.CharField(max_length=500, default="")
    list51 = models.CharField(max_length=500, default="")
    list61 = models.CharField(max_length=500, default="")
    listnpara1 = models.CharField(max_length=5000, default="")
    keywords1 = models.CharField(max_length=5000, default="")
    thumbnail1 = models.FileField(upload_to='blog/images', default="")
    field1 = models.CharField(max_length=50)
    metadesc1 = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.title1



