from django.contrib import admin
from .models import Dynamic, DynamicType


@admin.register(Dynamic)
class DynamicAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'get_text', 'type', 'created_time', 'update_time', 'is_public', 'is_delete')


@admin.register(DynamicType)
class DynamicTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'mood_type')
