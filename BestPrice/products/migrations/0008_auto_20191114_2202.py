
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20191112_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url_morrisons',
            field=models.CharField(db_index=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='url_sainsburys',
            field=models.CharField(db_index=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='url_tesco',
            field=models.CharField(db_index=True, max_length=250),
        ),
    ]
