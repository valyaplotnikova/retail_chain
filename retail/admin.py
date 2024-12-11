from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from retail.models import Link, Product


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_name', 'email', 'country', 'city', 'street', 'house_number',
                    'provider_link', 'debt', 'created_at', 'level', 'type')
    list_filter = ('city',)
    list_display_links = ('link_name',)
    search_fields = ('link_name', 'email', 'country', 'city', 'debt', 'level', 'type')
    actions = ['clear_debt']

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    @admin.display(description="Поставщик")
    def provider_link(self, obj):
        """ Ссылка для перехода в карточку поставщика. """
        if obj.provider:
            url = reverse(f'admin:retail_link_change', args=[obj.provider.pk])
            return format_html('<a href="{}">{}</a>', url, obj.provider)
        return '-'

    provider_link.short_description = 'Поставщик'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_model', 'date_realise', 'provider')
    list_filter = ('product_name', 'product_model', 'date_realise', 'provider')
    search_fields = ('product_name', 'product_model', 'date_realise', 'provider')
    list_display_links = ('product_name',)
