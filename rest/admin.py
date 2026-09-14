from django.contrib import admin
from django.utils.html import format_html
from .models import User, rest


# Admin panel sarlavhalari
admin.site.site_header = "Zenzo Market Admin"
admin.site.site_title = "Zenzo Market"
admin.site.index_title = "Boshqaruv paneli"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'fullname', 'is_blocked', 'is_staff', 'is_superuser')
    list_filter = ('is_blocked', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'fullname')
    ordering = ('-date_joined',)


@admin.register(rest)
class RestAdmin(admin.ModelAdmin):
    # Ro'yxatda ko'rinadigan ustunlar (yangi maydonlar bilan)
    list_display = (
        'id',
        'rasm_preview',
        'nomi',
        'kategoriya',
        'puli',          # ✅ narx emas, puli
        'yulduzi',       # ✅ reyting emas, yulduzi
        'korishi',
        'faol',
    )
    
    # Filterlar
    list_filter = (
        'kategoriya',
        'faol',
    )
    
    # Qidiruv
    search_fields = ('nomi', 'korishi')
    
    # To'g'ridan-to'g'ri tahrirlash
    list_editable = ('puli', 'faol')   # ✅ puli
    
    # Faqat o'qish
    readonly_fields = ('rasm_katta', 'yaratilgan')
    
    # Tartiblash
    ordering = ('-yaratilgan',)
    
    # Sahifa bo'limlari
    fieldsets = (
        ('📦 Asosiy ma\'lumotlar', {
            'fields': ('nomi', 'kategoriya', 'korishi', 'image', 'rasm_katta')
        }),
        ('💰 Narx va reyting', {
            'fields': ('puli', 'yulduzi')   # ✅ yangi maydonlar
        }),
        ('📊 Holat', {
            'fields': ('faol', 'yaratilgan')
        }),
    )
    
    def rasm_preview(self, obj):
        """Ro'yxatdagi kichik rasm"""
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; '
                'object-fit: cover; border-radius: 8px;" />',
                obj.image.url
            )
        return "—"
    rasm_preview.short_description = "Rasm"
    
    def rasm_katta(self, obj):
        """Formadagi katta rasm"""
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 300px; max-height: 300px; '
                'border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);" />',
                obj.image.url
            )
        return "Rasm yuklanmagan"
    rasm_katta.short_description = "Rasm ko'rinishi"