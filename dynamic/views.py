from django.views.generic import ListView, TemplateView
from .models import Dynamic


def paginator_handle(request, context):
    paginator = context['paginator']
    page_num = request.GET.get('page', 1)
    page_of_dynamics = paginator.get_page(page_num)
    current_page_num = page_of_dynamics.number
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))

    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    context['page_range'] = page_range
    return context


class Dynamics(ListView):
    template_name = 'dynamic/dynamics.html'
    context_object_name = 'dynamic_list'
    paginate_by = 5
    allow_empty = True

    def get_queryset(self):
        return Dynamic.objects.filter(is_public=True, is_delete=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return paginator_handle(self.request, context)


class MyDynamics(ListView):
    template_name = 'dynamic/my_dynamics_list.html'
    context_object_name = 'my_dynamic_list'
    paginate_by = 5
    allow_empty = True

    def get_queryset(self):
        return Dynamic.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return paginator_handle(self.request, context)
