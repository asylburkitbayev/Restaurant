from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(upload_to='foods/', blank=True, null=True)
    desc = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class BookTable(models.Model):
    name = models.CharField(max_length=55)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    date = models.DateTimeField()
    persons = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return f"Клиент {self.name} забронировал столик {self.table.name}"


class Response(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    subjects = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/')
    index = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    text1 = models.CharField(max_length=50)
    text2 = models.CharField(max_length=50)
    text3 = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.name

