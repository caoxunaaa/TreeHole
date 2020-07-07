from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['test'] = 'Hello World'
        print(self.request)
        return context
