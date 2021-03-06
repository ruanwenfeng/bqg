# Generated by Django 2.0.7 on 2018-07-18 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='c_book', to='app.Books')),
                ('segment_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='c_segment', to='app.Books')),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='s_book', to='app.Books')),
            ],
        ),
    ]
