from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     image = models.ImageField(upload_to='img', default=None, blank=True, null=True, verbose_name='Фото')
#     otchestvo = models.CharField( max_length=15, blank=True, verbose_name='Отчество')
#     telefone = models.CharField( max_length=15, blank=True, verbose_name='Телефон')
#     nomer_kvartir = models.CharField( max_length=4, blank=True, verbose_name='Номер квартиры')
#     birthday = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='День рождения')

#     class Meta:
#         db_table = 'user'
#         verbose_name='Список жильцов'
#         verbose_name_plural='Жильцы'

#     def __str__(self):
#         return self.first_name +' '+ self.otchestvo +' '+ self.last_name