from django.contrib import admin
from .models import Resim, Urun, Fatura
import logging

# Register your models here.
logger = logging.getLogger(__name__)

class MyModelAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        # Model kaydedilmeden önce log oluşturun
        logger.info(f'{obj} kaydedildi.')

        super().save_model(request, obj, form, change)

admin.site.register(Resim, MyModelAdmin)
admin.site.register(Urun, MyModelAdmin)
admin.site.register(Fatura, MyModelAdmin)