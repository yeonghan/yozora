from django.db import models

# Create your models here.



class blog_basic(models.Model):
    number = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)

    def __str__(self):
        #return self.number, self.title, self.text, self.create_date, self.modify_date
        return '%s %s %s %s %s'%(self.number, self.title, self.text, self.create_date, self.modify_date)
