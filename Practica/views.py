from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView

from .models import *
# Create your views here.


def index(request):
    latest_threads_list = Thread.objects.order_by('ThreadName')[:5]
    context = {'latest_threads_list': latest_threads_list}
    return render(request, 'hey/index.html', context)


class ThreadDetail(DetailView):
    model = Thread
    template_name = 'hey/thread_detail.html'

    def get_context_data(self, **kwargs):
        latest_threads_list = Thread.objects.order_by('ThreadName')[:5]
        context = super(ThreadDetail, self).get_context_data(**kwargs)
        context['latest_threads_list'] = latest_threads_list
        return context


