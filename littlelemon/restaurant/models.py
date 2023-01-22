from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()
    menu_item_description = models.TextField(max_length=1000, default="")

    def __str__(self):
        return f"{self.title}: {str(self.price)}"

    def get_item(self):
        return f"{self.title}: {str(self.price)}"


class Booking(models.Model):
    name = models.CharField(max_length=255)
    guests_num = models.SmallIntegerField()
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self):
        return self.first_name
