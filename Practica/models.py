from django.db import models

# Create your models here.


class User(models.Model):
    Name = models.CharField(max_length=60),
    Password = models.CharField(max_length=60),
    Public = models.BooleanField


class Image(models.Model):
    UserId = models.ForeignKey(User, on_delete=models.DO_NOTHING,),
    URL = models.CharField(max_length=300),
    Likes = models.IntegerField,
    Dislikes = models.IntegerField,
    Comments = models.IntegerField,


class Comment(models.Model):
    UserId = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
    ImageId = models.ForeignKey(Image, on_delete=models.DO_NOTHING,)
    Content = models.CharField(max_length=600)
    ReferencedCommentId = models.IntegerField


class Tag(models.Model):
    TagDescription = models.CharField(max_length=300)


class TaggedImage(models.Model):
    ImageID = models.ForeignKey(Image, on_delete=models.DO_NOTHING,)
    UserID = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
    TagID = models.ForeignKey(Tag, on_delete=models.DO_NOTHING,)


class Thread(models.Model):
    ThreadName = models.CharField(max_length=200)
    TagId = models.ForeignKey(Tag, on_delete=models.DO_NOTHING,)



