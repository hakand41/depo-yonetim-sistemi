from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import UrunForm, ResimForm, FaturaForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import Urun, Resim, Fatura
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
# Create your views here.

def index(request):
    urunler = Urun.objects.all()
    context = {
        "urunler":urunler
    }
    return render(request, "index.html", context)

def dashboard(request):
    return render(request, "dashboard.html")

def detailurun(request,id):
    urun = Urun.objects.filter(id = id).first()
    return render(request, "detailurun.html", {"urun":urun})

def detailfatura(request,id):
    fatura = Fatura.objects.filter(id = id).first()
    return render(request, "detailfatura.html", {"fatura":fatura})

def detailresim(request,id):
    resim = Resim.objects.filter(id = id).first()
    return render(request, "detailresim.html", {"resim":resim})

def urunler(request):
    urunler = Urun.objects.all()
    context = {
        "urunler":urunler
    }
    return render(request, "urunler.html", context)

def faturalar(request):
    faturalar = Fatura.objects.all()
    context = {
        "faturalar":faturalar
    }
    return render(request, "faturalar.html", context)

@login_required(login_url="user:login")
def addproduct(request):
    form = UrunForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.save()
        messages.success(request, "Ürün başarıyla eklendi")
        return redirect("dashboard")
    return render(request, "addproduct.html", {"form" : form})

@login_required(login_url="user:login")
def addimage(request):
    if request.method == 'POST':
        form = ResimForm(request.POST, request.FILES)
        if form.is_valid():
            resim = form.save(commit=False)
            resim.save()
            messages.success(request, "Resim başarıyla eklendi")
            return redirect("dashboard")
    else:
        form = ResimForm()
    
    return render(request, "addimage.html", {"form": form})

@login_required(login_url="user:login")
def addfatura(request):
    if request.method == 'POST':
        form = FaturaForm(request.POST)
        if form.is_valid():
            fatura = form.save()
            return redirect("dashboard")
    else:
        form = FaturaForm()

    return render(request, "addfatura.html", {"form": form})

@login_required(login_url="user:login")  
def deletefatura(request):
    faturalar = Fatura.objects.all()
    return render(request, "deletefatura.html", {"faturalar": faturalar})

@login_required(login_url="user:login")
def fatura_sil(request, fatura_id):
    fatura = get_object_or_404(Fatura, id=fatura_id)
    fatura.delete()
    return redirect("deletefatura")

@login_required(login_url="user:login")  
def deleteurun(request):
    urunler = Urun.objects.all()
    return render(request, "deleteurun.html", {"urunler": urunler})

@login_required(login_url="user:login")
def urun_sil(request, urun_id):
    urun = get_object_or_404(Urun, id=urun_id)
    urun.delete()
    return redirect("deleteurun")

@login_required(login_url="user:login")  
def deleteresim(request):
    resimler = Resim.objects.all()
    return render(request, "deleteresim.html", {"resimler": resimler})

@login_required(login_url="user:login")
def resim_sil(request, resim_id):
    resim = get_object_or_404(Resim, id=resim_id)
    resim.resim.delete()  # Dosyayı fiziksel olarak silme
    resim.delete()  # Veritabanından resimi silme
    return redirect("deleteresim")

@login_required(login_url="user:login")  
def updateurun(request):
    urunler = Urun.objects.all()
    return render(request, "updateurun.html", {"urunler": urunler})

@login_required(login_url="user:login")
def urun_up(request, id):
    urun = get_object_or_404(Urun, id = id)
    form = UrunForm(request.POST or None, request.FILES or None, instance=urun)
    if form.is_valid():
        urun = form.save(commit=False)
        urun.save()
        messages.success(request, "Ürün başarıyla güncellendi")
        return redirect("dashboard")
    return render(request, "urun_up.html", {"form":form})

@login_required(login_url="user:login")  
def updateresim(request):
    resimler = Resim.objects.all()
    return render(request, "updateresim.html", {"resimler": resimler})

@login_required(login_url="user:login")
def resim_up(request, id):
    resim = get_object_or_404(Resim, id = id)
    form = ResimForm(request.POST or None, request.FILES or None, instance=resim)
    if form.is_valid():
        resim = form.save(commit=False)
        resim.save()
        messages.success(request, "Resim başarıyla güncellendi")
        return redirect("dashboard")
    return render(request, "resim_up.html", {"form":form})

@login_required(login_url="user:login")  
def updatefatura(request):
    faturalar = Fatura.objects.all()
    return render(request, "updatefatura.html", {"faturalar": faturalar})

@login_required(login_url="user:login")
def fatura_up(request, id):
    fatura = get_object_or_404(Fatura, id = id)
    form = FaturaForm(request.POST or None, request.FILES or None, instance=fatura)
    if form.is_valid():
        fatura = form.save(commit=False)
        fatura.save()
        messages.success(request, "Fatura başarıyla güncellendi")
        return redirect("dashboard")
    return render(request, "fatura_up.html", {"form":form})

def urun_fiyat_grafik(request, urun_id):
    try:
        urun = Urun.objects.get(pk=urun_id)
        faturalar = Fatura.objects.filter(urun=urun).order_by('created_at')
    except Urun.DoesNotExist:
        urun = None
        faturalar = []

    fiyatlar = [fatura.fiyat for fatura in faturalar]
    tarihler = [fatura.created_at.strftime('%Y-%m-%d %H:%M:%S') for fatura in faturalar]

    plt.figure(figsize=(10, 6))
    plt.plot(tarihler, fiyatlar, marker='o', color='blue')
    plt.xlabel('Tarih')
    plt.ylabel('Fiyat')
    plt.title(f'{urun.urun_adi} Ürününün Fiyat Değişimi')
    plt.xticks(rotation=45)
    plt.tight_layout()

    response = HttpResponse(content_type='image/png')
    canvas = FigureCanvas(plt.gcf())
    canvas.print_png(response)
    plt.close()

    return response

def sorgu(request):
    if request.method == 'POST':
        urun_id = request.POST.get('urun_id')  # Get the ID of the selected Urun
        try:
            urun = Urun.objects.get(pk=urun_id)
            urun_data = {
                'urun_adi': urun.urun_adi,
                'urun_adedi': urun.urun_adedi,
                'resim': urun.resim,
                'created_at': urun.created_at,
                'updated_at': urun.updated_at,
            }
            return render(request, 'sorgu.html', {'urunler': urun_data})
        except Urun.DoesNotExist:
            # Handle the case where the Urun object doesn't exist
            pass

    return render(request, 'sorgu.html')
    