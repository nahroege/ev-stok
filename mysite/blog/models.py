from django.db import models

class MyModel(models.Model):

    urun_kodu  = models.CharField(max_length=25)
    urun_adi  = models.CharField(max_length=25)
    adet = models.IntegerField()
    son_kullanma = models.CharField(max_length=8)
    


from django_pandas.io import read_frame
qs = MyModel.objects.all()

def publish(self):

        self.save()

def __str__(self):
        return self.title
