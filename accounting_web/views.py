from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
import datetime

from .models import Record

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
    
    def getRecords(self):
        records = Record.objects.all().order_by('-date')
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

        print(data)

        return data

    def get(self, request, *args, **kwargs):
        content = {
            'title': 'Home',
            'records': self.getRecords()
        }

        return render(request, 'home.html', content)
    
    def post(self, request, *args, **kwargs):
        content = {
            'title': 'Home',
            'records': self.getRecords()
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
