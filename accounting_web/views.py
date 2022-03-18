from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.
class Home(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Home Page")

class Login(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'logingForm.html')
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
                'err_active':'err_active',
                'username' : username}
            return render(request, 'logingForm.html', content)
