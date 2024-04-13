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
 users = User.objects.all()
 p=[]
 for user in users:
  user_items = Product.objects.filter(user=user).values('item','date_created','edited','deleted','id')
  serializers = ListSerializers(user_items, many=True).data
  numItems = len(serializers)
  # print(numItems)
  for item in serializers:
   item['user_items']=numItems
   item['added_by']=str(user)
   if user.is_active:
    item['status']='User'
    user.user_permissions.clear()
    TemplateHandler(user,Product)
   if user.is_staff:
    item['status']='Staff'
    TemplateHandler(user,User)
   if user.is_superuser:
    item['status']='Superuser'
    TemplateHandler(user,Group)
   p.append(item) 
 Total_items = len(p)
 print(p)
 return render(request, 'home.html',{'obj':p,'Total':Total_items})

def delItem(request, id):
 get_item = Product.objects.filter(id=id)
 serializers = ListSerializers(get_item, many=True).data
 if request.method == 'POST':
  get_item.delete()
  #code below is self-iterative: it add +1 to all deleted field of req.user
  Product.objects.filter(user=request.user).update(deleted=F("deleted")+1)
  return redirect('home') 
 print(serializers)
 return render(request,'delete.html',{'item':serializers})

def editItem(request,id):
 get_item = Product.objects.filter(id=id)
 item = ListSerializers(get_item, many=True).data
 if request.method=='POST':
  new_item = request.POST['title']
  print(new_item)
  get_item.update(item=new_item, edited=F("edited")+1)
  return redirect('home')
 print(item)
 return render(request,'edit.html',{'item':item})

def checking(request):
 users =User.objects.all()
 if request.method == 'POST':
  users_status = request.POST.getlist('assign')
  privileges(users_status)
  return redirect('home')
 return render(request,'check.html',{'context':users})