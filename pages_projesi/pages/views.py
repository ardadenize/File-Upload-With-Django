from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
import os
from .forms import CsvForm, TxtForm, XlsxForm
from .models import CsvFile, TxtFile, XlsxFile
from django.urls import reverse_lazy



from dataprep.eda import plot
from dataprep.datasets import load_dataset
from dataprep.eda import plot_correlation
from dataprep.eda.missing import plot_missing
import numpy as np


class AnasayfaView(TemplateView):
    template_name='home.html'

class VeriAnaliziView(TemplateView):
    template_name='VeriAnalizi.html'

class RegresyonAnaliziView(TemplateView):
    template_name='RegresyonAnalizi.html'

class SiniflandirmaView(TemplateView):
    template_name='Siniflandirma.html'

class KumelemeView(TemplateView):
    template_name='Kumeleme.html'

class UploadView(TemplateView):
 template_name='upload.html'

class UploadCsvView(TemplateView):
 template_name='upload_csv.html'

class UploadTxtView(TemplateView):
 template_name='upload_txt.html'

class UploadXlsxView(TemplateView):
 template_name='upload_xlsx.html'


class CSVdoc_list(ListView):
   model = CsvFile
   template_name = 'doc_listCSV.html'
   context_object_name = 'docs'

class TXTdoc_list(ListView):
   model = TxtFile
   template_name = 'doc_listTXT.html'
   context_object_name = 'docs'

class XLSXdoc_list(ListView):
   model = XlsxFile
   template_name = 'doc_listXLSX.html'
   context_object_name = 'docs'



class upload_csv(CreateView):
   model = CsvFile
   form_class = CsvForm
   success_url = reverse_lazy('doc_listCSV')
   template_name = 'upload_csv.html'

class upload_txt(CreateView):
   model = TxtFile
   form_class = TxtForm
   success_url = reverse_lazy('doc_listTXT')
   template_name = 'upload_txt.html'

class upload_xlsx(CreateView):
   model = XlsxFile
   form_class = XlsxForm
   success_url = reverse_lazy('doc_listXLSX')
   template_name = 'upload_xlsx.html'

def delete_csv(request, pk):
   if request.method == 'POST':
      doc = CsvFile.objects.get(pk=pk)
      doc.delete()
   return redirect('doc_listCSV')

def delete_txt(request, pk):
   if request.method == 'POST':
      doc = TxtFile.objects.get(pk=pk)
      doc.delete()
   return redirect('doc_listTXT')

def delete_xlsx(request, pk):
   if request.method == 'POST':
      doc = XlsxFile.objects.get(pk=pk)
      doc.delete()
   return redirect('doc_listXLSX')


# ornek veri seti. Biz burada sanki bunu kullanicidan aliyoruz gibi devam edecegiz



def plotcsv(request, pk):
 if request.method == 'POST':
  doc = CsvFile.objects.get(pk=pk)
  df = load_dataset(doc)
  df = df.replace(" ?", np.NaN)
 return plot(df) 

"""

# data ilk yuklendiginde dondurulecek cikti
## bu cikti veri seti hakkinda genel bir bilgi verir bunu da Dataset Statistics altinda gosterir
## ardindan degiskenler ozelinde eksik verileri gosterir ve cok fazla sifir varsa kolonda onu belirtir bunu da Dataset Insights altinda goruruz
## son olarak da her degiskenin tipine gore gorseller olusturur

## daha sonra kisiye korelasyon degerlerini de dondurecegiz

wine_df = load_dataset("wine-quality-red") # bu veri setinin yuklenmesinin sebebi korelasyon olayini gosteren degiskenleri daha uygun
plot_correlation(wine_df)

## burada fonksiyon korelasyon degerlerini cikartiyor ve 3 farkli yontemde korelasyona bakiyor bunlarin grafikleri de bulunuyor. Kullanici ile bunlar da paylasilacak


# kisiye genel verinin hali sunulduktan sonra degisken ozelinde inceleme yapma secenegi veriyor olacagiz
## kisiden  hangi degiskeni incelemek istedigini soracagiz ve bunu input olarak alacagiz
## fonksiyon da o degisken icin istatistikler ve grafikler dondurecek. Burada birden fazla grafik oluyor o degisken ozelinde
## son olarak degiskenin kategorik veya numerik olma durumuna gore dondurulen istatistikler ve gorseller farklilasacaktir fonksiyon bu durumu tanimliyor zaten

plot(df,"age")

## ayni zamanda kisiye sunu soracagiz iki degiskeni birlikte incelemek ister misiniz? bu durumda kisi bunu istiyorsa ondan input olarak 2 degisken alacagiz

plot(df, "workclass","education")

## kisi den yine input alarak bir degiskenin diger degiskenlerele olan korelasyonunu gormek isterse onu da sununla donduruyoruz 

plot_correlation(wine_df,"pH")

## yine ayni sekilde iki degisken arasindaki korelasyonlari da gormek isterse iki adet input alarak bunu da donduruyoruz

plot_correlation(wine_df,"pH","density")


 
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        split_tup = os.path.splitext(uploaded_file.name)
        print(split_tup)
  
        file_name = split_tup[0]
        file_extension = split_tup[1]
  
        print("File Name: ", file_name)
        print("File Extension: ", file_extension)

        if(file_extension == ".xlsx" or file_extension == ".csv"or file_extension == ".txt"):
              fs = FileSystemStorage()
              name = fs.save(uploaded_file.name, uploaded_file)
              context['url'] = fs.url(name)
              return render(request, 'uploadedFile.html')
              

        else:
              print("Please upload 'xlsx', 'csv' or 'txt' files")
              return render(request, 'notUpload.html')

       
    else:
        return render(request, 'upload.html')

        """



   


"""
def upload_csv(request):
    if request.method == 'POST':

       form = CsvForm(request.POST, request.FILES)
       if form.is_valid():
          form.save()
          return redirect('doc_listCSV')
    else:
        form = CsvForm()

    return render(request, 'upload_csv.html', {
        'form': form
    })
"""




"""
def upload_xlsx(request):
    if request.method == 'POST':
     form = XlsxForm(request.POST, request.FILES)
     if form.is_valid():
        form.save()
        return redirect('doc_listXLSX')
    else:
        form = XlsxForm()

    return render(request, 'upload_xlsx.html', {
        'form': form
    })

def upload_txt(request):
    if request.method == 'POST':
     form = TxtForm(request.POST, request.FILES)
     if form.is_valid():
        form.save()
        return redirect('doc_listTXT')
    else:
        form = TxtForm()

    return render(request, 'upload_txt.html', {
        'form': form
    })
              
"""
