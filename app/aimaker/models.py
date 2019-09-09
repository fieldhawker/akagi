from django.db import models
import io
import base64

class Photo(models.Model):
    # 保存先ディレクトリの指定
    image = models.ImageField(upload_to='images')

    def image_src(self):
        with self.image.open() as img:
            base64_img = base64.b64encode(img.read()).decode()

            return 'data:' + img.file.content_type + ';base64,' + base64_img
