from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    def __str__(self):
        return self.first_name

class cyber_attacks(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to="data",blank=True)
    link=models.URLField()
    def __str__(self):
        return self.title

class latest_news(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to="data",blank=True)
    date=models.DateField()
    def __str__(self):
        return self.title

class security_threats(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to="data",blank=True)
    def __str__(self):
        return self.name

class lawyer(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    address=models.TextField()
    firm=models.CharField(max_length=30)
    image=models.ImageField(upload_to="data",blank=True)
    experience=models.CharField(max_length=100)
    info=models.TextField()
    email=models.EmailField()
    map1=models.TextField()
    def __str__(self):
        return self.name

class ngo(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField(max_length=10)
    address=models.TextField()
    slogan=models.TextField()
    image=models.ImageField(upload_to="data",blank=True)
    website=models.URLField()
    info=models.TextField()
    email=models.EmailField()
    map1=models.TextField()
    def __str__(self):
        return self.name

class policestation(models.Model):
    name=models.CharField(max_length=100)
    contact=models.IntegerField()
    address=models.TextField()
    map1=models.TextField()
    def __str__(self):
        return self.name

class helpline(models.Model):
    name=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    contact=models.IntegerField()
    def __str__(self):
        return self.name
    
class laws(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    def __str__(self):
        return self.name

class help1(models.Model):
    title= models.CharField(max_length=500, unique=True)
    message= models.TextField()
    def __str__(self):
        return self.title

class review1(models.Model):
    title= models.CharField(max_length=500, unique=True)
    message= models.TextField()
    def __str__(self):
        return self.title
    
class contact1(models.Model):
    name=models.CharField(max_length=100, unique=True)
    phone=models.IntegerField()
    email=models.EmailField()
    subject= models.CharField(max_length=500, unique=True)
    message= models.TextField()
    def __str__(self):
        return self.name

class register1(models.Model):
    name=models.CharField(max_length=100, unique=True)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    confirmpassword=models.CharField(max_length=100)
    dob=models.CharField(null=True, blank=True, max_length=100)
    gender=models.CharField(max_length=1,choices=[('m','male'),('f','female')], default='f')
    city=models.CharField(max_length=100, null=True, blank=True)
    state=models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

class tips(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    def __str__(self):
        return self.title

class crimes(models.Model):
    name=models.CharField(max_length=200)
    description=RichTextField(blank=True,null=True)
    def __str__(self):
        return self.name

class alerts(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    infection_mechanism=models.TextField()
    image=models.ImageField(upload_to="data",blank=True)
    indicator_of_compromise=RichTextField(blank=True,null=True)
    recommendations=models.TextField()
    references=models.TextField()
    def __str__(self):
        return self.name

class dgpsuraksha(models.Model):
    title=models.CharField(max_length=200)
    docs=models.FileField()
    def __str__(self):
        return self.title

class security_tips(models.Model):
    title=models.CharField(max_length=200)
    docs=models.FileField()
    def __str__(self):
        return self.title


class product(models.Model):
    name=models.CharField(max_length=200, primary_key=True) 
    description=models.TextField()
    def __str__(self):
        return self.name

class vulnerabilities1(models.Model):
    vid=models.CharField(max_length=100, primary_key=True)
    name=models.CharField(max_length=200)
    description=models.TextField()
    severity=models.CharField(max_length=500)
    references=models.URLField()
    def __str__(self):
        return self.name

class productvuln(models.Model):
    did=models.ForeignKey(vulnerabilities1, on_delete=models.CASCADE)
    name=models.ForeignKey(product, on_delete=models.CASCADE)
    summary=models.TextField()    
    severity=models.CharField(max_length=500)
    

class newsletter(models.Model):
    email=models.CharField(max_length=200)
    def __str__(self):
        return self.email

class blog(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="data",blank=True)
    content=RichTextField(blank=True,null=True)
    date=models.DateField()
    def __str__(self):
        return self.title
