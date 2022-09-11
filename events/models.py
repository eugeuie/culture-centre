from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)
    building = models.IntegerField(primary_key=True)

    class Meta:
        ordering = ["building"]
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self) -> str:
        return f"{self.name}, строение {self.building}"


class Category(models.Model):
    title = models.CharField(max_length=100)
    place = models.OneToOneField(
        Place, on_delete=models.CASCADE, primary_key=True
    )  # one to one

    class Meta:
        ordering = ["title"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.title


class Person(models.Model):
    name = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]
        verbose_name = "Человек"
        verbose_name_plural = "Люди"

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # many to one
    participants = models.ManyToManyField(Person)  # many to many

    class Meta:
        ordering = ["time"]
        verbose_name = "Событие"
        verbose_name_plural = "События"

    @property
    def place(self):
        return self.category.place

    def __str__(self) -> str:
        return self.title
