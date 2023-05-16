from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from .models import Tag


# Create your views here.
class TagListView(LoginRequiredMixin, ListView):
    """Show a list of memos with a specific tag"""

    # TODO create taglistview
    # TODO tag_list.html

    # TODO are there any other views needed for Tags?


@csrf_exempt
def get_tags():
    """This view returns a list of tags."""
    tags = Tag.objects.all()
    tag_list = [tag.to_dict() for tag in tags]
    return JsonResponse({"tags": tag_list}, status=200)


@csrf_exempt
def clear_empty_tags():
    """This view clears tags with no memo."""
    tags = Tag.objects.all()
    for tag in tags:
        if tag.memo_set.count() == 0:
            tag.delete()
