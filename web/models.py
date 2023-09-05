from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/store_images/')
    deepLink = models.URLField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/category_images/')
    icon = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


# class Deal(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.TextField()
#     description = models.TextField()
#     coupon_code = models.CharField(max_length=50)
#     store = models.ForeignKey(Store, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     expires_at = models.DateTimeField()
#     added_at = models.DateTimeField(auto_now_add=True)
#     clicks = models.PositiveIntegerField(default=0)


class Coupon(models.Model):
    name = models.CharField(max_length=100)
    slug = models.TextField()
    description = models.TextField()
    coupon_code = models.CharField(max_length=50)
    deeplink = models.URLField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_deal = models.BooleanField(default=False)
    expires_at = models.DateTimeField()
    added_at = models.DateTimeField(auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name}'
