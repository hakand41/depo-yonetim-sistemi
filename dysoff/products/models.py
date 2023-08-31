from django.db import models

# Create your models here.

class Resim(models.Model):
    resim = models.ImageField(blank=True, upload_to='images/')
    title = models.CharField(max_length=50)

class Urun(models.Model):
    urun_adi = models.CharField(max_length=50)
    urun_adedi = models.IntegerField()
    resim = models.ForeignKey(Resim, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Fatura(models.Model):
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE)
    fiyat = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


