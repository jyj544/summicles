# Generated by Django 3.1.5 on 2021-01-26 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('link', models.CharField(max_length=300, primary_key=True, serialize=False, verbose_name='기사 원본 링크')),
                ('category', models.CharField(max_length=64, verbose_name='카테고리')),
                ('title', models.CharField(max_length=300, verbose_name='제목')),
                ('article_date', models.CharField(blank=True, max_length=128, null=True, verbose_name='기사 발행 시간')),
                ('img', models.CharField(blank=True, max_length=256, null=True, verbose_name='기사 이미지')),
                ('contents', models.TextField(verbose_name='본문')),
                ('crawl_time', models.CharField(blank=True, max_length=128, null=True, verbose_name='크롤링 시간')),
                ('newspaper', models.CharField(blank=True, max_length=64, null=True, verbose_name='신문사')),
            ],
            options={
                'verbose_name': '기사 정보',
                'verbose_name_plural': '기사 정보',
                'db_table': 'article',
                'managed': False,
            },
        ),
    ]