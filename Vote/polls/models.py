# from django.db import models

# Create your models here.
# coding=utf-8
from django.db import models


# Create your models here.
# 问题
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question_text



# 选择
class Choice(models.Model):
    # contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text