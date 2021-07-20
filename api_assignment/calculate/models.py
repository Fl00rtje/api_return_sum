from django.db import models


class Number(models.Model):
    num_1 = models.IntegerField(verbose_name="Number 1")
    num_2 = models.IntegerField(verbose_name="Number 2")
    total = models.IntegerField(verbose_name="Total of number 1 and number 2", null=True)

    def __str__(self):
        return f"Number 1: {self.num_1} \n" \
               f"Number 2: {self.num_2} \n" \
               f"Total: {self.total}"
