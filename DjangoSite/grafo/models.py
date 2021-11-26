from django.db import models

# Create your models here.
class Distance(models.Model):

    R1 = models.IntegerField()
    R2 = models.IntegerField()
    distance = models.FloatField()

    class Meta:
        verbose_name = ("Distance")
        verbose_name_plural = ("Distances")

    def __str__(self):
        return self.distance

    def get_absolute_url(self):
        return reverse("Distance_detail", kwargs={"pk": self.pk})
