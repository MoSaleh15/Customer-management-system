from django.db import models

# category model
class Category(models.Model):
    name = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

#client model
class Record(models.Model):
    first_name = models.CharField(max_length=2500)    
    last_name = models.CharField(max_length=2500) 
    category = models.ForeignKey(Category,on_delete=models.CASCADE)#دي ال بتربط بينها وبين ال category
    phone = models.IntegerField()
    tall = models.IntegerField()
    wedgit = models.IntegerField()
    adrees = models.CharField(max_length=500)
    create_at = models.DateField()   

    def __str__(self):
        return self.first_name +' '+self.last_name
    
    class Meta:
        ordering = ['-create_at']