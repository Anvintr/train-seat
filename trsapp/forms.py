
from django.forms import ModelForm

from trsapp.models import *



class Routes_form(ModelForm):
    class Meta:
        model = Route_model
        fields = ['source','destination']
    

class train_form(ModelForm):
    class Meta:
        model = Train_model
        fields = ['ROUTE_ID','train_number','train_name']