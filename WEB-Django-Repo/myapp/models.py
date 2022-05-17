from django.db import models
from django.utils import timezone
# from datetime import datetime

# Create your models here.
# دائما لما بسوي داتا بيز بروح على ملف ثاني اسمه :   settings
# و اضيف البرنامج في جزء installed app
# بعد ذلك اعمل migration
# class Student(models.Model):

#     name = models.CharField(null=True,
#                                 max_length=20)

    # option = [
    #     ('male', 'male'),
    #     ('female', 'female')
    # ]
    # name = models.CharField(max_length=100,
    #                             null=True,
    #                             verbose_name="Student Name",
    #                             editable=True,
    #                             unique=True,
    #                             error_messages={
    #                                 'unique': 'تم اضافة هذا الطالب سابقا ...'
    #                             })
    # age = models.IntegerField(null=True)

    # mobile = models.CharField(max_length=10, 
    #                             null=True, 
    #                             unique=True, 
    #                             help_text='05xxxxxxxx', 
    #                             default='05')

    # email = models.EmailField(max_length=100, null=True)

    # dem = models.DecimalField(null=True, 
    #                             decimal_places=2,
    #                             max_digits=4)

    # gendar = models.CharField(null=True, 
    #                             max_length=10, 
    #                             choices=option)

    # joined_date = models.DateField(null=True)

    # joined_time = models.TimeField(null=True)

    # joined_date_time = models.DateTimeField(null=True,
    #                                             default=datetime.now)

    # student_file = models.FileField(null=True, 
    #                                     upload_to='myapp/upload_files')

    # student_imege = models.ImageField(null=True, 
    #                                     upload_to='upload_images')
    
    # student_bio = models.TextField(null=True)

    # agree = models.BooleanField(null=True,
    #                                 name='Srvice Agreement')

    # def __str__(self):
    #     return self.name

# class Teacher(models.Model):
#     name = models.CharField(null=True,
#                              max_length=20)

# class Email(models.Model):
#     user_email = models.EmailField(null=True)

#     def __str__(self):
#         return self.user_email

# class Client(models.Model):
#     name = models.CharField(null= True, 
#                                 max_length=20)
#     email = models.OneToOneField(Email, on_delete=models.CASCADE)
#     # PROTECT: لا تحذف ايميله
#     # CASCADE: احذف ايميله

#     def __str__(self):
#         return self.name

# class Food(models.Model):
#     food_name = models.CharField(max_length=20, null=True)

#     def __str__(self):
#         return self.food_name

# class Client(models.Model):
#     name = models.CharField(max_length=20, null= True)

#     food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return f'{self.name} - {self.food}'

# class Book(models.Model):
#     book_name = models.CharField(max_length=20, null=True)
    
#     def __str__(self):
#         return self.book_name

# class Store(models.Model):
#     name = models.CharField(max_length=20, null= True)
#     book = models.ManyToManyField(Book)

#     def __str__(self):
#         return self.name

# class Student(models.Model):
#     name = models.CharField(max_length=30, null=True)
#     age = models.IntegerField(null=True)
#     description = models.TextField(null=True)

#     class Meta:
#         # db_table = 'Student_Table'
#         # verbose_name = 'Student_Model'
#         # verbose_name_plural = 'Student'

#         # verbose_name = 'People'
#         # verbose_name_plural = 'People'
#         ordering = ['name']

#     def __str__(self):
#         return self.name


class Student(models.Model):
    name = models.CharField(max_length=30, null=True)

    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=10)

class Framework(models.Model):
    name = models.CharField(max_length=10) 
    language = models.ForeignKey(Language, on_delete=models.CASCADE)