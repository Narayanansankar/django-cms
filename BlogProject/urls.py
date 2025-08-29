# blog_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog.views import SignUpView

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # Include all URLs from our 'blog' application for the main site functionality
    path('', include('blog.urls')),

    # --- User Authentication URLs ---

    # URL for user registration (Sign Up)
    path('signup/', SignUpView.as_view(), name='signup'),

    # URL for user login. We specify our custom template.
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # URL for user logout.
    # This view correctly handles POST requests by default.
    # After logout, it will redirect to the URL specified in LOGOUT_REDIRECT_URL in settings.py.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]