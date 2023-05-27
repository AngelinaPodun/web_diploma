from django.contrib import admin
from .models import *


# Для отображения данной моделей как дополнительных
class ServiceCategoryInline(admin.TabularInline):
    model = ServiceCategory


class TheServiceInline(admin.TabularInline):
    model = TheService


class CommentsInline(admin.TabularInline):
    model = Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'data', 'promo_info')
    inlines = [CommentsInline]


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'date')


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ("email__startswith", )



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ServiceCategoryInline]


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_of_category', 'service_cat')
    list_filter = ['service_cat']
    inlines = [TheServiceInline]


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('second_name', 'first_name')


@admin.register(TheService)
class TheServiceAdmin(admin.ModelAdmin):
    list_display = ('name_of_service', 'price')
    list_filter = ['service']


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['name_of_sale']

    class Meta:
        model = Sale


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'status', 'data')
    list_filter = ['status']
    search_fields = ("name__startswith", 'phone')


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['img']
