from django.db import models
from django.contrib.auth.models import User   #admin ke ander user ko use karne ke liye eshaka use kare ge

# Create your models here.
class Tweet(models.Model): #eshme joh MODEL hai ushmekai shahi field hoti hai jo ham yaha define karke ushme se use kar shakte hai 
    user = models.ForeignKey(User, on_delete=models.CASCADE) #esh line me ham user ko set karte hai jo tweet karega aur bina user ke data delete nahi hoga
    text = models.TextField(max_length=500)  #esh field me ham tweet kar shakte hai eshme textfield decide karta hai ki ham ko box keshe dikhe ga
    created_at = models.DateTimeField(auto_now_add=True) #esh line me ham date aur time ko set karte hai jab tweet hota hai yeh field automatically set hota hai 
    updated_at = models.DateTimeField(auto_now=True) #esh line me ham data aur time ko set karte hai jab tweet update hota hai yeh field automatically set hota hai 
    
#eshe line me ham __str__ method ko define karte hai jisse admin pannel me tweet ka text aur user ka username dikhe ga
    def __str__(self): # __str__ method ko define karte hai jisse admin pannel me tweet ka text aur user ka username dikhe ga
        return f'{self.user.username} - {self.text[:20]}' #esh line me ham user ka username aur tweet ka text ke first 20 charachters ko return karte hai 
    
