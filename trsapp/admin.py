from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Login_model)
admin.site.register(user_model)
admin.site.register(complaint_model)
admin.site.register(feedback_model)
admin.site.register(Train_model) 
admin.site.register(Route_model)
admin.site.register(Station_model)
admin.site.register(Seat_model)
admin.site.register(Status_model)
admin.site.register(Alert_model)
admin.site.register(Booking_model)
admin.site.register(Compartment_model)