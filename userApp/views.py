from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Product, TemplateHandler,privileges
from .serializers import ListSerializers
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404;
from .serializers import ListSerializers
from django.db.models import F
# Create your views here.

def home(request):
 p=[]
 users = User.objects.all()
 for user in users:
  user_items = Product.objects.filter(user=user).values('item','date_create','edited','deleted','id')
  serializers = ListSerializers(user_items, many=True).data
  numItems = len(serializers)
  # print(numItems)
  for item in serializers:
   item['added_by']=str(user)
   if user.is_active:
    user.user_permissions.clear()
    TemplateHandler(user,Product)
   if user.is_staff:
    TemplateHandler(user,User)
   if user.is_superuser:
    TemplateHandler(user,Group)
   p.append(item) 
 Total_items = len(p)
 print(p)
 return render(request, 'home.html',{'obj':p,'Total':Total_items})

def detailView(request, added_by):
 user = User.objects.filter(username=added_by).values()
 get_id = user.values('id').get()
 print(get_id)
 user_detail=[]
 get_user = Product.objects.filter(user=get_id['id']).values('item','edited','deleted','id')
 for obj in get_user:
  obj['items_added']=get_user.count()
  obj['username']=added_by
  for i in user:
   if i['is_superuser'] == True:
    obj['status']= 'Superuser'
   
   elif i['is_staff']==True:
    obj['status'] = "Staff"
   else:
    obj['status'] ='User'
  user_detail.append(obj)
 context = user_detail[0]
 print(context)
 return render(request,'see.html',{'context':context})

def delItem(request, id):
 get_item = Product.objects.filter(id=id)
 get_id = User.objects.filter(product=id).values('id').get()
 user_products=Product.objects.filter(user=get_id['id']).values()
 serializers = ListSerializers(get_item, many=True).data
 if request.method == 'POST':
  get_item.delete()
  user_products.update(deleted=F('deleted')+1)
  return redirect('home') 
 return render(request,'delete.html',{'item':serializers})

def editItem(request, id):
 get_product = Product.objects.filter(id=id)
 context=get_product.values('item').get()['item']
 get_id = User.objects.filter(product=id).values('id').get()
 user_products=Product.objects.filter(user=get_id['id']).values()
 if request.method =='POST':
  new_prod = request.POST['title']
  get_product.update(item=new_prod)
  user_products.update(edited=F('edited')+1)
  return redirect('home')
 return render(request,'edit.html', {'item':context})

def checking(request):
 users =User.objects.all()
 print(users)
 if request.method == 'POST':
  users_status = request.POST.getlist('assign')
  privileges(users_status)
  return redirect('home')
 return render(request,'check.html',{'context':users})

def addUser(request):
 if request.method =='POST':
  usernm = request.POST['usernm']
  email = request.POST['email']
  passwd = request.POST['passwd']
  if usernm and email and passwd:
   new_user=User.objects.create_user(usernm, email, passwd)
   new_user.save()
   print(new_user)
   messages.success(request, f"{usernm} has been added to the lists of users")
   return redirect('home')
  else:
   messages.error(request, 'Incomplete credentials interested user')
   return redirect('home')
 return render(request, 'userplus.html') 
