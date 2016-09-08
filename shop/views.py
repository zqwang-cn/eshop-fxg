from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from models import Item,Image,Category,Brand
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def index(request):
    return render(request,'index.html')

def list(request):
    page_item_num=3
    page_range_num=2

    try:
        selected_category=int(request.GET.get('category',-1))
        selected_brand=int(request.GET.get('brand',-1))
    except:
        selected_category=-1
        selected_brand=-1
    all_items=Item.objects.all()
    if selected_category!=-1:
        category=Category.objects.get(id=selected_category)
        all_items=all_items.filter(category=category)
    if selected_brand!=-1:
        brand=Brand.objects.get(id=selected_brand)
        all_items=all_items.filter(brand=brand)
    orderby=request.GET.get('orderby','id')
    all_items=all_items.order_by(orderby)

    paginator=Paginator(all_items,page_item_num)
    page=request.GET.get('page')
    try:
        items=paginator.page(page)
    except PageNotAnInteger:
        items=paginator.page(1)
    except EmptyPage:
        items=paginator.page(paginator.num_pages)
    mid=items.number
    left=range(max(1,mid-page_range_num),mid)
    right=range(mid+1,min(mid+paginator.num_pages,paginator.num_pages)+1)

    params=request.GET.copy()
    if 'page' in params.keys():
        del params['page']
    qs=params.urlencode()
    page_url=reverse('shop.list')+'?'+qs+'&page='

    categories=Category.objects.all()
    brands=Brand.objects.all()
    return render(request,'list.html',{
        'items':items,
        'categories':categories,
        'selected_category':selected_category,
        'brands':brands,
        'selected_brand':selected_brand,
        'orderby':orderby,
        'mid':mid,
        'left':left,
        'right':right,
        'page_url':page_url,
    })

def item(request,id):
    id=int(id)
    item=get_object_or_404(Item,id=id)
    images=Image.objects.filter(item=item)
    return render(request,'item.html',{'item':item,'images':images})

def error404(request):
    return render(request,'404.html')
