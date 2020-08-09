from django.db import models
from django.urls import reverse

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self): # 항상 문자열을 반환해야한다. 안에서 어떤연산을 수행해도 상관없지만 반환하는 값은 항상 문자열이 되도록!!
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])