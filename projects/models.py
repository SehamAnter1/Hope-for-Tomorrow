from django.db import models
from django.conf import settings

# Create your models here.

# ________ Categories Model ________
class Category (models.Model):
    title=models.CharField(max_length=255)
    title_ar=models.CharField(max_length=255)
    description_ar =models.TextField(null=True,blank=True)
    def __str__(self):
        return self.title
        

# ________ Project Model ________        
class Project (models.Model):
    title=models.CharField(max_length=255)
    title_ar=models.CharField(max_length=255)
    description =models.TextField(null=True,blank=True)
    description_ar =models.TextField(null=True,blank=True)
    cover = models.ImageField(upload_to='project_covers/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='project')
    categories=models.ManyToManyField(Category, related_name='project',blank=True)
    price_goal = models.DecimalField(max_digits=20, decimal_places=2)
    donations_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    donations_count = models.IntegerField(default=0)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    # update progress
    def __str__(self):
        return self.title
    def update_progress(self):
        if(self.donations_count>0):
            self.progress = (self.donations_amount/self.price_goal)*100
            self.save()

# ________ Projects Images Model ________        
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"Image for {self.project.title}"
        
# ________ Donation Model ________        
class Donation(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name="donations")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='donations')

    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')])
    payment_reference = models.CharField(max_length=100, null=True, blank=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.project