# Generated by Django 2.0.1 on 2018-06-29 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ideax', '0018_comment_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='challenges/')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField(max_length=140, null=True)),
                ('requester', models.TextField(max_length=140, null=True)),
                ('description', models.TextField(max_length=2500)),
                ('limit_date', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField()),
                ('featured', models.BooleanField(default=False)),
                ('discarted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideax.UserProfile')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ideax.Category')),
            ],
        ),
        migrations.AddField(
            model_name='idea',
            name='challenge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ideax.Challenge'),
        ),
    ]