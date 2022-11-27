from django.db import models



class Locals(models.Model):
    local_id =  models.CharField('Local ID', max_length= 120)
    first_name =  models.CharField('first name', max_length= 120)
    second_name =  models.CharField('last name', max_length= 120)
    location =  models.CharField('location', max_length= 120)
    number =  models.IntegerField('phone number')
    password =  models.CharField('password', max_length= 120)

    def __str__(self):
        return self.first_name

 

class hotels(models.Model):
    hotel_id =  models.CharField('hotel ID', max_length= 120)
    name =  models.CharField('name', max_length= 120)
    password =  models.CharField('password', max_length= 120)
    location_id =   models.CharField('Location', max_length= 120)
    a_rooms =  models.IntegerField('available rooms', max_length= 120)
    
    def __str__(self):
        return self.name

     


class Tourist(models.Model):
    user_id = models.CharField('Tourist ID', max_length= 120)
    cnic = models.IntegerField('CNIC')
    first_name = models.CharField('first name', max_length= 120)
    las_name = models.CharField('last name', max_length= 120)
    location = models.CharField('location', max_length= 120)
    password = models.CharField('password', max_length= 120)
    book_id = models.CharField('booking ID', max_length= 120)
    number = models.IntegerField('phone number')


    def __str__(self):
        return self.first_name