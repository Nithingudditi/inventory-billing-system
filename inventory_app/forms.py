from django import forms
from .models import Product,Customer


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'stock_quantity']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','email','phone']
        
