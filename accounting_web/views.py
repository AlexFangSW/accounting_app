from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
import datetime

from .models import Record
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RecordSerializer, UserSerializer

from .models import Record

# REST
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Record.objects.all().order_by('-date')
    serializer_class = RecordSerializer
    # permission_classes = [permissions.IsAuthenticated]


# Create your views here.
class Login(View):
    
    def get(self, request, *args, **kwargs):
        content = {
            'err_active':'d-none'
        }
        
        return render(request, 'loginForm.html', content)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Success

            return redirect('home') # Use url name
        else:
            # Fail
            content = {
                'err_active':'d-block',
                'username': username
            }

            return render(request, 'loginForm.html', content)

class Home(View):
    
    def getRecords(self, userName):
        records = Record.objects.filter(user_name__exact=userName).order_by('-date')
        data = []
        lastMonth = 0
        firstOfMonth = False

        for record in records:
            if record.date.month != lastMonth:
                firstOfMonth = record.date.month
                lastMonth = record.date.month
            else:
                firstOfMonth = False

            data.append({
                    'firstOfMonth' : firstOfMonth,
                    'data' : record
                })

        return data
    
    def addRecords(self, user_name, data):
        temp = Record(
            user_name=user_name,
            activaty=data['activaty'],
            price=data['price'],
            date=data['date']
        )
        temp.save()

        return

    def get(self, request, *args, **kwargs):
        content = {
            'title': 'Home',
            'records': self.getRecords(request.user)
        }

        return render(request, 'home.html', content)
    
    def post(self, request, *args, **kwargs):
        self.addRecords(request.user, request.POST)
        content = {
            'title': 'Home',
            'records': self.getRecords(request.user)
        }

        return render(request, 'home.html', content)

class SignUp(View):

    def get(self, request, *args, **kwargs):
        content = {
            'title': 'Sign Up'
        }

        return render(request, 'signUp.html', content)

class Search(View):

    def get(self, request, *args, **kwargs):
        content = {
            'title': 'Search'
        }

        return render(request, 'search.html', content)
