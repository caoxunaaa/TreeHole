from django.views.generic import View, TemplateView
from .models import Dynamic


class DynamicTemplate(TemplateView):
    template_name = 'dynamic/dynamics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['dynamic_list'] = Dynamic.objects.filter(is_public=True, is_delete=False)
        return context
