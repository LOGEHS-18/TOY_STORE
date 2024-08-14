

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('taxes', models.DecimalField(decimal_places=2, max_digits=10)),
                ('final_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('image', models.URLField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='myapp.order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=100)),
                ('subcategory', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
