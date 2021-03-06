# Generated by Django 2.0.4 on 2018-05-19 11:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeTime', models.DateTimeField(default=datetime.datetime.now, verbose_name='点赞时间')),
                ('user_all_like', models.CharField(blank=True, max_length=500, null=True, verbose_name='所有喜欢的')),
                ('beLike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article', verbose_name='被赞文章')),
                ('userLike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='点赞人')),
            ],
            options={
                'verbose_name': '点赞动作',
                'verbose_name_plural': '点赞动作',
            },
        ),
    ]
