from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class Grades(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Fileds(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Periods(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Choises(models.Model):
    option1=models.CharField(max_length=150)
    option2=models.CharField(max_length=150)
    option3=models.CharField(max_length=150)
    option4=models.CharField(max_length=150)

class Questions(models.Model):

    TYPE_QUESTION= (
        ('1', 'Four options'),
        ('2', 'Descriptive '),
        ('3', 'True or False'),
        ('4','blank')
    )

    type_qu=models.TextField(max_length=1, choices=TYPE_QUESTION,null=False)
    text=models.CharField(max_length=250)
    choices=models.ForeignKey(Choises,on_delete=models.CASCADE)
    answer=models.CharField(max_length=150)
    image=models.ImageField(upload_to='Questions_img',blank=True, null=True)
    hardness=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    source=models.CharField(max_length=100)
    grade=models.ManyToManyField(Grades,blank=False)
    field=models.ManyToManyField(Fileds)
    period=models.ManyToManyField(Periods,blank=False)