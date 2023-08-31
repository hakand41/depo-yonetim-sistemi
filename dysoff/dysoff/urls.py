"""dysoff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import loginUser, logoutUser
from products import views as vws
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', loginUser, name = "login"),
    path('logout/', logoutUser, name = "logout"),
    path('', vws.index, name= "index"),
    path("dashboard/", vws.dashboard, name="dashboard"),
    path("urunler/<int:id>/", vws.detailurun, name="detailurun"),
    path("faturalar/<int:id>", vws.detailfatura, name="detailfatura"),
    path("resimler/<int:id>", vws.detailresim, name="detailresim"),
    path("urunler/", vws.urunler, name="urunler"),
    path("faturalar/", vws.faturalar, name="faturalar"),
    path("addproduct/", vws.addproduct, name="addproduct"),
    path("addimage/", vws.addimage, name="addimage"),
    path("addfatura/", vws.addfatura, name="addfatura"),
    path('deletefatura/', vws.deletefatura, name='deletefatura'),
    path('fatura/sil/<int:fatura_id>/', vws.fatura_sil, name='fatura_sil'),
    path('deleteurun/', vws.deleteurun, name='deleteurun'),
    path('urun/sil/<int:urun_id>/', vws.urun_sil, name='urun_sil'),
    path('deleteresim/', vws.deleteresim, name='deleteresim'),
    path('resim/sil/<int:resim_id>/', vws.resim_sil, name='resim_sil'),
    path("updateurun/", vws.updateurun, name="updateurun"),
    path("urun_up/<int:id>", vws.urun_up, name="urun_up"),
    path("updateresim/", vws.updateresim, name="updateresim"),
    path("resim_up/<int:id>", vws.resim_up, name="resim_up"),
    path("updatefatura/", vws.updatefatura, name="updatefatura"),
    path("fatura_up/<int:id>/", vws.fatura_up, name="fatura_up"),
    path('urun_fiyat_grafik/<int:urun_id>/', vws.urun_fiyat_grafik, name='urun_fiyat_grafik'),
    path("sorgu/", vws.sorgu, name="sorgu"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)