from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.http import JsonResponse

from . models import regtb_user

def register(request):

    if request.method=='POST':
        name1=request.POST.get('nm')
        mob1=request.POST.get('mb')
        em1=request.POST.get('em')
        ps1=request.POST.get('ps')
        obj=regtb_user.objects.create(username=name1,mobilenumber=mob1,email=em1,password=ps1)
        obj.save()
        return render(request,'reg.html')
    else:
        return render(request,'reg.html')
def login(request):
    if request.method=='POST':
        email=request.POST.get('log_em')
        pswd=request.POST.get('log_ps')
        obj=regtb_user.objects.filter(email=email,password=pswd)
        if obj:
            request.session['user_email']=email
            request.session['user_pass']=pswd
            for i in obj:
                request.session['userid']=i.id
                return render(request,'profile.html')
        else:
            return render(request,'login.html',{"log_error":"inalid email id or password"})
    else:
        return render(request,'login.html')
    

def login_process(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Authentication successful
            return JsonResponse({'message': 'Login successful', 'email': user.email})
        else:
            # Authentication failed
            return JsonResponse({'message': 'Login failed'}, status=401)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def mock_api_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'testuser' and password == 'testpassword':
            return JsonResponse({'email': 'testuser@example.com'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
# Create your views here.
