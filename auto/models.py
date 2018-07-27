# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AutoConfigInfos(models.Model):
    objects = models.Manager()
    server_id = models.BigAutoField(db_column='server_ID', primary_key=True)  # Field name made lowercase.
    server_num = models.CharField(max_length=50)
    board = models.CharField(max_length=50)
    cpu = models.CharField(max_length=50)
    memory_bank = models.CharField(max_length=50)
    hard_disk = models.CharField(max_length=50)
    raid = models.CharField(max_length=50)
    vga = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)
    hba = models.CharField(max_length=50)
    net_card = models.CharField(max_length=50)
    fc_card = models.CharField(max_length=50)
    inspect_time = models.DateField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auto_config_infos'
