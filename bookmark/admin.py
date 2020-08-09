from django.contrib import admin

from .models import Bookmark # models.py 파일에서 Bookmark 라는 모델을 불러오겠다!!

admin.site.register(Bookmark)