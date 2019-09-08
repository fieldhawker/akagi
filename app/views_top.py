from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponseRedirect
# from django.urls import reverse_lazy
# from django.utils import timezone
# from django.views.generic import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django_filters.views import FilterView
from django.views.generic.base import TemplateView

# from .filters import ItemFilterSet
# from .forms import ItemForm
# from .models import Item


# 未ログインのユーザーにアクセスを許可する場合は、LoginRequiredMixinを継承から外してください。
#
# LoginRequiredMixin：未ログインのユーザーをログイン画面に誘導するMixin
# 参考：https://docs.djangoproject.com/ja/2.1/topics/auth/default/#the-loginrequired-mixin

class TopIndexView(LoginRequiredMixin, TemplateView):
    """
    ビュー：トップページ表示画面

    以下のパッケージを使用
    ・django-filter 一覧画面(ListView)に検索機能を追加
    https://django-filter.readthedocs.io/en/master/
    """
    template_name = 'app/top_index.html'

