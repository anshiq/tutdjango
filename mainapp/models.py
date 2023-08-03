from django.db import models

# Create your models here.
class ToDoListUser(models.Model):
    name=  models.CharField(max_length=200)
    # username of the user creating todolist
    def __str__(self):
        return self.name   # it is like ToDoListUser  user = huname('anshik')  user will contain anshik  equal to huname.name
         
class ToDoListItems(models.Model):  # it will store items the user have to do
    user = models.ForeignKey(ToDoListUser,on_delete=models.CASCADE) #links the users to its todo items.
    text = models.CharField(max_length=400)
    isCompleted = models.BooleanField()
    def __str__(self):
        return self.text
