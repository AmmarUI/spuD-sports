from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from .models import Item
from .forms import ItemForm

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import datetime

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        item_list = Item.objects.all()
    else:
        item_list = Item.objects.filter(user=request.user)

    context = {
        'name' : request.user.username,
        'npm' : '2406495994',
        'class' : 'PBP D',
        'item_list': item_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)   

@login_required(login_url='/login')
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method=="POST":
        item_entry = form.save(commit=False)
        item_entry.user = request.user
        item_entry.save() 

        return redirect('main:show_main')
    
    context = {
        'form':form
    }

    return render(request, "create_item.html", context)

def show_item(request, id):
    item = get_object_or_404(Item, pk=id)

    context = {
        'item' : item
    }

    return render(request, 'show_item.html', context)

def edit_item(request, id):
    item = get_object_or_404(Item, pk=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_item.html", context)

def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def login_user(request):
    if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    
    context = {'form': form}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        
    context = {'form':form}
    return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return redirect('main:login')

def show_xml(request):
    item_list = Item.objects.all()
    xml_data = serializers.serialize("xml", item_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    item_list = Item.objects.all()
    data = [
        {
            'id': str(item.id),
            'name': item.name,
            'stock': item.stock,
            'price': item.price,
            'description': item.description,
            'thumbnail': item.thumbnail,
            'category': item.category,
            'is_featured': item.is_featured,
            'user_id': item.user_id,
        }
        for item in item_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, item_id):
   item = Item.objects.filter(pk=item_id)
   xml_data = serializers.serialize("xml",item)
   return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, item_id):
   item = Item.objects.filter(pk=item_id)
   json_data = serializers.serialize("json",item)
   return HttpResponse(json_data, content_type="application/json")

# ---------- AJAX CRUD endpoints ----------

@csrf_exempt
@require_POST
def add_item_entry_ajax(request):
    name = request.POST.get("name")
    stock = request.POST.get("stock")
    price = request.POST.get("price")
    description = request.POST.get("description")
    thumbnail = request.POST.get("thumbnail")
    category = request.POST.get("category")
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user if request.user.is_authenticated else None

    new_item = Item(
        name=name,
        stock=int(stock) if stock else 0,
        price=int(price) if price else 0,
        description=description or '',
        thumbnail=thumbnail or '',
        category=category or 'balls',
        is_featured=is_featured,
        user=user
    )
    new_item.save()
    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def update_item_entry_ajax(request):
    item_id = request.POST.get("id")
    item = get_object_or_404(Item, pk=item_id)

    item.name = request.POST.get("name", item.name)
    item.stock = int(request.POST.get("stock", item.stock))
    item.price = int(request.POST.get("price", item.price))
    item.description = request.POST.get("description", item.description)
    item.thumbnail = request.POST.get("thumbnail", item.thumbnail)
    item.category = request.POST.get("category", item.category)
    item.is_featured = (request.POST.get("is_featured") == 'on')
    item.save()
    return HttpResponse(b"UPDATED", status=200)

@csrf_exempt
@require_POST
def delete_item_ajax(request):
    item_id = request.POST.get("id")
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return HttpResponse(b"DELETED", status=200)

# ---------- AJAX Auth endpoints ----------

@csrf_exempt
@require_POST
def login_ajax(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=400)

@csrf_exempt
@require_POST
def register_ajax(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

def logout_ajax(request):
    logout(request)
    return JsonResponse({'success': True})
