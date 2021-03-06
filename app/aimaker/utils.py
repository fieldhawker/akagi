from logging import basicConfig, getLogger, DEBUG
from django.http import HttpResponse
import requests
import json
import io
import base64

basicConfig(level=DEBUG)
logger = getLogger(__name__)


def AiMakerRequest(base64):

    logger.debug('AiMakerRequest')
    # AIメーカーのWebAPIから取得したデータを返却する

    API_Key = 'c28f3694803e7631c5feb0831f29be77670a5d6f77ede6be444afd0b6d86280d2b67b3cc50730753e7e49c2342fd5b18'
    id = 3673
    url = 'https://aimaker.io/image/classification/api'

    query = {
        'id': id,
        'apikey': API_Key,
        'base64': base64
    }

    try:
        # APIリクエスト
        response = requests.post(url, query)
        response = response.json()
        # logger.debug(response)
        return response

    except:
        logger.debug('Except AiMakerRequest.')

    return []


def AiMakerResponse(json):
    logger.debug('AiMakerResponse')
    # AIメーカーから受け取ったJSONから必要な値を取得

    # 想定されるレスポンスは以下のようになっている
    # {
    #     "state": 1,
    #     "url": "https://aimaker.io/sample.png",
    #     "labels": {
    #         "0": {
    #             "score": 0.997,
    #             "label": "ラベル0"
    #         },
    #         "1": {
    #             "score": 0.003,
    #             "label": "ラベル1"
    #         }
    #     }
    # }

    result = {
        'state': 'NG',
        'label': "ラベル0",
        'score': 0
    }

    max_score = 0
    max_label = ''

    if not json['state'] == 1:
        logger.debug(result)
        return result

    for label in json['labels']:
        if max_score < label["score"]:
            max_score = label["score"]
            max_label = label["label"]

    result = {
        'state': 'OK',
        'label': max_label,
        'score': max_score
    }

    # logger.debug(result)
    return result
