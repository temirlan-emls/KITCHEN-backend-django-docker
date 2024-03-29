# Generated by Django 4.1.1 on 2022-12-09 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_product_consumption_product_dimensions_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ("data_added",)},
        ),
        migrations.AlterField(
            model_name="product",
            name="sub_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="products.subcategory",
            ),
        ),
    ]
