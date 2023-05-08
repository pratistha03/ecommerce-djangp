from django.db.models import Count
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from .models import Customer, Product, Contact
from .forms import CustomerRegistrationForm, CustomerProfileForm, ContactForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView



class CategoryView(View):
    def get(self, request, val):
        product=Product.objects.filter(category=val)
        title= Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())
    

class CategoryTitle(View):
    def get(self, request, val):
        product=Product.objects.filter(title=val)
        title= Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html", locals())
    

class ProductDetail(View):
    def get(self, request, pk):
        product=Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html", locals())

class CustomerRegistrationView(View):
    def get(self, request):
        form=CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', locals())
    def post(self, request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Registered Successfully!")
        else:
            messages.warning(request, "Invalid Input")

        return render(request, 'app/customerregistration.html', locals())


class ProfileView(View):
    def get(self, request):
        form=CustomerProfileForm()
        return render(request, 'app/profile.html', locals())

    def post(self, request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']
            state=form.cleaned_data['state']

            reg=Customer(user=user, name=name, locality=locality, mobile=mobile, city=city, state=state)
            reg.save()
            messages.success(request,"Profile Saved Successfully!")

        else:
            messages.warning(request, "Invalid Input!")
        return render(request, 'app/profile.html', locals())

class AddressView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'app/address.html'
    context_object_name = 'addr'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

# class updateAddress(View):
#     def get(self, request, pk):
#         addr=Customer.objects.get(pk=pk)
#         form=CustomerProfileForm( instance=addr  )
#         return render(request, 'app/updateAddress.html', locals())
#     def post(self, request, pk):
#         form=CustomerProfileForm(request.POST)
#         if form.is_valid():
#             addr=Customer.objects.get(pk=pk)
#             addr.name=form.cleaned_data['name']
#             addr.locality=form.cleaned_data['locality']
#             addr.mobile=form.cleaned_data['mobile']
#             addr.city=form.cleaned_data['city']
#             addr.state=form.cleaned_data['state']
#             addr.save()
#             messages.success(request, "Profile Updated successfully!")
#         else:
#             messages.warning(request, "invalid Input")
#         return redirect("address")

class updateAddress(UpdateView):
    model=Customer
    form_class=CustomerProfileForm
    template_name='app/updateAddress.html'
    success_url=reverse_lazy('address')

class ContactView(CreateView):
    template_name='app/contact.html'
    model=Contact
    form_class=ContactForm
    success_url=reverse_lazy('home')
    def post(self, request, *args, **kwargs):

        form = self.get_form()
        form.save()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)