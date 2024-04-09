from django.db import models
from django.contrib.auth.models import User,Permission
from django.contrib.contenttypes.models import ContentType

# code templates for privileges to superUser, Staffs and Users

# Create your models here.
def TemplateHandler(model):
 content_type = ContentType.objects.get_for_model(model)
 user_perm = Permission.objects.filter(content_type=content_type)
 return user_perm
 
 # if permission is not None:
 #  for perm in user_perm:
 #   permission.append(perm.codename)
 # else:
 #   permission = [perm.codename for perm in user_perm]


class Product(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
 item = models.CharField(max_length=255)
 date_created = models.DateTimeField(auto_now_add=True, editable=False)
 edited = models.IntegerField(default=0)
 deleted = models.IntegerField(default=0)
