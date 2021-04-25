from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Source(models.Model):
    name = models.CharField(_('نام منبع'),max_length=200)

class CourseGroup(models.Model):
    name = models.CharField(_("نام گروه درسی"),max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(_("نام دسته بندی"),max_length=120)
    coursegroup = models.ForeignKey(CourseGroup , on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Periods(models.Model):
    name=models.CharField(_("نام دوره"),max_length=100)

    def __str__(self):
        return self.name

class Fileds(models.Model):
    name=models.CharField(_("نام رشته"),max_length=100)
    periods=models.ForeignKey(Periods,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Grades(models.Model):
    name=models.CharField(_("نام مقطع تحصیلی"),max_length=100)
    field = models.ForeignKey(Fileds,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Lesson(models.Model):
    name=models.CharField(_("نام درس"),max_length=150)
    coursegroup = models.ForeignKey(CourseGroup , on_delete= models.CASCADE)
    grade=models.ForeignKey(Grades,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Season(models.Model):
    name = models.CharField(_("نام فصل"),max_length=200)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)

class Choises(models.Model):
    option1=models.CharField(_("گزینه ۱"),max_length=150,null=False)
    option2=models.CharField(_("گزینه ۲"),max_length=150,null=False)
    option3=models.CharField(_("گزینه ۳"),max_length=150,null=True,blank=True)
    option4=models.CharField(_("گزینه ۴"),max_length=150,null=True,blank=True)
    option5=models.CharField(_("گزینه ۵"),max_length=150,null=True,blank=True)


class Questions(models.Model):

    TYPE_QUESTION= (
        ('1', 'Multi options'),
        ('2', 'Descriptive '),
        ('3', 'True or False'),
        ('4', 'blank')
    )
    written_by= models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    type_qu=models.TextField(_("نوع سوال"),max_length=1, choices=TYPE_QUESTION,null=False)
    text=models.CharField(_("متن سوال"),max_length=250,null=False)
    choices=models.ForeignKey(Choises,on_delete=models.CASCADE,blank=True, null=True)
    answer_choice=models.CharField(max_length=1)
    answer_text=models.CharField(_("متن جواب"),max_length=150,null=True, blank=True)
    question_image=models.ImageField(_("تصویر سوال"),upload_to='Questions_img',blank=True, null=True)
    question_voice=models.FileField(_("فایل صوتی سوال"),upload_to='Questions_voice',blank=True, null=True)
    answer_image=models.ImageField(_("تصویر جواب"),upload_to='Answer_img',blank=True, null=True)
    answer_voice=models.FileField(_("فایل صوتی جواب"),upload_to='Answer_voice',blank=True, null=True)
    hardness=models.PositiveIntegerField(_("درجه سختی"),validators=[MinValueValidator(1), MaxValueValidator(10)],null=False)
    numberـofـuses = models.IntegerField(_("تعداد استفاده"),validators=[MinValueValidator(0)],)
    number_of_correct_answers = models.IntegerField(_("تعداد جواب درست"),validators=[MinValueValidator(0)],)
    numberـofـincorrectـanswers = models.IntegerField(_("تعداد جواب غلط"),validators=[MinValueValidator(0)],)
    likes = models.IntegerField(_("لایک"),validators=[MinValueValidator(0)],)
    source=models.ForeignKey(Source,max_length=100,null=False ,on_delete=models.CASCADE)
    season=models.ManyToManyField(Season)

    @property
    def answer(self):
        if self.type_qu == 'Multi options' or 'True or False' :
            return self.answer_choice
        else:
            return self.answer_text

    @property
    def type_obj(self):
        if self.type == 1:
            return {'id': "1", 'name': "چند گزینه ای"}
        elif self.type == 2:
            return {'id': "2", 'name': "تشریحی"}
        if self.type == 3:
            return {'id': "3", 'name': "درست یا غلط"}
        else:
            return {'id': "5", 'name': "جای خالی"}
