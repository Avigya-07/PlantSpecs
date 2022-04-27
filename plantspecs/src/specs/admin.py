from django.contrib import admin
from .models import plant,Area,Treatment,plantUpload
# Register your models here.
@admin.register(plant)
class plantAdmin(admin.ModelAdmin):
    list_display=('Common_Name','Scientific_Name','Family','SubFamily')

