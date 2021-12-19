from django.contrib import admin
from demoapp.models import Project, ClientFirm, Language
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.models import LogEntry
# Register your models here.
admin.site.site_title = "Demo Project"
admin.site.site_header = 'Demo Project'
admin.site.index_title = _('Administration')
admin.site.empty_value_display = '-'
# admin.site.index_template = "admin/admin.html"
admin.site.enable_nav_sidebar = False
admin.site.register(LogEntry)

class LanguageAdmin(admin.ModelAdmin):

    fieldsets = [
        [_('Language general information'), {
            'fields': [
                'language', 'lang_abbreviation',
            ]
        }],

    ]
    list_display = (
        'language', 'lang_abbreviation', 'created_date', 'modified_date'
    )


class ClientAdmin(admin.ModelAdmin):

    fieldsets = [
        [_('Client general information'), {
            'fields': [
                'name', 'email', 'country', ('city', 'address')
            ]
        }],

    ]
    list_display = (
        'name', 'email', 'country',
        'address', 'city', 'created_date', 'modified_date'
    )

class ProjectAdmin(admin.ModelAdmin):

    show_change_link = True

    list_display = (
        'name',
        'client',
        'text',
        'user',
        'created_date',
        'modified_date'
    )
    list_filter = ("client", "created_date")




admin.site.register(Language, LanguageAdmin)
admin.site.register(ClientFirm, ClientAdmin)
admin.site.register(Project, ProjectAdmin)