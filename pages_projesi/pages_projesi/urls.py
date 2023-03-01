
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from pages import views
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("upload/", views.upload, name='upload'),
    

    path("docs/csv", views.CSVdoc_list.as_view(), name='doc_listCSV'),
    path("docs/xlsx", views.XLSXdoc_list.as_view(), name='doc_listXLSX'),
    path("docs/txt", views.TXTdoc_list.as_view(), name='doc_listTXT'),
    path("csv/upload/", views.upload_csv.as_view(), name='upload_csv'),
    path("xlsx/upload/", views.upload_xlsx.as_view(), name='upload_xlsx'),
    path("txt/upload/", views.upload_txt.as_view(), name='upload_txt'),
