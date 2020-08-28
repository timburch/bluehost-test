import re
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

PRODUCT_NAME_OPTIONS = (
    ("", ""),
    ("domain", "Domain"),
    ("hosting", "Hosting"),
    ("email", "Email"),
    ("pdomain", "P-Domain"),
    ("edomain", "E-Domain")
)

class Product(models.Model):
    CustomerId = models.CharField(max_length=20)
    ProductName = models.CharField(choices=PRODUCT_NAME_OPTIONS, max_length=7)
    Domain = models.CharField(max_length=253)
    StartDate = models.DateTimeField(auto_now_add=True)
    DurationMonths = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def save(self, *args, **kwargs):
        self.validate_domain()
        self.validate_duration()
        self.check_for_duplicate()
        super(Product, self).save(*args, **kwargs)
        if self.ProductName == "pdomain":
            self.secure_domain()

    def secure_domain(self):
        return

    def validate_domain(self):
        if self.ProductName == 'domain' or self.ProductName == 'pdomain':
            if re.search("\.(com|org)$", self.Domain) is None:
                raise ValidationError('Domain must be .com or .org')
        if self.ProductName == 'edomain':
            if re.search("\.edu$", self.Domain) is None:
                raise ValidationError('Domain must be .edu')
        if self.ProductName == 'hosting' or self.ProductName == 'email':
            qs = Product.objects.filter(
                Domain__iexact=self.Domain
            ).filter(
                ProductName__in=['domain', 'edomain', 'pdomain']
            )
            if qs.count() == 0:
                raise ValidationError('Domain registration does not exist')

    def validate_duration(self):
        if self.ProductName in ['domain', 'edomain', 'pdomain']:
            if self.DurationMonths % 12 > 0:
                raise ValidationError('Duration must be multiple of 12')

    def check_for_duplicate(self):
        if hasattr(self, 'Id') and self.Id:
            return
        qs = Product.objects.filter(
            ProductName__iexact=self.ProductName
        ).filter(
            Domain__iexact=self.Domain
        )
        if qs.count() > 0:
            raise ValidationError('Duplicate product')