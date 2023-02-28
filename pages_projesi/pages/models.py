from django.db import models
from django.core.validators import FileExtensionValidator

image = models.ImageField(upload_to='img')

class CsvFile(models.Model):
    title = models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    csv = models.FileField(upload_to='docs/csvs/',validators=[FileExtensionValidator(allowed_extensions=["csv"])])

    def __str__(self):
        return self.title

class TxtFile(models.Model):
    title = models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    txt = models.FileField(upload_to='docs/txts/',validators=[FileExtensionValidator(allowed_extensions=["txt"])])
    def __str__(self):
        return self.title

class XlsxFile(models.Model):
    title = models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    xlsx = models.FileField(upload_to='docs/xlsxs/',validators=[FileExtensionValidator(allowed_extensions=["xlsx"])])
    def __str__(self):
        return self.title

