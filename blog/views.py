from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from blog.models import Blog
from dotenv import load_dotenv
import os
load_dotenv(override=True)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class BlogCreateView(CreateView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content']
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy("blog:blog_list")


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        if self.object.view_count == 100:
            subject = f"{self.object.title} - Набралось 100 просмотров"
            message = f"Статья {self.object.title} весьма актуальна"
            from_email = os.getenv("EMAIL_USERNAME")
            recipient_list = [os.getenv("EMAIL_USERNAME")]
            send_mail(subject, message, from_email, recipient_list)
        self.object.save()
        return self.object


class SendEmailView(View):
    def get(self, request):
        subject = "Hello from Django"
        message = "This is an email sent from Django."
        from_email = os.getenv("EMAIL_USERNAME")
        recipient_list = [os.getenv("EMAIL_USERNAME")]

        try:
            send_mail(subject, message, from_email, recipient_list)
            return HttpResponse("Email sent successfully!")
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")
