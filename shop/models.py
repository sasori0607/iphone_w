from django.db import models
from django.urls import reverse
from django.contrib import admin
import datetime

class Category(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120, verbose_name='Название категории')

    class Meta:
        verbose_name = '1Категории'
        verbose_name_plural = '1Категории'

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        reverse('shop_category', kwargs={'slug': self.category.slug})

class Color(models.Model):
    img = models.ImageField(default='default.png',
                            upload_to='colors', verbose_name='Превью изображение')
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120, verbose_name='Название цвета')


    def __str__(self):
        return self.title

class Basket(models.Model):
    session_key = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    color = models.CharField(max_length=128)

    TwoSimTrue = models.CharField(max_length=128, default=1)
    IpadVersion = models.CharField(max_length=128, null=True, blank=True)
    MemoryVolume = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    RAM = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    processor = models.CharField(max_length=120, null=True, blank=True)

    size_corps = models.CharField(max_length=120, null=True, blank=True)

    version = models.CharField(max_length=120, null=True, blank=True)

    belt = models.CharField(max_length=120, null=True, blank=True,
                             verbose_name='Ремень')

    connector = models.CharField(max_length=120, null=True, blank=True,
                            verbose_name='Разъем')

    charging = models.CharField(max_length=120, null=True, blank=True,
                                 verbose_name='Зарядка')

    coverings = models.CharField(max_length=120, null=True, blank=True,
                                verbose_name='Покрытия')

    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name="Цена")
    quantity = models.IntegerField(default=1, verbose_name="Количество")
    img_url = models.CharField(max_length=120, verbose_name='Ссылка на img')
    article_date = models.DateTimeField(default=datetime.datetime.now())




# class Gallery(models.Model):
#     image = models.ImageField(upload_to='gallery')
#     product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')



class IPhone_Ipad_Main(models.Model):

   slug = models.SlugField(unique=True)

   category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)
   title = models.CharField(max_length=120, verbose_name='Имя товара')
   TwoSimTrue = models.BooleanField(verbose_name='Наличие 2ух Симок', default=False)
   IpadVersion = models.BooleanField(verbose_name='Есть ли 2 версии', default=False)

   img = models.ImageField(default='default.png', upload_to='goods_img', verbose_name='Превью изображение')

   description = models.TextField(verbose_name='Описание', default=' ')

   img_description = models.ImageField(default='default.png', upload_to='goods_img', verbose_name='В комплекте')

   MemoryVolume1 = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True,
                                       verbose_name='Объем памяти 1')

   MemoryVolume2 = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True,
                                       verbose_name='Объем памяти 2(При наличие)')

   MemoryVolume3 = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True,
                                       verbose_name='Объем памяти 3(При наличие)')

   MemoryVolume4 = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True,
                                       verbose_name='Объем памяти 4(При наличие)')

   RAM1 = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True,
                                       verbose_name='Объем Оперативной памяти 1')

   RAM2 = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True,
                              verbose_name='Объем Оперативной памяти 2')

   RAM3 = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True,
                              verbose_name='Объем Оперативной памяти 3')

   processor1 = models.CharField(max_length=120, null=True, blank=True,
                                 verbose_name='Процессор 1')

   processor2 = models.CharField(max_length=120, null=True, blank=True,
                                 verbose_name='Процессор 2')

   сolor1 = models.ForeignKey('Color',  related_name='color1', verbose_name='Цвет1',
                              null=True, blank=True, on_delete=models.CASCADE)
   сolor2 = models.ForeignKey('Color',  related_name='color2', verbose_name='Цвет2',
                              null=True, blank=True, on_delete=models.CASCADE)
   сolor3 = models.ForeignKey('Color',  related_name='color3', verbose_name='Цвет3',
                              null=True, blank=True, on_delete=models.CASCADE)
   сolor4 = models.ForeignKey('Color',  related_name='color4', verbose_name='Цвет4',
                              null=True, blank=True, on_delete=models.CASCADE)
   сolor5 = models.ForeignKey('Color',  related_name='color5', verbose_name='Цвет5',
                              null=True, blank=True, on_delete=models.CASCADE)
   сolor6 = models.ForeignKey('Color',  related_name='color6', verbose_name='Цвет6',
                              null=True, blank=True, on_delete=models.CASCADE)




   class Meta:
       verbose_name = 'iPhone+iPad+Mac'
       verbose_name_plural = 'iPhones+iPads+Macs'

   def __str__(self):
       return self.slug

   def get_absolute_url(self):
       return reverse('shop_detail', kwargs={'slug': self.slug, 'category': self.category})


grade_list = (
    [1, '1 Sim'],
    [2, 's Sim']
)

version_list = (
    ['Wi-Fi', 'Wi-Fi'],
    ['Wi-Fi + 4G', 'Wi-Fi + 4G']
)



class IPhonePart(models.Model):

    color = models.ForeignKey('Color', verbose_name='Цвет', on_delete=models.CASCADE)

    anchor = models.ForeignKey('IPhone_Ipad_Main', verbose_name='Модель привязки', on_delete=models.CASCADE)

    vendorСode = models.CharField(max_length=120, verbose_name='Артикул')

    sim = models.IntegerField(choices=grade_list, default=1)

    MemoryVolume = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True,
                                        verbose_name='Объем памяти')

    imgMain = models.ImageField(default='default.png', upload_to='goods_img', verbose_name='Фото айфона')

    version = models.CharField(max_length=120, choices=version_list, null=True, blank=True, verbose_name='Версия Айпада')

    ram = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True,
                                       verbose_name='Объем оперативной памяти')

    processor1 = models.CharField(max_length=120, null=True, blank=True,
                                  verbose_name='Процессор')

    price = models.DecimalField(max_digits=5, default=0, decimal_places=0, verbose_name='Доп ценна за цвет')

    class Meta:
       verbose_name = 'iPhone+iPad+Mac Товары'
       verbose_name_plural = 'iPhones+iPads+Macs Товары'

    def __str__(self):
        return self.anchor.title


class Watch(models.Model):

   slug = models.SlugField(unique=True)

   category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)

   title = models.CharField(max_length=120, verbose_name='Имя товара')

   img = models.ImageField(default='default.png', upload_to='goods_img', verbose_name='Превью изображение')

   description = models.TextField(verbose_name='Описание', default=' ')

   img_description = models.ImageField(default='default.png', upload_to='goods_img', verbose_name='В комплекте')


   size_corps1 = models.CharField(max_length=120, null=True, blank=True,
                                 verbose_name='Размер корпуса 1')

   size_corps2 = models.CharField(max_length=120, null=True, blank=True,
                                 verbose_name='Размер корпуса 2')

   version1 = models.CharField(max_length=120, null=True, blank=True,
                                 verbose_name='Версия 1')

   version2 = models.CharField(max_length=120, null=True, blank=True,
                                 verbose_name='Версия 2')

   belt1 = models.CharField(max_length=120, null=True, blank=True,
                                 verbose_name='Ремень 1')

   belt2 = models.CharField(max_length=120, null=True, blank=True,
                                 verbose_name='Ремень 2')

   сolor1 = models.ForeignKey('Color',  related_name='color11', verbose_name='Цвет1',
                              null=True, blank=True, on_delete=models.CASCADE)
   сolor2 = models.ForeignKey('Color',  related_name='color21', verbose_name='Цвет2',
                              null=True, blank=True, on_delete=models.CASCADE)
   сolor3 = models.ForeignKey('Color',  related_name='color31', verbose_name='Цвет3',
                              null=True, blank=True, on_delete=models.CASCADE)
   сolor4 = models.ForeignKey('Color',  related_name='color41', verbose_name='Цвет4',
                              null=True, blank=True, on_delete=models.CASCADE)
   сolor5 = models.ForeignKey('Color',  related_name='color51', verbose_name='Цвет5',
                              null=True, blank=True, on_delete=models.CASCADE)
   сolor6 = models.ForeignKey('Color',  related_name='color61', verbose_name='Цвет6',
                              null=True, blank=True, on_delete=models.CASCADE)

   class Meta:
       verbose_name = 'Watch'
       verbose_name_plural = 'Watch'

   def __str__(self):
       return self.title

   def get_absolute_url(self):
       return reverse('shop_detail', kwargs={'slug': self.slug, 'category': self.category})



class WatchPart(models.Model):

    color = models.ForeignKey('Color', verbose_name='Цвет', on_delete=models.CASCADE)

    anchor = models.ForeignKey('Watch', verbose_name='Модель привязки', on_delete=models.CASCADE)

    vendorСode = models.CharField(max_length=120, verbose_name='Артикул')

    size = models.CharField(max_length=120, null=True, blank=True,
                                   verbose_name='Размер корпуса')
    version = models.CharField(max_length=120, null=True, blank=True,
                                verbose_name='Версия')
    belt = models.CharField(max_length=120, null=True, blank=True,
                               verbose_name='Тип ремешка')

    price = models.DecimalField(max_digits=5, default=0, decimal_places=0, verbose_name='Доп ценна за цвет')

    imgMain = models.ImageField(default='default.png', upload_to='goods_img', verbose_name='Фото айфона')

    class Meta:
       verbose_name = 'Watch Товары'
       verbose_name_plural = 'Watch Товары'


class airPods(models.Model):

    slug = models.SlugField(unique=True)

    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)

    title = models.CharField(max_length=120, verbose_name='Имя товара')

    img = models.ImageField(default='default.png', upload_to='goods_img', verbose_name='Превью изображение')

    description = models.TextField(verbose_name='Описание', default=' ')

    img_description = models.ImageField(default='default.png', upload_to='goods_img', verbose_name='В комплекте')

    connector1 = models.CharField(max_length=120, null=True, blank=True,
                                  verbose_name='Разъем 1')

    connector2 = models.CharField(max_length=120, null=True, blank=True,
                                  verbose_name='Разъем 2')

    charging1 = models.CharField(max_length=120, null=True, blank=True,
                                  verbose_name='Зарядка 1')

    charging2 = models.CharField(max_length=120, null=True, blank=True,
                                  verbose_name='Зарядка 2')

    coverings1 = models.CharField(max_length=120, null=True, blank=True,
                                 verbose_name='Покрытия 1')

    coverings2 = models.CharField(max_length=120, null=True, blank=True,
                                 verbose_name='Покрытия 2')

    сolor1 = models.ForeignKey('Color', related_name='color12', verbose_name='Цвет1',
                               null=True, blank=True, on_delete=models.CASCADE)
    сolor2 = models.ForeignKey('Color', related_name='color22', verbose_name='Цвет2',
                               null=True, blank=True, on_delete=models.CASCADE)
    сolor3 = models.ForeignKey('Color', related_name='color32', verbose_name='Цвет3',
                               null=True, blank=True, on_delete=models.CASCADE)
    сolor4 = models.ForeignKey('Color', related_name='color42', verbose_name='Цвет4',
                               null=True, blank=True, on_delete=models.CASCADE)
    сolor5 = models.ForeignKey('Color', related_name='color52', verbose_name='Цвет5',
                               null=True, blank=True, on_delete=models.CASCADE)
    сolor6 = models.ForeignKey('Color', related_name='color62', verbose_name='Цвет6',
                               null=True, blank=True, on_delete=models.CASCADE)
    class Meta:
       verbose_name = 'airPods'
       verbose_name_plural = 'airPods'

    def __str__(self):
       return self.title

    def get_absolute_url(self):
       return reverse('shop_detail', kwargs={'slug': self.slug, 'category': self.category})



class airPodsPart(models.Model):

    color = models.ForeignKey('Color', verbose_name='Цвет', on_delete=models.CASCADE)

    anchor = models.ForeignKey('airPods', verbose_name='Модель привязки', on_delete=models.CASCADE)

    vendorСode = models.CharField(max_length=120, null=True, blank=True,
                                  verbose_name='Артикул')

    connector = models.CharField(max_length=120, null=True, blank=True,
                                 default='-',
                                 verbose_name='Разъем')

    charging = models.CharField(max_length=120, null=True, blank=True,
                                default='-',
                                verbose_name='Зарядка')

    coverings = models.CharField(max_length=120, null=True, blank=True,
                                 default='-',
                                 verbose_name='Покрытия')


    price = models.DecimalField(max_digits=5, default=0, decimal_places=0, verbose_name='Доп ценна за цвет')

    imgMain = models.ImageField(default='default.png', upload_to='goods_img', verbose_name='Фото айфона')

    class Meta:
       verbose_name = 'airPods Товары'
       verbose_name_plural = 'airPods Товары'


class Accessories(models.Model):

    slug = models.SlugField(unique=True)

    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)

    title = models.CharField(max_length=120, verbose_name='Имя товара')

    img = models.ImageField(default='default.png', upload_to='goods_img', verbose_name='Превью изображение')

    description = models.TextField(verbose_name='Описание', default=' ')

    MemoryVolume1 = models.CharField(max_length=120, null=True, blank=True,
                                        verbose_name='Объем памяти 1(При наличие)')

    MemoryVolume2 = models.CharField(max_length=120, null=True, blank=True,
                                     verbose_name='Объем памяти 2(При наличие)')

    modelCase1 = models.CharField(max_length=120, null=True, blank=True,
                                  verbose_name='Модель привязки чехла 1')

    modelCase2 = models.CharField(max_length=120, null=True, blank=True,
                                  verbose_name='Модель привязки чехла 2')

    modelCase3 = models.CharField(max_length=120, null=True, blank=True,
                                  verbose_name='Модель привязки чехла 3')


    сolor1 = models.ForeignKey('Color', related_name='color13', verbose_name='Цвет1',
                               null=True, blank=True, on_delete=models.CASCADE)
    сolor2 = models.ForeignKey('Color', related_name='color23', verbose_name='Цвет2',
                               null=True, blank=True, on_delete=models.CASCADE)
    сolor3 = models.ForeignKey('Color', related_name='color33', verbose_name='Цвет3',
                               null=True, blank=True, on_delete=models.CASCADE)
    сolor4 = models.ForeignKey('Color', related_name='color43', verbose_name='Цвет4',
                               null=True, blank=True, on_delete=models.CASCADE)
    сolor5 = models.ForeignKey('Color', related_name='color53', verbose_name='Цвет5',
                               null=True, blank=True, on_delete=models.CASCADE)
    сolor6 = models.ForeignKey('Color', related_name='color63', verbose_name='Цвет6',
                               null=True, blank=True, on_delete=models.CASCADE)
    class Meta:
       verbose_name = 'Accessories'
       verbose_name_plural = 'Accessories'


class AccessoriesPart(models.Model):

    color = models.ForeignKey('Color', verbose_name='Цвет', on_delete=models.CASCADE)

    anchor = models.ForeignKey('Accessories', verbose_name='Модель привязки', on_delete=models.CASCADE)

    vendorСode = models.CharField(max_length=120, verbose_name='Артикул')

    MemoryVolume = models.CharField(max_length=120, null=True, blank=True,
                                     verbose_name='Объем памяти(При наличие)')

    modelCase = models.CharField(max_length=120, null=True, blank=True,
                                  verbose_name='Модель привязки чехла')


    price = models.DecimalField(max_digits=5, default=0, decimal_places=0, verbose_name='Доп ценна за цвет')

    imgMain = models.ImageField(default='default.png', upload_to='goods_img', verbose_name='Фото айфона')

    class Meta:
       verbose_name = 'Accessories Товары'
       verbose_name_plural = 'Accessories Товары'




class Order(models.Model):
    name = models.CharField(max_length=120, verbose_name='Имя')
    address = models.CharField(max_length=120, verbose_name='Адрес')
    phone = models.CharField(max_length=120, verbose_name='Телефон')
    description = models.TextField(verbose_name='Коментарий к заказу', default=' ')
    info = models.TextField(verbose_name='Заказ', default=' ')

    class Meta:
       verbose_name = 'Заказ'
       verbose_name_plural = 'Заказы'

    def __str__(self):
       return (self.name + ' ' + self.phone)

