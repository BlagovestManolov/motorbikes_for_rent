from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Blog(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(
            'Blog title',
            max_length=500,
            blank=False,
            null=False,
        ),

        date_of_creation=models.DateField(
            auto_now_add=True,
            blank=False,
        ),

        information=models.TextField(
            'First and most important information about the blog',
            null=False,
            blank=False,
        ),

        main_image=models.FileField(
            upload_to='blog/main_images/',
        ),
    )

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    blog = models.ForeignKey(
        Blog,
        related_name='images',
        on_delete=models.CASCADE,
    )

    date_of_creation = models.DateField(
        auto_now_add=True,
        blank=True,
    )

    image = models.FileField(
        upload_to='blog/more_images/',
        null=False,
        blank=False,
    )

    generated_image_number = models.PositiveIntegerField(
        default=0,
        editable=False,
    )

    def save(self, *args, **kwargs):
        existing_img_count = BlogImage.objects.filter(blog=self.blog).count()
        self.generated_image_number = existing_img_count + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.blog.title} Image {self.generated_image_number}'


class BlogMoreInformation(TranslatableModel):
    blog = models.OneToOneField(
        Blog,
        on_delete=models.CASCADE,
        related_name='more_information',
    )

    translations = TranslatedFields(
        date_of_creation=models.DateField(
            auto_now_add=True,
            blank=False,
        ),

        more_information=models.TextField(
            'More information',
        ),
    )
