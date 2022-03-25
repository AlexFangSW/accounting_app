from typing import Any, Dict, List
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
import datetime

from .models import Record, Tag
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RecordSerializer, UserSerializer, TagSerializer

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

class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tag.objects.all().order_by('tag_name')
    serializer_class = TagSerializer
    # permission_classes = [permissions.IsAuthenticated]

# Create your views here.
class Login(View):
    
    def get(self, request, *args, **kwargs):
        
        logout(request)

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

            return redirect('home')
        else:
            # Fail
            content = {
                'err_active':'d-block',
                'username': username
            }

            return render(request, 'loginForm.html', content)

class Home(View):
    """
    Home page of the Accounting app.
    Users can add records here.
    """
    def get_records(self, user: User) -> List[Dict[str, Any]]:
        """
        Get current user's records.And add some value for randering
        
        Args:
            user:
                current user.
        
        Returns:
            A list of dictionary with record and info for randering.
            example:
                [{
                    'first_of_month' : False,   # No need to render record's month on top.
                    'data' : record
                    'str_date' : str_date
                },
                {
                    'first_of_month' : 3,   # Will rander '3月' on top of the record.
                    'data' : record
                    'str_date' : str_date
                }]

        """
        records = Record.objects.filter(user__exact=user).order_by('-date')
        data = []
        last_month = 0
        first_of_month = False

        for record in records:
            if record.date.month != last_month:
                first_of_month = record.date.month
                last_month = record.date.month
            else:
                first_of_month = False

            str_date = str(record.date)

            data.append({
                    'first_of_month' : first_of_month,
                    'data' : record,
                    'str_date' : str_date
                })

        return data
    
    def add_records(self, user: User, data: Dict[str, Any]) -> None:

        temp = Record(
            user=user,
            income_or_expense=data['income_or_expense'],
            tag_name=Tag.objects.filter(tag_name__exact=data['tag_name'])[0],
            discription=data['discription'],
            price=data['price'],
            date=data['date']
        )

        temp.save()

        return
    
    def get_tags(self, user: User) -> Dict[str, List[Tag]]:

        tags = Tag.objects.filter(user__exact=user).order_by('tag_name')
        tag_dict = {
            'income' : tags.filter(income_or_expense__exact='收入'),
            'expense' : tags.filter(income_or_expense__exact='支出')
        }

        return tag_dict

    def get(self, request, *args, **kwargs):

        if (not request.user.is_authenticated):
            return redirect('login')

        content = {
            'title': 'Home',
            'user' : request.user,
            'records': self.get_records(request.user),
            'tags' : self.get_tags(request.user)
        }

        return render(request, 'home.html', content)
    
    def post(self, request, *args, **kwargs):

        self.add_records(request.user, request.POST)
        content = {
            'title': 'Home',
            'user' : request.user,
            'records': self.get_records(request.user),
            'tags' : self.get_tags(request.user)
        }

        return render(request, 'home.html', content)

class SignUp(View):

    def get(self, request, *args, **kwargs):
        content = {
            'title': 'Sign Up',
            'err_active':'d-none'
        }

        return render(request, 'signUp.html', content)

    def post(self, request, *args, **kwargs):

        username = request.POST['username']
        password = request.POST['password']
        password_re = request.POST['password_re']

        username.replace(" ", "")
        password.replace(" ", "")
        password_re.replace(" ", "")

        if (len(password) > 0 and len(username) > 0 and password_re == password):

            user = User.objects.create_user(username=username, password=password)

            return redirect('login')
        else:

            content = {
                'err_active':'d-block',
                'username': username
            }

            return render(request, 'signUp.html', content)

class Search(View):
    """
    Search Page.
    For users to search records.
    """

    def get(self, request, *args, **kwargs):

        if (not request.user.is_authenticated):
            return redirect('login')
        
        content = {
            'title': 'Search',
            'user' : request.user,
        }

        return render(request, 'search.html', content)
