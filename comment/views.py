from django.views.generic import CreateView
from .forms import CommentCreateForm
from .models import Comment
from django.http import JsonResponse


class CommentCreateView(CreateView):
    form_class = CommentCreateForm
    model = Comment

    def form_valid(self, form):
        print(self.request.POST)
        user = self.request.user
        content_type = form.cleaned_data['content_object']
        object_id = form.cleaned_data['object_id']
        # content = form.cleaned_data['c']
        # comment = Comment.objects.create(user=user, )
        data = dict()
        data['status'] = 'SUCCESS'
        data['object_id'] = object_id
        return JsonResponse(data)
