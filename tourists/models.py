from django.db import models


class Locals(models.Model):
    
    first_name =  models.CharField('first name', max_length= 120)
    second_name =  models.CharField('last name', max_length= 120)
    location =  models.CharField('location', max_length= 120)
    number =  models.IntegerField('phone number')
    password =  models.CharField('password', max_length= 120)

    def __str__(self):
        return self.first_name

 
class hotels(models.Model):
    name =  models.CharField('name', max_length= 120)
    password =  models.CharField('password', max_length= 120)
    location_id =   models.CharField('Location', max_length= 120)
    a_rooms =  models.IntegerField('available rooms', max_length= 120)
     
     
    
    def __str__(self):
        return self.name



class Hotel_add(models.Model):
    name =  models.CharField('name', max_length= 120)
    location =   models.CharField('Location', max_length= 120)
    a_rooms =  models.IntegerField('available rooms', max_length= 120)
    premium_pack =   models.CharField('premium', max_length= 120)
    normal_pack =   models.CharField('normal', max_length= 120)
    budget_pack =   models.CharField('budget', max_length= 120)
    Details =  models.CharField('Details', max_length= 120)
    
    def __str__(self):
        return self.name




class Hotel_rating(models.Model):
    Name =  models.CharField('Name', max_length= 120)
    Rating =   models.IntegerField('Rating', max_length= 120)
    Review =   models.CharField('Review', max_length= 120)
    Choose_Hotel = models.ManyToManyField(Hotel_add, blank=True)

    def __str__(self):
        return self.Local_Name


 
class POI_add(models.Model):
    POI_name =  models.CharField('POI_Name', max_length= 120)
    location = models.CharField('POI_location',max_length=30)

    def __str__(self):
        return self.POI_name 


class POI_rating(models.Model):
    Name =  models.CharField('Name', max_length= 120)
    Rating =   models.IntegerField('Rating', max_length= 120)
    Review =   models.CharField('Review', max_length= 120)
    Choose_POI = models.ManyToManyField(POI_add, blank=True)
    
   
    def __str__(self):
        return self.Local_Name



class trip_add(models.Model):
    Tourist_Name =  models.CharField('Tourist_Name', max_length= 120) 
    Choose_POI1 =  models.CharField('POI_Name1', max_length= 120) 
    Choose_POI2 =  models.CharField('POI_Name2', max_length= 120) 
    Choose_POI3 =  models.CharField('POI_Name3', max_length= 120) 
    Choose_Hotel1 = models.CharField('Hotel_Name1', max_length= 120) 
    Choose_Hotel2 = models.CharField('Hotel_Name2', max_length= 120) 
    
   
    def __str__(self):
        return self.Tourist_Name

packages = [
    ('premium', 'Premium'),
    ('middle', 'Middle'),
    ('budget', 'Budget'), 
]




class bookings(models.Model):
    name =  models.CharField('Customer Name', max_length= 120)
    sdate = models.DateField('Start date')
    edate = models.DateField('End date')
    Package =  models.CharField('Packages', max_length= 120)
    Choose_Hotel = models.ManyToManyField(Hotel_add, blank=True)

 
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