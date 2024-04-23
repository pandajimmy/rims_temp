from django.db import models

class Sysrun(models.Model):
    customer_guid = models.CharField(primary_key=True, max_length=32)
    customer_prefix = models.CharField(max_length=5)
    type = models.CharField(db_column='Type', blank=True, max_length=10)  # Field name made lowercase.
    code = models.CharField(db_column='Code', blank=True, max_length=10)
    currentno = models.IntegerField(db_column='CurrentNo', blank=True, null=True)  # Field name made lowercase.
    nodigit = models.IntegerField(db_column='NoDigit', blank=True, null=True)  # Field name made lowercase.
    yyyy = models.IntegerField(db_column='YYYY', blank=True, null=True)  # Field name made lowercase.
    mm = models.IntegerField(db_column='MM', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sysrun'
        ordering = ('currentno',)

    def __str__(self):
        return self.currentno

    def get_absolute_url(self):
        return f'/{self.currentno}/' 