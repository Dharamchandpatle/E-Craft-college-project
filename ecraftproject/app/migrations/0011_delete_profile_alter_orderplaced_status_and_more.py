# Generated by Django 5.0.6 on 2024-05-22 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_address_profile_address1_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('Delivered', 'Delivered'), ('On The Way', 'On The Way'), ('Packed', 'Packed')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('JC', 'juteCraft'), ('PC', 'paintingCraft'), ('MC', 'metalCraft'), ('BC', 'bambooCraft')], max_length=2),
        ),
    ]
