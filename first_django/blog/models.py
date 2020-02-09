from django.db import models

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    #create_date = models.DateField(auto_now_add=True)
    #modify_date = models.DateField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        #return self.number, self.title, self.text, self.create_date, self.modify_date
        return self.title
        return "{title} - {author}".format(title=self.title,
                                            author=self.author)
#    def __str__(self):

class Comment(models.Model):
    author = models.CharField(max_length=255)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:10]
