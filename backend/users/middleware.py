from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings

def custom_login_redirect_middleware(get_response):
    def middleware(request):
        next_url = request.GET.get("next")
        if next_url and not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
            next_url = settings.LOGIN_REDIRECT_URL
        response = get_response(request)
        return response

    return middleware
