from django.contrib import admin
from .models import AppDefinition
from markdownify import markdownify

class AppDefinitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'rendered_description')
    readonly_fields = ('rendered_description',)

    def rendered_description(self, obj):
        return markdownify(obj.description)
    rendered_description.short_description = 'Description (Rendered)'

admin.site.register(AppDefinition, AppDefinitionAdmin)
