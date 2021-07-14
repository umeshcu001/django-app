# Generated by Django 3.2.3 on 2021-06-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogpost_keywords'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogsec',
            fields=[
                ('postid', models.AutoField(primary_key=True, serialize=False)),
                ('title1', models.CharField(max_length=500)),
                ('mainimglink', models.CharField(max_length=500)),
                ('mainimg', models.FileField(upload_to='blog/images')),
                ('mainalt', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('authorlink', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=500)),
                ('titledesc1', models.CharField(max_length=5000)),
                ('firsthead', models.CharField(max_length=500)),
                ('firstpara', models.CharField(max_length=5000)),
                ('list1', models.CharField(max_length=500)),
                ('list2', models.CharField(max_length=500)),
                ('list3', models.CharField(max_length=500)),
                ('list4', models.CharField(max_length=500)),
                ('list5', models.CharField(max_length=500)),
                ('list6', models.CharField(max_length=500)),
                ('listnpara', models.CharField(max_length=5000)),
                ('subhead1', models.CharField(default='', max_length=500)),
                ('subpara1', models.CharField(default='', max_length=5000)),
                ('chead1', models.CharField(default='', max_length=500)),
                ('cpara1', models.CharField(default='', max_length=5000)),
                ('img1link', models.CharField(default='', max_length=500)),
                ('img1', models.FileField(default='', upload_to='blog/images')),
                ('img1alt', models.CharField(default='', max_length=500)),
                ('imghead1', models.CharField(default='', max_length=500)),
                ('img1para', models.CharField(default='', max_length=5000)),
                ('img2link', models.CharField(default='', max_length=500)),
                ('img2', models.FileField(default='', upload_to='blog/images')),
                ('img2alt', models.CharField(default='', max_length=500)),
                ('imghead2', models.CharField(default='', max_length=500)),
                ('img2para', models.CharField(default='', max_length=5000)),
                ('img3link', models.CharField(default='', max_length=500)),
                ('img3', models.FileField(default='', upload_to='blog/images')),
                ('img3alt', models.CharField(default='', max_length=500)),
                ('imghead3', models.CharField(default='', max_length=500)),
                ('img3para', models.CharField(default='', max_length=5000)),
                ('sihead', models.CharField(default='', max_length=500)),
                ('sipara', models.CharField(default='', max_length=5000)),
                ('siimglink', models.CharField(default='', max_length=500)),
                ('siimg', models.FileField(default='', upload_to='blog/images')),
                ('siimgalt', models.CharField(default='', max_length=500)),
                ('chead2', models.CharField(default='', max_length=500)),
                ('cpara2', models.CharField(default='', max_length=5000)),
                ('img11link', models.CharField(default='', max_length=500)),
                ('img11', models.FileField(default='', upload_to='blog/images')),
                ('img11alt', models.CharField(default='', max_length=500)),
                ('imghead11', models.CharField(default='', max_length=500)),
                ('img11para', models.CharField(default='', max_length=5000)),
                ('img21link', models.CharField(default='', max_length=500)),
                ('img21', models.FileField(default='', upload_to='blog/images')),
                ('img21alt', models.CharField(default='', max_length=500)),
                ('imghead21', models.CharField(default='', max_length=500)),
                ('img21para', models.CharField(default='', max_length=5000)),
                ('img31link', models.CharField(default='', max_length=500)),
                ('img31', models.FileField(default='', upload_to='blog/images')),
                ('img31alt', models.CharField(default='', max_length=500)),
                ('imghead31', models.CharField(default='', max_length=500)),
                ('img31para', models.CharField(default='', max_length=5000)),
                ('firsthead1', models.CharField(default='', max_length=500)),
                ('firstpara1', models.CharField(default='', max_length=5000)),
                ('list11', models.CharField(default='', max_length=500)),
                ('list21', models.CharField(default='', max_length=500)),
                ('list31', models.CharField(default='', max_length=500)),
                ('list41', models.CharField(default='', max_length=500)),
                ('list51', models.CharField(default='', max_length=500)),
                ('list61', models.CharField(default='', max_length=500)),
                ('listnpara1', models.CharField(default='', max_length=5000)),
                ('keywords', models.CharField(default='', max_length=5000)),
                ('thumbnail', models.FileField(default='', upload_to='blog/images')),
                ('field', models.CharField(max_length=50)),
            ],
        ),
    ]