from django.contrib import admin
from .models import Order

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','size','order_status','size', 'placed_at']
    list_filter=['placed_at','updated_at','order_status']