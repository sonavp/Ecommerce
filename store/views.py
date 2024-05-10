from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from store.forms import Register,Loginform,orderform
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from store.models import Categories,Product,cart,order


def signin_required(fn):
    def wrapper(request,*args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args, **kwargs)
    return wrapper




class Home(ListView):
    model = Categories
    template_name = "store/index.html"
    context_object_name = "categories"

# 
    
# class Collections(ListView):
#     model = Categories
#     template_name = "store/index.html"
#     context_object_name = "categories"

class Category_detail(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        data=Product.objects.filter(categories_id=id)
        name=Categories.objects.get(id=id)
        return render(request,"store/category_detail.html",{"data":data,"name":name})
    
    
class Product_detail(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        
        return render(request,"store/p_detail.html",{"data":data})
    


class Registerview(CreateView):
    template_name = "store/register.html"
    form_class = Register
    model = User
    success_url=reverse_lazy("home")
    
    
class signinview(View):
    
    def get(self,request,*args, **kwargs):
        form=Loginform()
        return render(request,"store/login.html",{"form":form})
    
    def post(self,request,*args, **kwargs):
        form=Loginform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                login(request,user_obj)
                return redirect("home")
            else:
                print("false credentials")
            return redirect("reg")
        
class signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("home")
    
    
   
class Addtocartview(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        data = Product.objects.get(id=id)    
        cart.objects.create(item=data, user=request.user)
        return redirect("home")


class Cart_deleteview(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        cart.objects.get(id=id).delete()
        return redirect("home")

@method_decorator(signin_required,name="dispatch")
class Cart_detailview(View):
    def get(self, request, *args, **kwargs):
        data=cart.objects.filter(user=request.user)
        return render(request,"store/cart.html",{"data":data})
    
    
    
class Orderview(View):
    def get(self,request,*args,**kwargs):
        form=orderform()
        return render(request,"store/orderpage.html",{"form":form})
    
    def post(self,request,*args, **kwargs):
        id = kwargs.get("pk")
        data = Product.objects.get(id=id)    
        form=orderform(request.POST)
        if form.is_valid():
            qs=form.cleaned_data.get("address")
            order.objects.create(address=qs,order_item=data,customer=request.user)
            return redirect("home")
        
        return redirect("cart")
    
class Vieworder(View):
    def get(self,request,*args, **kwargs):
        data=order.objects.filter(customer = request.user)
        return render(request,"store/view_order.html",{"data":data})
    
class Remove_order(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        order.objects.get(id=id).delete()
        return redirect("cart")