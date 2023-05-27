from django.db import models


class Post(models.Model):
    objects = None
    title = models.CharField('Заголовок новости', max_length=1000)
    promo_info = models.TextField('Текст превью новости (до 300 символов)', max_length=300, default=None, null=True)
    description = models.TextField('Текст новости', default=None, null=True)
    data = models.DateField('Дата публикации', null=True)
    img = models.ImageField('Изображение', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class PostSuggestion(models.Model):
    name_author = models.CharField(max_length=30)
    email = models.EmailField()
    title = models.CharField('Заголовок новости', max_length=200)
    promo_info = models.TextField('Текст превью новости (до 300 символов)', max_length=300, default=None, null=True)
    description = models.TextField('Текст новости', default=None, null=True)
    data = models.DateTimeField(auto_now=True, null=True)
    img = models.ImageField('Изображение', upload_to='post_suggestions')

    def __str__(self):
        return f'{self.name_author}, {self.title}, {self.promo_info}'

    class Meta:
        verbose_name = "Предложенная новость"
        verbose_name_plural = "Предложенные новости"


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    date = models.DateTimeField(auto_now=True)
    # Связываю комментарий с постом.
    # Каскадно удаляю комментарии вместе с постом
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Subscriber(models.Model):
    email = models.EmailField(default=None)

    # Запись из данной модели будет презентовать в админке 'Подписчик ИМЯ EMAIL'
    def __str__(self):
        return 'Подписчик %s' % self.email

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"
        ordering = ["email"]  # Сортировка по полю имени


class Service(models.Model):
    objects = None
    name = models.CharField("Название категории услуги", max_length=50)
    text_details = models.TextField("Описание категории", max_length=1000)
    img = models.ImageField('Изображение', upload_to='service/')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = "Категория услуг"
        verbose_name_plural = "Категории услуг"
        ordering = ["name"]  # Сортировка по полю имени


class ServiceCategory(models.Model):
    name_of_category = models.CharField('Название подкатегории услуги', max_length=30)
    text_under_category = models.TextField(max_length=1000, blank=True)
    service_cat = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Выбрать категорию услуг',
                                    null=True)

    def __str__(self):
        return '%s' % self.name_of_category

    class Meta:
        verbose_name = "Подкатегория услуг"
        verbose_name_plural = "Подкатегории услуг"
        ordering = ["name_of_category"]  # Сортировка по полю имени


class TheService(models.Model):
    name_of_service = models.CharField("Название конкретной услуги", max_length=100)
    price = models.IntegerField('Цена BYN')
    service = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, verbose_name='Выбрать подкатегорию услуг',
                                null=True)

    def __str__(self):
        return '%s' % self.name_of_service

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["name_of_service"]  # Сортировка по полю имени


class Sale(models.Model):
    objects = None
    name_of_sale = models.CharField("Название акции", max_length=150)
    text_details = models.TextField("Описание акции", max_length=1000)
    data = models.DateField('Дата публикации акции', null=True)
    img = models.ImageField('Изображение', upload_to='sale/')

    def __str__(self):
        return '%s' % self.name_of_sale

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"


class Worker(models.Model):
    objects = None
    first_name = models.CharField('Имя сотрудника', max_length=100)
    second_name = models.CharField('Фамилия сотрудника', max_length=100)
    field = models.ManyToManyField(ServiceCategory, help_text="Выберите категорию услуг",
                                   verbose_name="Категория услуг")
    img = models.ImageField('Изображение', upload_to='worker/')

    def __str__(self):
        return f'{self.second_name} {self.first_name}'

    def get_service_category(self):
        lst_service = []
        for category in self.field.all():
            lst_service.append(category.name_of_category)
        return lst_service

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Order(models.Model):
    name = models.CharField('Имя заказчика', max_length=50)
    phone = models.CharField('Номер телефона заказчика', max_length=13)
    email = models.EmailField('Email заказчика', default=None)
    details = models.TextField('Комментарий', max_length=500)
    status = models.BooleanField("Заказ обработан", default=False)
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.phone}'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Images(models.Model):
    objects = None
    img = models.ImageField('Фото наших работ', upload_to='our_works/')

    def __str__(self):
        return f'{self.img}'

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"
