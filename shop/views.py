from django.shortcuts import render,get_object_or_404
from models import Item,Image,Category

# Create your views here.
def index(request):
    return render(request,'index.html')

def all(request):
    orderby=request.GET.get('orderby','id')
    items=Item.objects.order_by(orderby)
    categories=Category.objects.all()
    return render(request,'all.html',{'items':items,'categories':categories})

def item(request,id):
    id=int(id)
    item=get_object_or_404(Item,id=id)
    images=Image.objects.filter(item=item)
    return render(request,'item.html',{'item':item,'images':images})

def error404(request):
    return render(request,'404.html')
