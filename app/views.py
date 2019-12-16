from django.shortcuts import render

products = [
    {'id': 1, 'code': '10001', 'name': 'Product 1', 'price': 10000},
    {'id': 2, 'code': '10002', 'name': 'Product 2', 'price': 20000},
]

def index(request):
    context = {'products': products}
    return render(request, 'index.html', context)