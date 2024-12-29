from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default=' Хз, ты ничего не ввела')
    anons = models.CharField('Анонс', max_length=250, default=' Хз, ты ничего не ввела')
    full_text = models.TextField('Статья ')
    date = models.DateTimeField('Дата публикации ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость "
        verbose_name_plural = "Новости"

class User(models.Model):
    username = models.CharField('Имя пользователя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Почта', unique=True)
    password = models.CharField(max_length=128, default='11111111')
    reg_date = models.DateTimeField('Дата регистрации', auto_now_add=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Brand(models.Model):
    name = models.CharField('Название бренда', max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField('Название категории', max_length=100)
    description = models.TextField('Описание категории')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('Название продукта/поста', max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    external_link = models.URLField('Ссылка на источник')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField('Описание продукта/поста')
    image = models.ImageField(upload_to="news/static/news/img", null=True, blank=True)

    def __str__(self):
        return self.title

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class GoodsCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

