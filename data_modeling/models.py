from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=20)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Post(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Post by {self.customer} at {self.created_at}"
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content = models.TextField()
    commented_at = models.DateTimeField(auto_created=True)
    
    
    def __str__(self):
        return f"Comment by {self.customer} on {self.post} at {self.commented_at}"
    
    
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='likes')
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.customer} on {self.post} at {self.liked_at}"

    class Meta:
        unique_together = ('post', 'customer')
    
    

# Create your models here.
