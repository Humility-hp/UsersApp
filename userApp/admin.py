from collections.abc import Callable
from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Product
from django.contrib.auth.models import User, Group
# Register your models here.
# Only superusers can delete and edit items, other users can't
@admin.register(Product)
class TestAdmin(admin.ModelAdmin):
 def has_delete_permission(self, request, obj=None):
  permit = super().has_delete_permission(request)
  if request.user.is_superuser == True:
    return permit is True 
  else:
    return permit is False
  
 def has_change_permission(self,request,obj=None):
  permit = super().has_change_permission(request,obj)
  if request.user.is_superuser == True:
   return permit is True
  else:
   return permit is False
  

# class permitDel(admin.ModelAdmin):
#  def get_actions(self,request):
#   actions = super().get_action(request)
#   print(actions)
#   if request.user.username == "Desmond":
#    if "delete_selected" in actions:
#     del actions["delete_selected"]
#   return actions






# below is how to get the for any model type

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#  def get_form(self, request, obj, **kwargs):
#   form = super().get_form(request, obj, **kwargs)
  

#  def get_form(self, request, obj, **kwargs):
#   form = super().get_form(request, obj, **kwargs)
#   is_superuser = request.user.is_superuser
#   if not is_superuser:
#    print(obj)
#    form.base_fields['user'].disabled = True
#   return form