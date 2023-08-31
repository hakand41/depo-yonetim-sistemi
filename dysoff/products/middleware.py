"""from django.http import HttpResponseForbidden
from ..dysoff import settings
class IPAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip = request.META['REMOTE_ADDR']
        allowed_ips = getattr(settings, 'ALLOWED_IPS', [])

        if client_ip not in allowed_ips:
            return HttpResponseForbidden("Forbidden: IP address not allowed.")

        response = self.get_response(request)
        return response###"""