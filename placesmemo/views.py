"""Views for placesmemo app"""
from django.shortcuts import render


def home(request):
    """Home view"""
    template_name = "home.html"
    return render(request, template_name)


# TODO create navitation for
# 1. home
# 2. places browse
# 3. memos list
# 4. lists
# 5. account/login/register
# TODO make search capable
# TODO make filter capable
