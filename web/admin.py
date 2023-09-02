from django.contrib import admin
from .models import Store, Category, Coupon

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

# @admin.register(Deal)
# class DealAdmin(admin.ModelAdmin):
#     list_display = ('name', 'image', 'description', 'coupon_code', 'store', 'category', 'expires_at', 'added_at', 'clicks')

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'coupon_code', 'store', 'category', 'is_deal', 'expires_at', 'added_at', 'clicks')
