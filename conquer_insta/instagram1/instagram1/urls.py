from django.contrib import admin
from django.urls import path
from .views import HomeView, LegalView, LoginView, ContactView, RegisterView, logout_view, ProfileDetailView, ProfileUpdateView, ProfileListView
from django.conf import settings
from posts.views import PostCreateView, PostDetailView, like_post, like_post_ajax
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("legal/", LegalView.as_view(), name="legal"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/list/", ProfileListView.as_view(), name="profile_list"),
    path("profile/<pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/update/<pk>/", ProfileUpdateView.as_view(), name="profile_update"),
    path("posts/create/", PostCreateView.as_view(), name="post_create"),
    path("posts/<pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/like/<pk>/", like_post, name="post_like"),
    path("posts/like-ajax/<pk>/", like_post_ajax, name="post_like_ajax"),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




