from django.db import models
from django.utils import timezone



class Book(models.Model):
    pdf = models.FileField(upload_to='books/pdfs/')


    Contr_ID = models.IntegerField(null = True)
    ContrN = models.CharField(max_length=10)
    Uch_ID = models.IntegerField(null = True) #ограничение длинные int игнорится 
    AttachType = models.CharField(max_length=30, null = True)
    Attachimage = models.ImageField(upload_to='books/covers/', null=True, blank=True)
    AttachDate = models.DateField(default=timezone.now)
    MainAttach_ID =models.IntegerField(null = True)  #ограничение длинные int игнорится 
    Note = models.CharField(max_length=255, null = True, blank=True)
    '''STATUS_CHOICES = [
    ('new', 1),
    ('old', 2),
    ('redacted', 3)
    ]
    Status = models.IntegerField(
        choices= STATUS_CHOICES,
        default= 'new')'''
    Status = models.IntegerField(default = 1)    
    EditDate = models.DateField(default=timezone.now)


    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

