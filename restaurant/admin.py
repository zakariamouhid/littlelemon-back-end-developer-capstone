from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Menu)

@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'no_of_guests', 'booking_date', 'formatted_date']
    list_filter = ['user', 'booking_date', 'no_of_guests']
    search_fields = ['name', 'user__username', 'user__email']
    readonly_fields = ['id', 'formatted_date']
    date_hierarchy = 'booking_date'
    ordering = ['-booking_date']
    list_per_page = 25
    
    fieldsets = (
        ('Booking Information', {
            'fields': ('id', 'user', 'name', 'no_of_guests', 'booking_date', 'formatted_date')
        }),
    )
    
    def formatted_date(self, obj):
        """Display formatted booking date"""
        if obj.booking_date:
            return obj.booking_date.strftime('%Y-%m-%d %H:%M')
        return '-'
    formatted_date.short_description = 'Formatted Date'