from django import forms
from .models import Product,Customer,Order,OrderItem
from django.forms import inlineformset_factory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'stock_quantity']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','email','phone']
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer','status']

OrderItemFormSet = inlineformset_factory(
    Order,
    OrderItem,
    fields=['product','quantity','price_at_purchase'],
    extra=3,
    can_delete=True
)