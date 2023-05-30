from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicaciones.Academico.urls')),
    path('accounts/',include ('django.contrib.auth.urls') ),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

]
