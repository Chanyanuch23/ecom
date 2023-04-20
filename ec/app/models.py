from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_SIZE = (
    ('Xs','Xs'),
    ('S','S'),
    ('M','M'),
    ('L','L'),
)

CATEGORY_CHOICES = (
    ('TO','Top'),
    ('SK','Skirt'),
    ('PA','Pants'),
    ('SH','Shorts'),

)

COLOR = (
    ('black','black'),
    ('navy','navy'),
    ('gray','gray'),
    ('yellow','yellow'),
    ('LB','light blue'),
    ('red','red'),
    ('white','white'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField() 
    discription = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    size = models.CharField(choices=CATEGORY_SIZE ,max_length=2)
    color = models.CharField(choices=COLOR,max_length=10)
    product_image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the wat','On the wat'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)
    
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    rezorpay_order_id = models.CharField(max_length=100, blank=True,null=True)
    rezorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    rezorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    