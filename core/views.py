from django.shortcuts import render
from core.models import Category

# from django.http import HttpResponse

# Create your views here.
def index(request):
    categores = Category.objects.all()[0:10]
    topcategores = Category.objects.all()[0:3]
    
    return render(request ,"index.html",
    context = {
        'categores':categores,
        'topcategores':topcategores,
    }
                  )

def product_detials(request):
    return render(request , 'product.html')

def store(request):
    return render(request , 'store.html')

def checkout(request):
    return render(request , 'checkout.html')