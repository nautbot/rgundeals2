from django.contrib import admin
from django.db.models import Count
from django.utils import timezone

from .models import Category, Comment, Deal, Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'domains', 'url', 'deal_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'domains', 'url')

    def get_queryset(self, request):
        # Include count of assigned deals
        qs = super().get_queryset(request)
        return qs.annotate(deal_count=Count('deals'))

    def deal_count(self, instance):
        return instance.deal_count
    deal_count.admin_order_field = 'deal_count'
    deal_count.short_description = 'Deals'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug', 'deal_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')

    def get_queryset(self, request):
        # Include count of assigned deals
        qs = super().get_queryset(request)
        return qs.annotate(deal_count=Count('deals'))

    def deal_count(self, instance):
        return instance.deal_count
    deal_count.admin_order_field = 'deal_count'
    deal_count.short_description = 'Deals'


def set_locked(modeladmin, request, queryset):
    queryset.update(locked=True)
set_locked.short_description = "Lock selected deals"


def set_out_of_stock(modeladmin, request, queryset):
    queryset.update(out_of_stock=True)
set_out_of_stock.short_description = "Mark selected deals out of stock"


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    actions = (set_locked, set_out_of_stock)
    list_display = ('title', 'score', 'created', 'created_by', 'vendor', 'locked', 'out_of_stock')
    list_filter = ('locked', 'out_of_stock', 'created', 'vendor')
    search_fields = ('title', 'url', 'description', 'created_by__username')

    def save_model(self, request, obj, form, change):

        # Record the creation/edit user
        if not obj.pk:
            obj.created_by = request.user
        else:
            obj.edited = timezone.now()
            obj.edited_by = request.user

        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'created', 'deal')
