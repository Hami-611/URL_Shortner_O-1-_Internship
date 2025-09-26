from django.contrib import admin
from django.urls import path
from authentication import views as auth_views
from urlhandler import views as url_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', url_views.home),
    path('login/', auth_views.login, name="login"),
    path('signup/', auth_views.signup, name="signup"),
    path('logout/', auth_views.logout, name="logout"),
    path('dashboard/', url_views.dashboard, name="dashboard"),
    path('generate/', url_views.generate, name="generate"),
    path('deleteurl/', url_views.deleteurl, name="deleteurl"),
    path('<str:query>/', url_views.home, name="home"),  # For short URLs
]

