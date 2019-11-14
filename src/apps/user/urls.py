from django.conf.urls import url
from django.contrib.auth import views as auth_views
from apps.user import views as user_views

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(), {'template_name': 'user/login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', user_views.signup, name='signup'),
]
