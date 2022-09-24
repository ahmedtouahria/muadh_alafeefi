from django.db import models
from colorfield.fields import ColorField
# Create your models here.
from ckeditor.fields import RichTextField

class Skill(models.Model):
    skill = models.CharField('Skill name', max_length=200)
    percentage =models.PositiveIntegerField(default=0)
    color = ColorField(default='#1967ee')
    def __str__(self):
        return self.skill
    

class Experience(models.Model):
    post = models.CharField('Post', max_length=200)
    date_start = models.DateField("Date start")
    date_end = models.DateField("Date end")
    company = models.CharField("company name" , max_length=200)
    def __str__(self):
        return self.post
class Education(models.Model):
    specialty = models.CharField('specialty', max_length=200)
    date_start = models.DateField("Date start")
    date_end = models.DateField("Date end")
    college = models.CharField("university or college name" , max_length=200)
    def __str__(self):
        return self.specialty
class Testimonial(models.Model):
    person = models.CharField(max_length=200)
    image= models.ImageField("Image", upload_to="persons")
    contenu = models.TextField("Contenu")
    url_site = models.URLField("site url", max_length=200,null=True,blank=True)
    job_title = models.CharField("Job title", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.person
class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    image= models.ImageField("Image", upload_to="persons")
    job_title = models.CharField("Job title", max_length=50)
    abstract =  RichTextField()
    def __str__(self):
        return self.name
    
class Section(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name
    def items(self):
        return SectionItem.objects.filter(section=self)
class SectionItem(models.Model):
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="sections")
    title=models.CharField("Title", max_length=200)
    site_url=models.URLField("Site url", max_length=200,null=True,blank=True)
    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return self.name
    
