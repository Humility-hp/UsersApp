from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, TemplateHandler
from .serializers import ListSerializers
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404;
# Create your views here.
def home(request):
 permission = None
# perm = Permission.objects.filter(user=request.user)
# setting  user's permission
#  if request.user.is_active:
#   request.user.user_permissions.clear()
#   content_type = ContentType.objects.get_for_model(Product)
#   user_perm  = Permission.objects.filter(content_type=content_type)
#   permission = [perm.codename for perm in user_perm]
  
#  if request.user.is_staff:
#   content_type = ContentType.objects.get_for_model(User)
#   staff_perm = Permission.objects.filter(content_type=content_type)
#   print(staff_perm)
#   for perm in staff_perm: 
#     permission.append(perm.codename)

#  if request.user.is_superuser:
#   content_type = ContentType.objects.get_for_model(Group)
#   superuser_perm = Permission.objects.filter(content_type=content_type)
#   for perm in superuser_perm:
#     permission.append(perm.codename)
 if request.user.is_active:
  request.user.user_permissions.clear()
  user_perm=TemplateHandler(Product)
  permission = [perm.codename for perm in user_perm]

 if request.user.is_staff:
  staff_perm = TemplateHandler(User)
  for perm in staff_perm:
   permission.append(perm.codename)

 if request.user.is_superuser:
  super_perm = TemplateHandler(Group)
  for perm in super_perm:
   permission.append(perm.codename)
 
#  request.user.user_permissions.set(permission)
 print(permission)
 users = User.objects.all()
 p=[]
 for user in users:
  user_items = Product.objects.filter(user=user).values('item','date_created','edited','deleted')
  serializers = ListSerializers(user_items, many=True).data
  numItems = len(serializers)
  # print(numItems)
  for item in serializers:
   item['user_items']=numItems
   item['added_by']=str(user)
   if user.is_superuser:
    item['status']='superUser'
   elif user.is_staff:
    item['status']='staff'
   else:
    item['status']='user'
   p.append(item)
 Total_items = len(p)
 return render(request, 'home.html',{'obj':p,'Total':Total_items})

