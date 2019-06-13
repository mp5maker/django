from django.contrib import admin

from .models import (
    Images,
    Description
)

admin.site.register(Images)
admin.site.register(Description)