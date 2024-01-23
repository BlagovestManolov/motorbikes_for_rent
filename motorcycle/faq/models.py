from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class DepositAndInsurance(TranslatableModel):
    translations = TranslatedFields(
        question=models.CharField(
            'Question',
            max_length=300,
            null=False,
            blank=False,
        ),

        date_of_creation=models.DateField(
            auto_now_add=True,
            blank=True,
        ),

        answer=models.TextField(
            'Answer',
            blank=False,
            null=False,
        ),
    )


class Condition(TranslatableModel):
    translations = TranslatedFields(
        question=models.CharField(
            'Question',
            max_length=300,
            null=False,
            blank=False,
        ),

        date_of_creation=models.DateField(
            auto_now_add=True,
            blank=True,
        ),

        answer=models.TextField(
            'Answer',
            blank=False,
            null=False,
        ),
    )
