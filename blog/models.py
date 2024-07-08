from django.db import models
from django.contrib.auth.models import User
from .helpers import SaveMedia

# Create your models here.

class Auther(models.Model):
    objects = None
    first_name = models.CharField(verbose_name="ISM", max_length=50)
    last_name = models.CharField(verbose_name="FAMILIYA", max_length=50)
    # title = models.ForeignKey(Books, on_delete=models.CASCADE)
    birth_day = models.DateField(verbose_name="TUG'ILGAN SANASI")
    create_date = models.DateTimeField(verbose_name="RUYHATDAN O'TGAN SANA", auto_now_add=True)

    def __str__(self):
        return (f"{self.first_name}  "
                f"{self.last_name}")

    def get_full_info(self):
        return (f" {self.first_name}  "
                f"{self.last_name}")

class Books(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField()
    auther = models.ForeignKey(Auther, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=SaveMedia.save_image_path, null=True)
    price = models.DecimalField(max_digits=3, decimal_places=0)
    count = models.PositiveIntegerField(default=1)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Book: {self.title}"
                f"Description: {self.description}"
                f"Auther: {self.auther}"
                f"Price: {self.price}"
                f"Count: {self.count}")

class Commit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    book = models.ManyToManyField(Books)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"User: {self.user}"
                f"Comment: {self.text}"
                f"Book: {self.book}")

class Country(models.Model):
    address = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now_add=True)