from django.contrib import admin
from django.urls import path, include
from leaves import views as leave_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('login/', leave_views.login_view, name='login'),
    path('register/', leave_views.register_view, name='register'),
    path('logout/', leave_views.logout_view, name='logout'),

    # 👇 THIS LINE IS THE MOST IMPORTANT
    path("", include("leaves.urls")),
]
