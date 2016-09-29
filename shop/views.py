from django.shortcuts import render,get_object_or_404,redirect
from django.core.urlresolvers import reverse
from models import Item,Image,Category,Brand,CartItem
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required

# Create your views here.
def error404(request):
    return render(request,'404.html')

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

def add(request):
    user=request.user
    if not user.is_authenticated():
        return HttpResponse("not signed in")
    id=int(request.GET.get('id'))
    num=int(request.GET.get('num'))
    if num<1 or num>99:
        return HttpResponse("invalid num")
    item=get_object_or_404(Item,id=id)
    try:
        cartitem=CartItem.objects.get(user=user,item=item)
        cartitem.num=cartitem.num+num
        if cartitem.num>99:
            cartitem.num=99
        cartitem.save()
    except:
        cartitem=CartItem()
        cartitem.user=user
        cartitem.item=item
        cartitem.num=num
        cartitem.save()
    return HttpResponse("success")

def delete(request):
    user=request.user
    if not user.is_authenticated():
        return HttpResponse("not signed in")
    id=int(request.GET.get('id'))
    cartitem=get_object_or_404(CartItem,id=id)
    cartitem.delete()
    return HttpResponse("success")

def update(request):
    user=request.user
    if not user.is_authenticated():
        return HttpResponse("not signed in")
    for k,v in request.GET.items():
        id=int(k)
        num=int(v)
        if num<1 or num>99:
            return HttpResponse("invalid num")
        cartitem=get_object_or_404(CartItem,id=id)
        cartitem.num=num
        cartitem.save()
    return HttpResponse("success")

@login_required
def cart(request):
    cartitems=CartItem.objects.filter(user=request.user)
    total=0
    for cartitem in cartitems:
        cartitem.total=cartitem.item.price*cartitem.num
        total+=cartitem.total
    return render(request,'cart.html',{ 'cartitems':cartitems,'total':total })
