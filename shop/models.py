from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='상품명')
    description = models.TextField(verbose_name='상품 설명')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='가격')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 일자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정 일자')

    def __str__(self):
        return self.name
