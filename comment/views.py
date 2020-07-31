from django.views.generic import CreateView
from .forms import CommentCreateForm
from .models import Comment
from django.http import JsonResponse


class CommentCreateView(CreateView):
    form_class = CommentCreateForm
    model = Comment

    def form_valid(self, form):
        object_id = form.cleaned_data['object_id']
        comment = Comment()
        comment.user = self.request.user
        comment.content_object = form.cleaned_data['content_object']
        comment.text = self.request.POST.get('content', '')
        comment.save()

        data = dict()
        data['username'] = comment.user.username
        data['text'] = comment.text
        data['status'] = 'SUCCESS'
        return JsonResponse(data)
