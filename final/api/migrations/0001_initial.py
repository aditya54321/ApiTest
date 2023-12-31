# Generated by Django 4.2.4 on 2023-08-22 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discountPercentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('stock', models.IntegerField()),
                ('brand', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('thumbnail', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(related_name='productImages', to='api.productimage'),
        ),
    ]
