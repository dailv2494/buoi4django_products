from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
products = [
    {'id': 1, 'code': '10001', 'name': 'Product 1', 'price': 10000},
    {'id': 2, 'code': '10002', 'name': 'Product 2', 'price': 20000},
]



def index(request):
    context = {'products': products}
    return render(request, 'index.html', context)

def createCategory(request):
    form=CategoryForm()
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    return render(request,'category_form.html',{'form':form})

def updateCategory(request,id):
    category=get_object_or_404(Category,pk=id)
    form=CategoryForm(instance=category)
    if request.method=='POST':
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('category-list')

    return render(request,'category_form.html',{'form':form})

def deleteCategory(request,id):
    c=get_object_or_404(Category,pk=id)
    c.delete()
    return redirect('category-list')

def listCategory(request):
    categoryList=Category.objects.all()
    return render(request,'category_list.html',{'categoryList':categoryList})






    # def createCategory(request):
    #     return render(request,'category_form.html')
    # def updateCategory(request,id):
    #     return render(request,'category_form.html')
    # def deleteCategory(request,id):
    #     return redirect('category-list')
    # def listCategory(request):
    #     return render(request,'category_list.html')
def listProduct(request):
    productList=Product.objects.all()
    return render(request,'product_list.html',{'productList':productList})

def createProduct(request):
    form=ProductForm()
    if request.method=='POST':
        form =ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'product_form.html',{'form':form})

def updateProduct(request,id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')

    # return render(request, 'category_form.html', {'form': form})
    return render(request,'product_form.html',{'form':form})

def deleteProduct(request,id):
    c=get_object_or_404(Product,pk=id)
    c.delete()
    return redirect('product-list')
