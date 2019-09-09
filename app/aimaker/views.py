from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django_filters.views import FilterView
from django.shortcuts import render
from django.views.generic import TemplateView
from app.aimaker.forms import AiMakerForm
from app.aimaker.models import Photo
from app.aimaker.utils import AiMakerRequest, AiMakerResponse

import logging


class AiMakerView(LoginRequiredMixin, TemplateView):
    """
    AIメーカーへのリクエストを行う画面

    """

    def __init__(self):
        self.params = {'state': "",
                       'label': "",
                       'score': "",
                       'base64': "",
                       'form': AiMakerForm()}

    # GETリクエスト（index.htmlを初期表示）
    def get(self, req):
        return render(req, 'aimaker/index.html', self.params)

    # POSTリクエスト（index.htmlに結果を表示）
    def post(self, req):
        # POSTされたフォームデータを取得
        form = AiMakerForm(req.POST, req.FILES)
        # フォームデータのエラーチェック
        if not form.is_valid():
            raise ValueError('invalid form')
        # フォームデータから画像ファイルを取得
        photo = Photo(image=form.cleaned_data['image'])

        # 画像ファイルをbase64で受け取る
        base64 = photo.image_src()

        # AIメーカー
        response = AiMakerRequest(base64)
        result = AiMakerResponse(response)

        # 結果を格納
        self.params['state'] = result['state']
        self.params['label'] = result['label']
        self.params['score'] = '{:.2%}'.format(result['score'])
        self.params['base64'] = base64

        # ページの描画指示
        return render(req, 'aimaker/result.html', self.params)
