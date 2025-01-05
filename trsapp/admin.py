from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Login_model)
admin.site.register(user_model)
admin.site.register(complaint_model)
admin.site.register(feedback_model)