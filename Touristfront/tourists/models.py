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


class POI_add(models.Model):
    POI_name =  models.CharField('POI_Name', max_length= 120)
    location = models.CharField('POI_location',max_length=30)

    def __str__(self):
        return self.POI_name 


class POI_rating(models.Model):
    Local_Name =  models.CharField('Local Name', max_length= 120)
    Rating =   models.IntegerField('Rating', max_length= 120)
    Review =   models.CharField('Review', max_length= 120)
    Choose_POI = models.ManyToManyField(POI_add, blank=True)
    
   
    def __str__(self):
        return self.Local_Name



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