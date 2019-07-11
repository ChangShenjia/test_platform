# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('username', models.CharField(verbose_name='用户名', max_length=20, unique=True)),
                ('password', models.CharField(verbose_name='密码', max_length=20)),
                ('email', models.EmailField(verbose_name='邮箱', max_length=254, unique=True)),
                ('status', models.IntegerField(verbose_name='有效/无效', default=1)),
            ],
            options={
                'verbose_name': '用户信息',
                'db_table': 'UserInfo',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('type_name', models.CharField(max_length=20)),
                ('type_desc', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '用户类型',
                'db_table': 'UserType',
            },
        ),
    ]
