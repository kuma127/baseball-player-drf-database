from django.db import models


class Player(models.Model):
    POSITION_PITCHER = "投手"
    POSITION_CATCHER = "捕手"
    POSITION_INFIELDER = "内野手"
    POSITION_OUTFIELDER = "外野手"
    POSITION_SET = (
        (POSITION_PITCHER, "投手"),
        (POSITION_CATCHER, "捕手"),
        (POSITION_INFIELDER, "内野手"),
        (POSITION_OUTFIELDER, "外野手"),
    )

    no = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    position = models.CharField(
        choices=POSITION_SET,
        # default=POSITION_PITCHER,
        max_length=255)
    born = models.DateField(null=True)
    age = models.IntegerField(default=0)
    years = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    blood = models.CharField(max_length=255)
    pi_pa = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    salary = models.IntegerField(default=0)