from django.urls import path
from .views import account_inactive_view
from allauth.account.utils import send_email_confirmation
from django.http import HttpResponse
from .views import verification_complete
from .views import CustomLoginView
from . import views
from .views import custom_logout  

urlpatterns = [
  path('account/inactive/', account_inactive_view, name='account_inactive'),
  path('verification-complete/', verification_complete, name='verification_complete'),
  path('home/', views.home, name='home'),
  path('api/dj-rest-auth/login/', CustomLoginView.as_view(), name='custom_login'),
  path('api/dj-rest-auth/logout/', custom_logout, name='custom_logout'),
]

def test_email(request):
    user = request.user
    send_email_confirmation(request, user)
    return HttpResponse("Email sent.")