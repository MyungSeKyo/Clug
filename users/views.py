from django.contrib.auth import views, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import RedirectView, CreateView
from django.contrib import messages


class LoginView(views.LoginView):
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)

        # 로그인 성공후 이전 페이지로 리다이렉션 시킴
        context['next'] = self.request.META.get('HTTP_REFERER', '/')

        return context

    def form_valid(self, form):
        messages.info(self.request, "로그인되었습니다.")
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, "로그아웃되었습니다.")
        return super(LogoutView, self).get(request, *args, **kwargs)


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/signup.html'

class PasswordChangeView(views.PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = '/'

    def form_valid(self, form):
        messages.info(self.request, "비밀번호가 변경되었습니다.")
        return super(PasswordChangeView, self).form_valid(form)
