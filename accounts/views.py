from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username =username ,password =password)

        if user is not None:
            auth.login(request ,user)
            return redirect('/')

        else:
            messages.info(request , 'Invalid username or password ')  
            return redirect('login')  

    else:
        return render(request , 'login.html')



def register(request):
    

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password2 == password:
            if User.objects.filter(username = username).exists():
                #print('username already exists')
                messages.info(request , 'username already exists !')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request , 'email id already taken !')
                return redirect('register')
                #print('email id already taken !')

            else:    
                user = User.objects.create_user(username=username , password=password, email=email, first_name =first_name , last_name =last_name)
                user.save();
                #print('successfully submitted')
                messages.info(request , 'successfully submitted !')
                return redirect('login')

            
        else:
            #print('password not matching') 
            messages.info(request , 'password not matching !')
            return redirect('register')
   
        return redirect('/')
        
 
    else:

        return render(request , 'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')        


    