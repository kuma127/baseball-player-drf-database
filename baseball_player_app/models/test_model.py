from django.db import models

class TestModel(models.Model):

    class Meta:
        db_table = 'test_model'
      
    marines = models.IntegerField(default=0)
    tigers = models.IntegerField(default=0)