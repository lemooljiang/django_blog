from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

# Create your models here.

class Article(models.Model):
    title = models.CharField(u"标题",max_length=255)
    brief = models.CharField(u"摘要",null=True,blank=True,max_length=255)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)
    content = models.TextField(u"文章内容")
    author = models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    pub_date = models.DateTimeField(u"发布时间",blank=True,null=True)
    last_modify = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(u"优先级",default=1000)
    head_img = models.ImageField(u"文章封面",upload_to="uploads")

    status_choices = (('draft',u"草稿"),
                      ('published',u"已发布"),
                      ('hidden',u"隐藏"),
                      )
    status = models.CharField(choices=status_choices,default='published',max_length=32)
    def __str__(self):
        return self.title
    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError(('Draft entries may not have a publication date.'))
        # Set the pub_date for published items if it hasn't been set already.
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()



class Category(models.Model):
    name = models.CharField(max_length=64,unique=True)
    brief = models.CharField(null=True,blank=True,max_length=255)
    slug = models.CharField(null=True,blank=True,max_length=255)
    set_as_top_menu = models.BooleanField(default=False)
    position_index = models.SmallIntegerField()
    admins = models.ManyToManyField("UserProfile",blank=True)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=32)
    def __str__(self):
        return self.name
