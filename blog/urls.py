from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("list/", views.BlogListView.as_view(), name="blog_list"),
    path("<int:pk>", views.BlogDetailView.as_view(), name="blog_detail"),
    path("update/<int:pk>/", views.BlogUpdateView.as_view(), name="blog_update"),
    path("delete/<int:pk>/", views.BlogDeleteView.as_view(), name="blog_delete"),
    path("send-email/", views.SendEmailView.as_view(), name="send_email"),
]