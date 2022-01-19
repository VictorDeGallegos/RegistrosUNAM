"""User admin classes."""

# Django
from django.contrib import admin

# Models
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'user', 'CURP', 'Sueldo',
                    'NumeroTrabajador', 'CorreoElectronico', 'Antiguedad')
    list_display_links = ('pk', 'user',)
    list_editable = ('CURP', 'Sueldo', 'NumeroTrabajador',
                     'CorreoElectronico', 'Antiguedad')

    search_fields = (
        'user__CorreoElectronico',
        'user__username',
        'user__first_name',
        'user__last_name',
        'NumeroTrabajador',
        'CURP'
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )
