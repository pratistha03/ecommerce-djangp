from django.conf.urls.static import static 
from django.conf import settings
from django.urls import path
from .views import AddressView, CategoryView,ContactView, CategoryTitle, ProductDetail, ProfileView, updateAddress, CustomerRegistrationView

from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm
from django.views.generic import TemplateView

# app_name='ecommerce_app'

urlpatterns = [
    path('', TemplateView.as_view(template_name='app/index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='app/about.html'), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),

    path('category/<slug:val>', CategoryView.as_view(), name="category"),
    path('category-title/<val>', CategoryTitle.as_view(), name="category-title"),
    path('product-detail/<int:pk>', ProductDetail.as_view(), name="product-detail"),
    
    path('profile/', ProfileView.as_view(), name="profile"),
    path('address/', AddressView.as_view(), name="address"),
    path('<int:pk>/updateAddress/', updateAddress.as_view(), name='updateAddress' ),


    # authentication
    path('registration/', CustomerRegistrationView.as_view(), name="customerregistration"),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name="login"),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name="password_reset"),
    path('changepassword/', auth_view.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone') , name="changepassword"),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name="passwordchange"),
    



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
