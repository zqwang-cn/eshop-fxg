from django.shortcuts import render,get_object_or_404
from models import Item,Image,Category

# Create your views here.
def index(request):
    return render(request,'index.html')

def url_replace(parmas,key,value):
    params[key]=value
    return params.urlencode()

def list(request):
    params=request.GET.copy()
    orderby=params.get('orderby','id')
    items=Item.objects.order_by(orderby)
    return render(request,'list.html',{'items':items,"url_replace":url_replace})

def item(request,id):
    id=int(id)
    item=get_object_or_404(Item,id=id)
    images=Image.objects.filter(item=item)
    return render(request,'item.html',{'item':item,'images':images})

def error404(request):
    return render(request,'404.html')
