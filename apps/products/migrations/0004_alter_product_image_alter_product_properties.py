# Generated by Django 4.1.1 on 2022-10-07 12:08

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_alter_product_price_alter_product_properties"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=django_better_admin_arrayfield.models.fields.ArrayField(
                base_field=models.ImageField(
                    upload_to="products_images", verbose_name="Product Image"
                ),
                default=list,
                size=10,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="properties",
            field=django_better_admin_arrayfield.models.fields.ArrayField(
                base_field=models.CharField(blank=True, default="", max_length=100),
                default=list,
                size=10,
            ),
        ),
    ]