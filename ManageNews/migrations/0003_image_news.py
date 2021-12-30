# Generated by Django 4.0 on 2021-12-30 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ManageNews', '0002_news_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='image/')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ManageNews.news')),
            ],
        ),
    ]