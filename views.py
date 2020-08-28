from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from .forms import AddForm, UploadForm
from . import forms
from .models import Product
from datetime import datetime

def load(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_data = request.FILES['file'].read().decode("utf-8")
            rows = file_data.split("\n")
            rows.pop()
            for row in rows:
                fields = row.split(',')
                product = Product()
                product.CustomerId = fields[0]
                product.ProductName = fields[1] or None
                product.Domain = fields[2] or None
                product.StartDate = fields[3] or None
                product.DurationMonths = fields[4] or None
                try:
                    product.full_clean()
                    product.save()
                except ValidationError as e:
                    return render(request, 'load.html', {'error': e.message, 'form': form})
            return render(request, 'load.html', {'success': 'Loaded product(s)', 'form': form})
    else:
        form = UploadForm()
    return render(request, 'load.html', {'form': form})

def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, 'add.html', {'success': 'Saved product', 'form': form})
            except ValidationError as e:
                return render(request, 'add.html', {'error': e.message, 'form': form})
        else:
            return render(request, 'add.html', {'error': 'Validation error', 'form': form})
    else:
        form = AddForm()
    return render(request, 'add.html', {'form': form})

def list(request):
    return render(request, 'list.html', {'products': Product.objects.all()})

def email(request):
    return render(request, 'email.html', {'products': Product.objects.all()})