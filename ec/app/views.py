# from db.models import Count
from django.shortcuts import render,redirect
from django.views import View
from . models import Product
# from . import CustomerRegistrationFrom
# from . import CustomerProfileForm
# from django.contrib import massages
from .models import Customer

def home(request):
    return render(request, 'app/home.html')

def about(request):
     return render(request, 'app/about.html')

def contect(request):
     return render(request, 'app/contect.html')

class CategoryView(View):
     def get(self,request,val):
          product = Product.objects.filter(category=val)
          title = Product.objects.filter(category=val).values('title').annotate(total=count('title'))
          return render(request,'app/category.html')

class CategoryTitle(View):
     def get(self,request,val):
          product = Product.objects.filter(title=val)
          title = Product.objects.filter(category=product[0].category).values('title')
          return render(request,'app/category.html')          

class Productdetail(View):
    def get(self,request,pk):
     #    product = Product.objects.get()
        product = Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',locals())

# class CustomerRegistrationView(View):
#      def get(self,request):
#          form = CustomerRegistrationFrom
#          return render(request,'app/customerregistration.html',locals()) 
#      def post(self,request):
#           form = CustomerRegistrationFrom(request.post)
#           if form.is_valid():
#                form.save()
#                massages.success(request,'Congratulation! User Register Successfully')
#           else:
#                massages.warning(request,'Invalied Input Data')
#                return render(request,'app/customerregistration.html',locals()) 

# class ProfileView(View):
#      def get(self,request):
#           form = CustomerProfileForm()
#           return render(request, 'app/profile.html',locals())
#      def post(self,request):
#           form = CustomerProfileForm(request.POST)
#           if form.is_vaild():
#                user = request.user
#                name = form.cleaned_data['name']
#                locality = form.cleaned_data['locality']
#                city = form.cleaned_data['city']
#                mobile = form.cleaned_data['mobile']
#                state = form.cleaned_data['state']
#                zipcode = form.cleaned_data['zipcode']

#                reg = Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,state=state,zipcode=zipcode)
#                reg.save()
#                massages.success(request,'Congratulation! User Register Successfully')
#           else:
#                massages.warning(request,'Invalied Input Data')

#           return render(request, 'app/profile.html',locals())

# def address(request):
#      add = Customer.objects.filter(user=request.user)
#      return render(request,'app/address.html',locals())

# class updateAddress(View):
#      def get(self,request,pk):
#           add = Customer.objects.get(pk=pk)
#           form = CustomerProfileForm(instance=add)
#           return render(request,'app/updateAddress.html',locals())
#      def post(self,request,pk):
#           form = CustomerProfileForm(request.POST)
#           if form.is_valid():
#                add = Customer.objects.get(pk=pk)
#                add.name = form.cleaned_data['name']
#                add.locality = form.cleaned_data['locality']
#                add.city = form.cleaned_data['city']
#                add.mobile = form.cleaned_data['mobile']
#                add.state = form.cleaned_data['state']
#                add.zipcode = form.cleaned_data['zipcode']
#                add.save()
#                massages.success(request,'Congratulation! User Register Successfully')
#           else:
#                massages.warning(request,'Invalied Input Data')
#           return redirect('address')
     

