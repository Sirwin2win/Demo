# Generated by Django 2.2.3 on 2019-07-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
    ]