from django.shortcuts import render,get_object_or_404
from models import Item,Image

# Create your views here.
def index(request):
    return render(request,'index.html')

def all(request):
    pass

def item(request,id):
    id=int(id)
    item=get_object_or_404(Item,id=id)
    images=Image.objects.filter(item=item)
    print images[0].img.url
    return render(request,'item.html',{'item':item,'images':images,'image':images[0]})
