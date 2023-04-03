from django.shortcuts import render,redirect
from app1.models import *
from django.contrib import messages

def log_in(request):
    return render(request,'login.html')
def relogin(request):
    return redirect('/')
def login(request):
    errors = User.objects.log_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    user = User.objects.filter(email=request.POST['email'])

    if user:
        if bcrypt.checkpw(request.POST['pwd'].encode(), user[0].password.encode()):
            request.session['user']=user[0].id

            return redirect('/home')
def sign_up(request):
    
    return render(request,'register.html')
def signup(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/sign_up')
    else:
        password = request.POST['pwd']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user=User.objects.create(first_name=request.POST['first_name'],
                            last_name=request.POST['last_name'],
                            email=request.POST['email'],
                            password=pw_hash)
        request.session['userid']=user.id
        return redirect('/home')
def home(request):
        if 'user'not in request.session:
            return redirect('/')
        data={
        'user':User.objects.all(),
        'userid':User.objects.get(id=request.session['user']),
        }
        return render(request,'home.html',data)
def log_out(request):
    request.session.clear()
    return redirect('/')

# Create your views here.
