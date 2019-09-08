from django.urls import path
from django.conf.urls import url, include

from .models import Item
from django.views.generic import TemplateView

from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView, FaceView
from .views_top import TopIndexView

# アプリケーションのルーティング設定

urlpatterns = [
    path('', TopIndexView.as_view(), name='top'),

    # ml5.js
    path('ml5/styletransfervideo',TemplateView.as_view(template_name='app/ml5/style_transfer_video.html'), name='style_transfer_video'),

    # 顔判定
    path('face/', FaceView.as_view(), name='face'),

    # CRUD
    path('data/detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('data/create/', ItemCreateView.as_view(), name='create'),
    path('data/update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    path('data/delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
    path('data/', ItemFilterView.as_view(), name='index'),
]
