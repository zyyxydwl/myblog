from django.db import models

# Create your models here.


class Artical(models.Model):
    title=models.CharField(max_length=32,default="Title")
    content=models.TextField(null=True)
    pub_date=models.DateTimeField(auto_now=True)
    # python manage.py shell 可以测试未知的方法，Artical.objects.all().values()
    def __str__(self):
        return self.title

