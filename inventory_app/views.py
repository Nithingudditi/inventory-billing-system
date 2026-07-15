from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Customer,Order,OrderItem
from .forms import ProductForm,CustomerForm,OrderForm,OrderItemFormSet



# ---------- PRODUCT VIEWS ----------

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory_app/product_list.html', {'products': products})

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request,"inventory_app/product_form.html", {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory_app/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'inventory_app/product_confirm_delete.html', {'product': product})



# ---------- CUSTOMER VIEWS ----------

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'inventory_app/customer_list.html', {'customers': customers})


def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'inventory_app/customer_form.html', {'form': form})


def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'inventory_app/customer_form.html', {'form': form})


def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'inventory_app/customer_confirm_delete.html', {'customer': customer})


# ---------- ORDER VIEWS ----------


def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            formset = OrderItemFormSet(request.POST, instance=order)
            if formset.is_valid():
                items = formset.save()
                for item in items:
                    item.product.stock_quantity -= item.quantity
                    item.product.save()
                return redirect('order_list')
            else:
                order.delete()
        else:
            formset = OrderItemFormSet(request.POST)
    else:
        form = OrderForm()
        formset = OrderItemFormSet()

    return render(request, 'inventory_app/order_form.html', {'form': form, 'formset': formset})



def order_list(request):
    orders = Order.objects.all()
    return render(request, 'inventory_app/order_list.html', {'orders': orders})