# from django.urls import path
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static


# urlpatterns = [
#     path('', views.home),
#     path('category/<slug:val>', views.CategoryView.as_view(),name='category'),
# ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
##########

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetFrom,PasswordChangeForm

urlpatterns = [
    path('', views.home),
    path('about/', views.about,name='about'),
    path('contect/', views.contect,name='contect'),
    path('category/<slug:val>', views.CategoryView.as_view(),name='category'),
    path('category-title/<val>',views.CategoryTitle.as_view(),name='category-title'),
    path('product-detail/', views.Productdetail.as_view(), name='produc-detail'),
#     path('profile/',views.ProfileView.as_view(),name='profile'),
#     path('address/',views.address ,name='address'),
#     path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),

#     #login authentication
#     path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
#     path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
#     path('password-reset',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetFrom), name='password_reset'),
#     path('passswordchange/', auth_view.PasswordChangeView.as_view(template_name='app/passswordchange.html', form_class=MyPasswordResetFrom, success_url='passswordchangedone'), name='passswordchange'),
#     path('passswordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passswordchangedone.html'), name='passswordchangedone'),
#     path(),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

