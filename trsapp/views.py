
from pyexpat.errors import messages
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from trsapp.forms import Routes_form, train_form

from .models import Login_model, Route_model, Train_model, complaint_model, user_model

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'Administrator/login.html')
    def post(self, request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        obj=Login_model.objects.get(username=username,password=password)
        if obj.usertype=='admin':
            return HttpResponse('''<script>alert("login successfully");window.location='/dash'</script>''')
        # elif obj.type=='user':
        #     return render(request,'Userdashboard.html')
        else :
            return HttpResponse("User type not recognized")
        
    


class Dashboard(View):
    def get(self, request):
        return render(request, 'Administrator/dashboard.html')
    
    
class Routes(View):
    def get(self, request):
        c=Route_model.objects.all()
        return render(request, 'Administrator/routes.html', {'a':c})
    def post(self, request):
        c=Routes_form(request.POST)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert("route added successfully");window.location='/routes'</script>''')
        
class Delete_Route(View):
    def get(self, request, id):
        c=Route_model.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert("route deleted successfully");window.location='/routes'</script>''')
    
class Seats(View):
    def get(self, request):
        return render(request, 'Administrator/seats.html')
    
class editroute(View):
    def get(self, request, id):
        c=Route_model.objects.get(id=id)
        return render(request, 'Administrator/editroute.html', {'a':c})
    def post(self, request, id):
        c=Route_model.objects.get(id=id)
        d=Routes_form(request.POST, instance=c)
        if d.is_valid():
            d.save()
            return HttpResponse('''<script>alert("route updated successfully");window.location='/routes'</script>'''
            )
    
class Stations(View):
    def get(self, request):
        return render(request, 'Administrator/stations.html')



class Trains(View):
    def get(self, request):
        c=Route_model.objects.all()
        d = Train_model.objects.all()
        return render(request, 'Administrator/trains.html', {'a':c, 'd':d})
    def post(self, request):
        c=train_form(request.POST)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert("train added successfully");window.location='/trains'</script>''')
        
class Delete_Train(View):
    def get(self, request, id):
        c=Train_model.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert("train deleted successfully");window.location='/trains'</script>''')
    
class EditTrain(View):
    def get(self, request, id):
        c=Train_model.objects.get(id=id)
        return render(request, 'Administrator/edittrain.html', {'a':c})

    
    
class Users(View):
    def get(self, request):
        c=user_model.objects.all()
        return render(request, 'Administrator/users.html', {'a':c})
    
class Viewseat(View):
    def get(self, request):
        return render(request, 'Administrator/viewseat.html')
    
class Base(View):
    def get(self, request):
        return render(request, 'Administrator/base.html')
    
class Compartments(View):
    def get(self, request):
        return render(request, 'Administrator/compartments.html')
    
class Complaints(View):
    def get(self, request):
        d=complaint_model.objects.all()
        return render(request, 'Administrator/complaints.html',{'b':d})
    
class CreateStatus(View):
    def get(self, request):
        return render(request, 'Administrator/createStatus.html')
    
    
class Viewstatus(View):
    def get(self, request):
        return render(request, 'Administrator/viewStatus.html')
    
class Alert(View):
    def get(self, request):
        return render(request, 'Administrator/alert.html')
class Bookings(View):
    def get(self, request):
        return render(request, 'Administrator/bookings.html')
    
    
    

    
     