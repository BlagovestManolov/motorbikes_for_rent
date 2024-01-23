from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Accessory(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(
            'Accessory name',
            max_length=255,
            null=False,
            blank=False,
        ),

        date_of_creation=models.DateField(
            auto_now_add=True,
            blank=False,
        ),

        type=models.CharField(
            max_length=20,
            default='Accessories',
            editable=False,
            blank=True,
        ),

        price_per_day=models.PositiveIntegerField(
            'Price per 1 day',
        ),

        main_image=models.ImageField(
            upload_to='accessories/main_images/',
        ),
    )

    def __str__(self):
        return self.name


class AccessoryImage(models.Model):
    accessory = models.ForeignKey(
        Accessory,
        related_name='images',
        on_delete=models.CASCADE,
    )

    date_of_creation = models.DateField(
        auto_now_add=True,
        blank=True,
    )

    image = models.FileField(
        upload_to='accessory/more_images/',
        blank=False,
        null=False,
    )

    generated_image_number = models.PositiveIntegerField(
        default=0,
        editable=False,
    )

    def save(self, *args, **kwargs):
        existing_img_count = AccessoryImage.objects.filter(accessory=self.accessory).count()
        self.generated_image_number = existing_img_count + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.accessory.name} Image {self.generated_image_number}'
