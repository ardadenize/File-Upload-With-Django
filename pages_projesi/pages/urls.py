from django.urls import path
from .views import AnasayfaView, VeriAnaliziView, RegresyonAnaliziView, SiniflandirmaView, KumelemeView, UploadCsvView, UploadTxtView, UploadXlsxView

urlpatterns=[
    path('', AnasayfaView.as_view(),name='Anasayfa'),
    path('VeriAnalizi/',VeriAnaliziView.as_view(), name='Veri Analizi'),
    path('RegresyonAnalizi/',RegresyonAnaliziView.as_view(), name='Regresyon Analizi'),
    path('Siniflandirma/',SiniflandirmaView.as_view(), name='Sınıflandırma'),
    path('Kumeleme/',KumelemeView.as_view(), name='Kümeleme'),
    path('csv/upload/',UploadCsvView.as_view(), name='UploadCsv'),
    path('txt/upload/',UploadTxtView.as_view(), name='UploadTxt'),
    path('xlsx/upload/',UploadXlsxView.as_view(), name='UploadXlsx')
]
