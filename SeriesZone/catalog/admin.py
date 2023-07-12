from django.contrib import admin
from . import models


admin.site.register(models.Serial)
admin.site.register(models.Series)
admin.site.register(models.Season)
admin.site.register(models.Category)