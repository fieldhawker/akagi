from django import forms

from .models import Item


class ItemForm(forms.ModelForm):
    """
    モデルフォーム構成クラス
    ・公式 モデルからフォームを作成する
    https://docs.djangoproject.com/ja/2.1/topics/forms/modelforms/
    """

    class Meta:
        model = Item
        fields = '__all__'

        # 以下のフィールド以外が入力フォームに表示される
        # AutoField
        # auto_now=True
        # auto_now_add=Ture
        # editable=False

class ImageForm(forms.Form):
    image = forms.ImageField(label="判定する画像を選択してください",
                             error_messages={'missing' : '画像ファイルが選択されていません。',
                                             'invalid' : '分類する画像ファイルを選択してください。',
                                             'invalid_image' : '画像ファイルではないようです。'})