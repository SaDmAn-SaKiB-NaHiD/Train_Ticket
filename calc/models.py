from django.db import models

# Create your models here.
class train_details(models.Model):
    train_id = models.IntegerField(primary_key=True)
    train_name = models.CharField(max_length=100)
    train_class =  models.CharField(max_length=10)
    seat_status = models.CharField(max_length=15, blank=True, null=True)
    available_date = models.DateTimeField()
    price = models.DecimalField(max_digits=5,decimal_places=2, default=0)
    #image  = models.ImageField(upload_to='pics')
    start_dest = models.CharField(max_length=100)
    end_dest = models.CharField(max_length=100)
    class Meta:
        db_table='train_details'
    #discount_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #video_url = models.CharField(max_length=200,blank=True,null=True)
