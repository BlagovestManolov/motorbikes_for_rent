from django.db import models
from django.utils.text import slugify
from parler.models import TranslatableModel, TranslatedFields


class Tour(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(
            'Tour title',
            max_length=100,
            null=False,
            blank=False,
        ),

        date_of_creation=models.DateField(
            auto_now_add=True,
            blank=False,
        ),

        information=models.TextField(
            'Information about the tour',
        ),

        main_image=models.FileField(
            upload_to='tour/main_image/',
        ),

        price=models.PositiveIntegerField(
            'Tour price',
        ),

        slug=models.SlugField(
            null=True,
            blank=True,
        ),
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class TourMoreInformation(TranslatableModel):
    tour = models.OneToOneField(
        Tour,
        on_delete=models.CASCADE,
        related_name='more_information',
    )

    translations = TranslatedFields(
        more_information=models.TextField(
            'More information'
        ),
    )


class TourImage(models.Model):
    tour = models.ForeignKey(
        Tour,
        related_name='images',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    date_of_creation = models.DateField(
        auto_now_add=True,
        blank=True,
    )

    image = models.FileField(
        upload_to='tour/more_images/',
        null=False,
        blank=False,
    )

    generated_image_number = models.PositiveIntegerField(
        default=0,
        editable=False,
    )

    def save(self, *args, **kwargs):
        existing_img_count = TourImage.objects.filter(tour=self.tour).count()
        self.generated_image_number = existing_img_count + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.tour.name} Image {self.generated_image_number}'
