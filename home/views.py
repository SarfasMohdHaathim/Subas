from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .send_sms import send_sms
import random
from django.contrib.auth.models import User 
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def home(request):
    return render(request,'index.html')
    



def signup(request):
    if request.method=="POST":
        frist_name=request.POST['frist_name']
        email=request.POST['email']
        username=email.split('@', 1)

        if User.objects.filter(email=email):
            messages.warning(request, 'Email is already exist, Pls Login')
            return redirect('signup')
        else:
            password=request.POST['password']
            corfirm_password=request.POST['repassword']
            if password==corfirm_password:
                    request.session['frist_name'] = frist_name
                    request.session['email'] = email
                    request.session['username'] = username
                    request.session['password'] = password
                                    
                    random_integer = random.randint(11111, 99999)
                    request.session['random_integer'] = random_integer
                    try:
                        message = f'Hi {frist_name} ,Your sign up OTP is {random_integer}'

                        recipient_list = [email]
                        email_from = settings.EMAIL_HOST_USER
                        send_mail( 'OTP', message, email_from, recipient_list )
                        messages.warning(request, 'OTP send Successfully')
                        return redirect('login_otp')

                    except:
                        messages.warning(request, 'Email Failed')
                        return redirect('signup')
    return render(request,'signup.html')






def userlogin(request):
    return render(request,'login.html')



def sign_in(request):
    if request.method == 'POST':
        email=request.POST['email']
        username=email.split('@', 1)
        password=request.POST['password']
        try:
            User.objects.get(email=email)
            
            user=authenticate(request,username=username[0],password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.warning(request, 'Invalid Password')
        except:
            messages.warning(request, 'Invalid Email')

    return render(request,'sign_in.html')


def shop(request):
    product=Product.objects.all()
    context={'product':product}
    recent_products = Product.objects.order_by('-id')[:3]
    context['recent_products'] = recent_products
    if request.method=='GET':
        brand = request.GET.get('brand', None)
        if brand is not None:
            product=Product.objects.filter(brand=brand)
            context={'product':product}

    return render(request,'store.html',context)





def product(request):
    return render(request,'product.html')




def checkout(request):
    return render(request,'checkout.html')




def cart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount=0
    for c in cart:
        value=c.quantity * c.product_name.actual_price
        amount=value+amount
    context={'cart':cart,'amount':amount}
    return render(request,'cart.html',context)



def wishlist(request):
    return render(request,'wishlist.html')



def compare(request):
    return render(request,'compare.html')



def account(request):
    return render(request,'account.html')



def addCart(request,pk):
    user=request.user
    product=Product.objects.get(id=pk)
    cart=Cart.objects.create(user=user,product_name=product)
    return redirect('cart')




def send_otp(request):
    if request.method == 'POST':
        pnumber=request.POST['pnumber']
        random_integer = random.randint(11111, 99999)
        try:
            send_sms(random_integer,pnumber)
            request.session['random_integer'] = random_integer
            messages.success(request, 'OTP send Successfully')
        except:
            messages.success(request, 'Use 7510351030 or 9746717567 because these two  number are verified in twilio others are unverified')
            return redirect(userlogin)

    return redirect(login_otp)



def login_otp(request):
    random_integer = request.session.get('random_integer')
    frist_name = request.session.get('frist_name')
    email = request.session.get('email')
    username = request.session.get('username')
    password = request.session.get('password')
    if request.method == 'POST':
        otp=request.POST['otp']
        if int(random_integer) == int(otp):
            user=User.objects.create_user(
                        first_name=frist_name,
                            username=username[0],
                                email=email,
                                password=password
                              )
            user.save()
            user=authenticate(request,username=username,password=password)            
            messages.success(request, 'OTP matched. You are now logged in!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
    return render(request,'login_otp.html')


def userlogout(request):
    logout(request)
    return redirect('home')




def update_quantity(request,pk):
    if request.method =='POST':
        kjhniuju
        quantity=request.POST['quantity']
        cart=Cart.objects.get(id=pk)
        cart.quantity=quantity
    return redirect('cart')


def delete_cart(request,pk):
    cart=Cart.objects.get(id=pk)
    cart.delete()
    return redirect('cart')

