from django.db import models
from django.contrib.auth.models import User,Permission
from django.contrib.contenttypes.models import ContentType

# code templates for privileges to superUser, Staffs and Users

# Create your models here.
def TemplateHandler(user,model):
 single_perm = []
 content_type = ContentType.objects.get_for_model(model)
 user_perms = Permission.objects.filter(content_type=content_type)
 for user_perm in user_perms:
  perm = Permission.objects.get(
   codename = user_perm.codename,
   content_type = content_type
  )
  single_perm.append(perm)
 for perm in single_perm:
  user.user_permissions.add(perm)
 
# code template for user privileges
def privileges(list_users):
 for items in list_users:
  status_name=items.split('-')
  get_user = User.objects.get(username=status_name[1])
  if status_name[0] == 'Super_user':
   get_user.is_active = True
   get_user.is_staff = True
   get_user.is_superuser = True
  elif status_name[0] == 'Staff':
   get_user.is_active = True
   get_user.is_staff = True
   get_user.is_superuser = False
  elif status_name[0] == 'User':
   get_user.is_active = True
   get_user.is_staff = False
   get_user.is_superuser = False
  else:
   get_user.delete()
  get_user.save()


class Product(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
 item = models.CharField(max_length=255)
 date_created = models.DateTimeField(auto_now_add=True)
 edited = models.IntegerField(default=0)
 deleted = models.IntegerField(default=0)