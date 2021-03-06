# Generated by Django 3.1.4 on 2020-12-11 12:38

from django.db import migrations, transaction
from django.utils import timezone
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('forumMessages', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        from forumMessages.models import Message, Category

        category_test_data = [
            'General_Discussions',
            'Course_Related',
            'Palavra',
        ]
        with transaction.atomic():
            for name in category_test_data:
                Category(name=name).save()

        message_test_data = [
            (User(UserName='a'), timezone.now, 'Lorem ipsum', Category(name='Course_Related')),
            (User(UserName='b'), timezone.now, 'Dolor sit amet', Category(name='General_discussions')),
        ]
        with transaction.atomic():
            for user, date, text, categories in message_test_data:
                Message(user=user, date=date, text=text, categories=categories).save()

    operations = [
        migrations.RunPython(generate_data)
    ]
