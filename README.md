akagi
====

SEP勉強会用のDjangoアプリケーション

参考：
[Python] プログラム初心者のためのWebアプリ簡単作成法
https://qiita.com/okoppe8/items/4cc0f87ea933749f5a49

リポジトリ：
https://github.com/fieldhawker/akagi

[Qiita: [Python] テンプレートアプリを使った業務用Webアプリケーション高速開発法の紹介【チュートリアル形式】](https://qiita.com/okoppe8/items/4cc0f87ea933749f5a49)

環境構築
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser 

起動
python manage.py runserver

## Requirement

```
Django==2.1.1
django-crispy-forms==1.7.2
django-filter==2.0.0
pytz==2018.5
```

## Usage

Steps

1. Git clone this project
2. Edit modelfile `app/models.py`
3. Run `makemigrations` and `migrate`
4. Edit HTML files `templates/item_filter.html` and `item_detail_contents.html`

If you use it production environment, you must replace `settings.SECRET_KEY`.

## Contribution



## Licence



## Author


## Command

image-collector　画像収集
https://github.com/skmatz/image-collector

python image_collector.py -t 佐倉綾音 -n 10 -d sakura_images
python image_collector.py -t Gackt -n 200 -d google_images
python image_collector.py -t オードリー春日 -n 200 -d google_images

img_face_dt 画像から顔を切り出し
https://qiita.com/kerobot/items/e3abe3f21808b4b584bd

python img_face_dt.py
 実行時は以下のパスを任意に書き換えて実行
 IMAGE_PATH_PATTERN = "./sakura_images/佐倉綾音/*"
 IMAGE_PATH_PATTERN = "./google_images/Gackt/*"
 IMAGE_PATH_PATTERN = "./google_images/オードリー春日/*"
 OUTPUT_IMAGE_DIR = "./face_image"
 OUTPUT_IMAGE_DIR = "./face_image/gackt"
 OUTPUT_IMAGE_DIR = "./face_image/オードリー春日"

img_data_gen 画像を水増し
https://qiita.com/kerobot/items/54bc1224424280150d1c

python img_data_gen.py
 実行時は以下のパスを任意に書き換えて実行
 IMAGE_PATH_PATTERN = "./face_image/*"
 IMAGE_PATH_PATTERN = "./face_image/gackt/*"
 IMAGE_PATH_PATTERN = "./face_image/オードリー春日/*"
 OUTPUT_IMAGE_DIR = "./face_scratch_image"
 OUTPUT_IMAGE_DIR = "./face_scratch_image/gackt"
 OUTPUT_IMAGE_DIR = "./face_scratch_image/オードリー春日"

img_model_gen 顔分類モデルの生成
https://qiita.com/kerobot/items/be4fd1a166073fbcff38

実行にはgraphvizが必要なのでローカル環境にインストールすること
https://analytics-note.xyz/mac/mac-graphviz-install/
 brew install graphviz

python img_model_gen.py
 実行時は以下のパスを任意に書き換えて実行
 TEST_IMAGE_DIR = "./test_image"
 TRAIN_IMAGE_DIR = "./face_scratch_image"
 OUTPUT_MODEL_DIR = "./model"

img_decide 顔判定モデルで画像判定処理
https://qiita.com/kerobot/items/1ce75622d173d231d423

python img_decide.py 853620.jpeg
python img_decide.py tmp/000019_002.jpg
python img_decide.py tmp/010008_002.jpg


from .cv2 import *
ImportError: libSM.so.6: cannot open shared object file: No such file or directory

herokuではlibSM.so.6がないようなので, 入れる
https://qiita.com/haru1843/items/210cb08024195b9d1bc8
