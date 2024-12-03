from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
# from .views import CustomLoginView  # You can remove this import

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path('accounts/', include('allauth.urls')),
    path("api-auth/", include("rest_framework.urls")),
    path("api/dj-rest-auth/", include("dj_rest_auth.urls")),
    path("api/dj-rest-auth/registration/account-confirm-email/<str:key>/", ConfirmEmailView.as_view()),
    path("api/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/dj-rest-auth/account-confirmation-email/", VerifyEmailView.as_view(), name="account_email_verification_sent"),
    # Use the default dj_rest_auth login view
    path('api/dj-rest-auth/login/', include("dj_rest_auth.urls")),
    path('api/chat/', include('chatbot.urls')),

]

# Add this at the end of the file
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)