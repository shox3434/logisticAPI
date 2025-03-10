from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, DriverProfile, Cargo, CargoReview

# Custom User uchun Admin
class UserAdmin(BaseUserAdmin):
    list_display = ('phone_number', 'name', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('phone_number', 'name', 'email')
    ordering = ('phone_number',)
    
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal Info', {'fields': ('name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'name', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    filter_horizontal = ()  # Bo‘sh qilib qo‘yamiz, chunki groups va user_permissions yo‘q

# DriverProfile uchun Admin
class DriverProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle_type', 'license_type', 'vehicle_capacity', 'experience')
    list_filter = ('vehicle_type',)
    search_fields = ('user__phone_number', 'user__name', 'vehicle_type')

# Cargo uchun Admin
class CargoAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer', 'driver', 'vehicle_type', 'status', 'created_at')
    list_filter = ('vehicle_type', 'status')
    search_fields = ('name', 'customer__phone_number', 'driver__user__phone_number')
    list_editable = ('status',)

# CargoReview uchun Admin
class CargoReviewAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'customer', 'comment', 'created_at')
    search_fields = ('cargo__name', 'customer__phone_number', 'comment')

# Modellarni ro‘yxatdan o‘tkazish
admin.site.register(User, UserAdmin)
admin.site.register(DriverProfile, DriverProfileAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(CargoReview, CargoReviewAdmin)