from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate,login, update_session_auth_hash
from django.contrib import messages
from .models import fooditem
from .models import Order
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .utils import calculate_total_price


# Create your views here.


# home page and other menu

def home(request):

    items=list(fooditem.objects.all())
    if request.method == 'POST':
        selected_item_ids = request.POST.getlist('selected_items')
        items_dict = [{'id': item.id, 'title': item.title, 'price': item.price, 'image':item.image.url,'rating': item.rating} for item in items]
        
        selected_items = [item for item in items_dict if str(item['id']) in selected_item_ids]

        
        request.session['selected_items'] = selected_items
        return redirect('checkout') 
    return render(request,'home.html',{'items':items})

def breakfast(request):
    items =list(fooditem.objects.filter(category='breakfast'))
    if request.method == 'POST':
        selected_item_ids = request.POST.getlist('selected_items')
        items_dict = [{'id': item.id, 'title': item.title, 'price': item.price, 'image':item.image.url,'rating': item.rating} for item in items]
        
        selected_items = [item for item in items_dict if str(item['id']) in selected_item_ids]
        request.session['selected_items'] = selected_items
        return redirect('checkout')

    return render(request,'breakfast.html',{'items':items})

def lunch(request):
    items =list(fooditem.objects.filter(category='lunch'))
    
    if request.method == 'POST':
        selected_item_ids = request.POST.getlist('selected_items')
        items_dict = [{'id': item.id, 'title': item.title, 'price': item.price, 'image':item.image.url,'rating': item.rating} for item in items]
        
        selected_items = [item for item in items_dict if str(item['id']) in selected_item_ids]
        request.session['selected_items'] = selected_items
        return redirect('checkout')


    return render(request,'lunch.html',{'items':items})

def dinner(request):
    items =list(fooditem.objects.filter(category='dinner'))
    if request.method == 'POST':
        selected_item_ids = request.POST.getlist('selected_items')
        items_dict = [{'id': item.id, 'title': item.title, 'price': item.price, 'image':item.image.url,'rating': item.rating} for item in items]
        
        selected_items = [item for item in items_dict if str(item['id']) in selected_item_ids]
        request.session['selected_items'] = selected_items
        return redirect('checkout')

    return render(request,'dinner.html',{'items':items})

def starter(request):
    items =list(fooditem.objects.filter(category='starter'))
    if request.method == 'POST':
        selected_item_ids = request.POST.getlist('selected_items')
        items_dict = [{'id': item.id, 'title': item.title, 'price': item.price, 'image':item.image.url,'rating': item.rating} for item in items]
        
        selected_items = [item for item in items_dict if str(item['id']) in selected_item_ids]
        request.session['selected_items'] = selected_items
        return redirect('checkout')

    return render(request,'starter.html',{'items':items})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')


# For user login, signup, update, delete

def signup(request):
    if request.method=='POST':
        required_fields = ['first name', 'last name', 'email', 'username', 'password1', 'password2']
        for field in required_fields:
            if not request.POST.get(field):
                messages.info(request, f'{field.capitalize()} cannot be blank.')
                return redirect('signup')

        first_name = request.POST['first name']
        last_name = request.POST['last name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # for default Django password validation requirements 
        try:
            validate_password(password1)
        except ValidationError as e:
            messages.error(request, ' '.join(e.messages))
            return redirect('signup')
        
        # for password mismatch
        if password1!=password2:
            messages.info(request,'confirm password not match')


        elif password1==password2:
            # for username already exist 
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exist')
                
                # create user 
            else:                
                user=User.objects.create_user(first_name=first_name, last_name=last_name,email=email,
                                        username=username,password=password1)

                user.save()
                messages.info(request,'Signup Successfull')


                return redirect('signup')
        else:
            messages.info(request,'invalid credintial')

    return render(request, 'signup.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credintial')
            return redirect('login')
    else:
        return render(request, 'login.html')


# def login_page(request):
#     form = forms.LoginForm()
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             pass
#     return render(request, 'login.html', context={'form': form})

def logout(request):
    auth.logout(request)
    return redirect('login')

def userdetails(request):
          
    user= User.objects.all()
    return render(request,'userdetails.html',{'user': user}) 

def delete_data(request,id):
    if request.method=='POST':
        user_obj =User.objects.get(id=id)
        user_obj.delete()
        return redirect('userdetails')

def update(request,id):
    user_obj = User.objects.get(id=id)

    return render(request,'update.html',{'user':user_obj})

def do_update(request,id):
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    email=request.POST.get('email')

    user_obj = User.objects.get(id=id)

    user_obj.first_name=first_name
    user_obj.last_name=last_name
    user_obj.email=email
    user_obj.save()            
    return redirect('userdetails')

def password_reset(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST,)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password has been successfully changed.')
            return redirect('password_reset')
        
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'password_reset.html', {'form': form,'form_errors': form.errors})

# place_order data from db

def order_data(request):
          
    order= Order.objects.all()
    return render(request,'order_data.html',{'order': order}) 


def delete_order(request,id):
    if request.method=='POST':
        ord=Order.objects.get(id=id)
        ord.delete()
        return redirect('order_data')


#  order section

def makelist(request):
    if request.method == 'POST':
        selected_items = request.POST.getlist('selected_items',[])
        request.session['selected_items'] = selected_items
        return redirect('checkout')  
    return render(request,'home.html')

def checkout(request):
    selected_items = request.session.get('selected_items')
    
    total_price = calculate_total_price(selected_items)

    return render(request, 'checkout.html', {'selected_items': selected_items,'total_price':total_price})


def order_details(request):
    if request.method=='POST':
        customer_name=request.POST.get('customer name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        order_detail=request.POST.get('order detail')
        pincode=request.POST.get('pincode')
        selected_items=request.POST.get('selected items')
        required_fields = ['customer name', 'email', 'address', 'order detail','pincode','selected items']
        for field in required_fields:
            if not request.POST.get(field):
                messages.info(request, f'{field.capitalize()} cannot be blank.')
                return redirect('checkout')
        order=Order(customer_name=customer_name,email=email,address=address,order_detail=order_detail,
                           pincode=pincode,payment_mode=selected_items)

        order.save()
        

        return redirect('feedback')
    else:
        messages.info(request,'Invalid details')

def feedback(request):

    return render(request, 'feedback.html')





        











    



