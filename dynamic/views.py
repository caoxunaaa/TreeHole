from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from .models import Dynamic, DynamicType
from django.shortcuts import redirect, reverse
from .forms import DynamicCreateForm
from django.contrib.auth.models import User


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


class DynamicsList(ListView):
    template_name = 'dynamic/dynamics_list.html'
    context_object_name = 'dynamic_list'
    paginate_by = 5
    allow_empty = True

    def get_queryset(self):
        return Dynamic.objects.filter(is_public=True, is_delete=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return paginator_handle(self.request, context)


class MyDynamicsList(ListView):
    template_name = 'dynamic/my_dynamics_list.html'
    context_object_name = 'dynamic_list'
    paginate_by = 5
    allow_empty = True

    def get_queryset(self):
        return Dynamic.objects.filter(owner=self.request.user, is_delete=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return paginator_handle(self.request, context)


class DynamicDetail(DetailView):
    template_name = 'dynamic/dynamic_detail.html'


class DynamicDelete(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pk = request.GET.get('delete', 0)
            dynamic = Dynamic.objects.get(pk=pk)
            if request.user == dynamic.owner:
                dynamic.is_delete = True
                dynamic.save()
                return redirect(request.GET.get('from', reverse('home')))
        else:
            return redirect(reverse('home'))


class DynamicCreate(CreateView):
    model = Dynamic
    template_name = 'dynamic/dynamic_create.html'
    fields = ['owner', 'text']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dynamic_types'] = DynamicType.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)


        # 判断有没有多重next
        if '?next=' not in self.request.POST.get('next', ''):
            return redirect(self.request.POST.get('next', reverse('home')))
        else:
            return redirect(reverse('home'))
