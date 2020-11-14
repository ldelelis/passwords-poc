from django.contrib import admin

from core.models import DynamicPasswordValidator


# Register your models here.
@admin.register(DynamicPasswordValidator)
class DynamicPasswordValidatorAdmin(admin.ModelAdmin):
    pass

