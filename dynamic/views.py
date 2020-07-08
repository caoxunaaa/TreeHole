from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import View
from .models import Dynamic
from django.shortcuts import reverse
from .form import DynamicCreateForm
from django.http import JsonResponse, HttpResponse
from django.core import serializers


# Create your views here.
class AjaxUpdate(View):
    def get(self, request, *args, **kwargs):
        data = dict()
        data['status'] = 'SUCCESS'
        # 3. 返回
        return JsonResponse(data)


class DynamicUpdate(UpdateView):
    model = Dynamic
    fields = ['text']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('dynamic_update_form', kwargs={'pk': 2})


class DynamicCreate(CreateView):
    model = Dynamic
    # fields = ['owner', 'text', 'type']
    template_name_suffix = '_create_form'
    form_class = DynamicCreateForm

    def get_success_url(self):
        return reverse('dynamic_update_form', kwargs={'pk': 1})
