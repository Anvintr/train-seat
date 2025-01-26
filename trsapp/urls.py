
from django.urls import include, path

from .views import *

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('dash', Dashboard.as_view(), name='dash'),
    path('routes', Routes.as_view(), name='routes'),
    path('seats',Seats.as_view(), name='seats'),
    path('stations',Stations.as_view(), name='stations'),
    path('trains',Trains.as_view(), name='trains'),
    path('users',Users.as_view(), name='users'),
    path('viewseat',Viewseat.as_view(), name='viewseat'),
    path('viewstatus',Viewstatus.as_view(), name='viewstatus'),
    path('base',Base.as_view(), name='base'),
    path('compartments',Compartments.as_view(), name='compartments'),
    path('complaints',Complaints.as_view(), name='complaints'),
    path('alert',Alert.as_view(), name='alert'),
    path('bookings',Bookings.as_view(), name='bookings'),
    path('deleteroute/<int:id>',Delete_Route.as_view(),name='deleteroute'),
    path('deletetrain/<int:id>',Delete_Train.as_view(),name='deletetrain'),
    path('editroute/<int:id>',editroute.as_view(),name='editroute'),
    path('status',CreateStatus.as_view(),name='status'),
    path('edittrain/<int:id>',EditTrain.as_view(),name='edittrain'),
    
    
     
     
     
     



]
