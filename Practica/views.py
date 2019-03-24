from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView

from .models import *
# Create your views here.


def index(request):
    latest_threads_list = Thread.objects.order_by('ThreadName')
    context = {'latest_threads_list': latest_threads_list}
    return render(request, 'hey/index.html', context)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ThreadDetail(DetailView):
    model = Thread
    template_name = 'hey/thread_detail.html'

    def get_context_data(self, **kwargs):
        latest_threads_list = Thread.objects.order_by('ThreadName')
        latest_image_list = Thread.objects.order_by('TagId')
        context = super(ThreadDetail, self).get_context_data(**kwargs)
        context['latest_threads_list'] = latest_threads_list
        context['latest_image_list'] = latest_image_list
        return context


class ImageDetail(DetailView):
    model = TaggedImage
    template_name = 'hey/image_detail.html'

    def get_context_data(self, **kwargs):
        latest_threads_list = Thread.objects.order_by('ThreadName')
        context = super(ImageDetail, self).get_context_data(**kwargs)
        context['latest_threads_list'] = latest_threads_list
        return context


