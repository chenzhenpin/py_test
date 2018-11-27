#coding=utf-8
from django.db import models

# Create your models here.



class Question(models.Model):
    question_text = models.CharField('问题描述',max_length=200)
    pub_date = models.DateTimeField('日期时间')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField('选择',max_length=200)
    votes = models.IntegerField(default=0)




    def __str__(self):
        return self.choice_text