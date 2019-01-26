from django.db import models

class MyModel(models.Model):

    urun_kodu  = models.CharField(max_length=25)
    adet = models.IntegerField()
    son_kullanma = models.CharField(max_length=8)
    kategori =models.CharField(max_length=9)
class Urun(models.Model):

    urun_kodu = models.CharField(max_length=25)
    urun_adi = models.CharField(max_length=25)
#    urun_kat = models.FileField(widget=forms.FileInput())
    adet = models.IntegerField()
    son_kullanma = models.CharField(max_length=8)



from django_pandas.io import read_frame
qs = MyModel.objects.all()
qs = Urun.objects.all()

def publish(self):

        self.save()

def __str__(self):
        return self.title

#def clean_son_kullanma(self):
 #### tel = self.cleaned_data['son_kullanma']
 ### if tel != "":
    #  if len(tel) != 8:
##    raise forms.ValidationError('tarih 8 haneli olmalı, lütfen noktalama işareti kullanmayın.')
#return tel
