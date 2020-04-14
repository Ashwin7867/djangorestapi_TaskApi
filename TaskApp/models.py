from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length = 20)
    task_desc = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)
    date_created = models.DateField(auto_now = True)
    image = models.ImageField(upload_to = 'Images/', default ="Images/None/No-img.jpg")
    doc = models.FileField(upload_to = 'Doc/', default = 'Doc/None/No-doc.pdf')

    def __str__(self):
        return "%s" % self.task_name
