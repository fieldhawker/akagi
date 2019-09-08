akagi
====

SEP勉強会用のDDjangoアプリケーション

[Qiita: [Python] テンプレートアプリを使った業務用Webアプリケーション高速開発法の紹介【チュートリアル形式】](https://qiita.com/okoppe8/items/4cc0f87ea933749f5a49)

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


