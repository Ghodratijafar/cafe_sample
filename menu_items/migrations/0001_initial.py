# Generated by Django 4.0.1 on 2022-01-21 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, help_text='This is deleted datetime', null=True, verbose_name='Deleted Datetime')),
                ('is_deleted', models.BooleanField(default=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, help_text='This is active status', verbose_name='Active status')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='menu_items.category', verbose_name='Parent Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, help_text='This is deleted datetime', null=True, verbose_name='Deleted Datetime')),
                ('is_deleted', models.BooleanField(default=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, help_text='This is active status', verbose_name='Active status')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Item name')),
                ('status', models.IntegerField(choices=[(0, 'Available for menu'), (1, 'Unavailable for Menu')], default=0)),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='Discount')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='menu_items', to='menu_items.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]