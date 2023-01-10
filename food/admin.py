from django.contrib import admin
from .models import Category, Food, Table, BookTable, Response, Event
from django.utils.safestring import mark_safe


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class FoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_image', 'price', 'category', 'desc']
    list_filter = ['category']
    search_fields = ['name', 'desc']
    list_editable = ['price']
    list_display_links = ['get_image']

    def get_image(self, obj):
        if obj.img:
            return mark_safe(f"<img src={obj.img.url} width='100' height='100'")
        return mark_safe(f"<img src='not_found.png'")


class TableAdmin(admin.ModelAdmin):
    list_display = ['name']


class BookTableAdmin(admin.ModelAdmin):
    list_display = ['name', 'table', 'phone', 'date', 'persons', 'message']


class ResponseAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'message']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(BookTable, BookTableAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Event)
