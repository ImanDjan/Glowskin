from django.contrib import admin
from .models import Articles
from .models import User


admin.site.register(Articles)
admin.site.register(User)
