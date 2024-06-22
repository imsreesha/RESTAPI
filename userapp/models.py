from django.db import models

# Create your models here.

class BookModel(models.Model):
    book_id=models.CharField(max_length=100)
    book_name=models.CharField(max_length=100)
    book_author=models.CharField(max_length=100)
    book_description=models.TextField()
    book_price=models.IntegerField()
    book_image=models.ImageField(upload_to='img/',null=True)
    class Meta:
        db_table='booktable'