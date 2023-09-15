from django.db import models
# Create your models here.

class Resim(models.Model):
    resim = models.ImageField(blank=True, upload_to='images/')
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class Urun(models.Model):
    urun_adi = models.CharField(max_length=50)
    urun_adedi = models.IntegerField()
    resim = models.ForeignKey(Resim, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.urun_adi

class Fatura(models.Model):
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE)
    fiyat = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Fatura {self.id} - Ürün: {self.urun.urun_adi}, Fiyat: {self.fiyat}"
    
    def save(self, *args, **kwargs):
        # Fatura kaydedildiğinde, ilişkili ürünün urun_adedi'ni artırın
        self.urun.urun_adedi += 1
        self.urun.save()
        super(Fatura, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Fatura silindiğinde, ilişkili ürünün urun_adedi'ni azaltın
        self.urun.urun_adedi -= 1
        self.urun.save()
        super(Fatura, self).delete(*args, **kwargs)


