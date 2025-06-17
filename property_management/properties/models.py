from django.db import models

class Property(models.Model):
    street_number   = models.CharField(max_length=10, blank=True, null=True)
    street_name     = models.CharField(max_length=100, blank=True, null=True)
    complement      = models.CharField(max_length=100, blank=True, null=True)
    landlord        = models.CharField(max_length=100, blank=True, null=True)
    date_acquired   = models.DateField(blank=True, null=True)
    internet        = models.BooleanField(default=False)
    electricity     = models.BooleanField(default=False)
    gas             = models.BooleanField(default=False)
    trash           = models.BooleanField(default=False)
    date_released   = models.DateField(blank=True, null=True)
    contract_length = models.IntegerField(help_text="Contract length in months", default=0)

    property_video  = models.FileField(
        blank=True,
        null=True,
        help_text="Optional video tour of the property"
    )

    maintenance     = models.TextField(blank=True)
    rooms           = models.IntegerField(default=0)
    bathrooms       = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    type            = models.CharField(max_length=50, blank=True)
    rent            = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    rent_margin     = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    actual_margin   = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    profit          = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    real_profit     = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.street_number} {self.street_name}"

class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image    = models.ImageField()
    caption  = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image #{self.pk} for {self.property}"
