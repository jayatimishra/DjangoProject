from tkinter import CASCADE
from django.db import models

"""
Creating models is essentialy your database layout with additional metadata
In our poll app we'll create two models: Question and a Choice 
Each Choice is associated with a question





"""

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

"""
Here each model is represented by a class that subclasses django.db.models.Model
Each member has a number of class variables, each of which represents a database field in the model 







"""


"""
After you've made changes to the models.py file 
It is time to let Django know that you've made some changes and that you'd like the changes to be stored as a migration.
For that the following command is used:
python manage.py makemigrations polls


Now to create the data models that you want to create in your app you will have to run the following command:
python manage.py migrate

This runs the migrations for you and manages your database schema automatically








"""