from django.db import models
from categories_app.models import Category
from author_app.models import Author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    category = models.ManyToManyField(Category,)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return f"{self.title} ---> {self.author}"
