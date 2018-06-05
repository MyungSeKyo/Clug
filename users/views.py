from django.contrib.auth import views, logout
from django.views.generic import RedirectView
from django.http import HttpResponseRedirect


class LoginView(views.LoginView):
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['next'] = self.request.META.get('HTTP_REFERER', '/')
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/'))
        else:
            return super(LoginView, self).get(request, *args, **kwargs)


class LogoutView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return self.request.META.get('HTTP_REFERER', '/')

