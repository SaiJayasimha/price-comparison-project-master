# middleware.py

from django.contrib.auth import logout

class SessionTimeoutMiddleware:
    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):
        if request.user.is_authenticated and request.session.get_expiry_age() <= 60:
            # Check if the user is authenticated and the session is about to expire (less than 1 minute left)
            logout(request)  # Log out the user
        response = self.get_response(request)
        return response