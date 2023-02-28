from django import forms 
from .models import CsvFile, TxtFile, XlsxFile

class CsvForm(forms.ModelForm):
    class Meta:
        model = CsvFile
        fields = ('title', 'author', 'csv' )

class XlsxForm(forms.ModelForm):
    class Meta:
        model = XlsxFile
        fields = ('title', 'author', 'xlsx' )

class TxtForm(forms.ModelForm):
    class Meta:
        model = TxtFile
        fields = ('title', 'author', 'txt' )
    