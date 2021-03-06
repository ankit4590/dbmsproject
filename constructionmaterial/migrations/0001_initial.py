# Generated by Django 3.0.5 on 2020-06-04 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_auto_20200525_1048'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='machine_and_tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('category', models.CharField(default='machine', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='rawmaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price_per_head', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='tools_issued_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qunatity_issued', models.IntegerField()),
                ('issued_date', models.DateField(auto_now_add=True)),
                ('returned_date', models.DateField(auto_now_add=True)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructionmaterial.machine_and_tools')),
            ],
        ),
        migrations.CreateModel(
            name='tool_to_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_quantity', models.IntegerField(default=0)),
                ('quantity_issued', models.IntegerField(default=0)),
                ('pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.project')),
                ('tool_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructionmaterial.machine_and_tools')),
            ],
        ),
        migrations.CreateModel(
            name='mat_to_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_quantiy', models.IntegerField(default=0)),
                ('quantity_demand', models.IntegerField(default=0)),
                ('mat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructionmaterial.rawmaterial')),
                ('pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.project')),
            ],
        ),
        migrations.CreateModel(
            name='machine_to_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.BigIntegerField(unique=True)),
                ('ava_status', models.CharField(default='available', max_length=100)),
                ('working_status', models.CharField(default='woking', max_length=100)),
                ('machine_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructionmaterial.machine_and_tools')),
                ('pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.project')),
            ],
        ),
        migrations.CreateModel(
            name='machine_maintainance_cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructionmaterial.machine_to_project')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.project')),
            ],
        ),
        migrations.CreateModel(
            name='machine_issued_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_date', models.DateField()),
                ('returned_date', models.DateField()),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructionmaterial.machine_to_project')),
                ('machine_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructionmaterial.machine_and_tools')),
            ],
        ),
        migrations.AddConstraint(
            model_name='tool_to_project',
            constraint=models.UniqueConstraint(fields=('tool_category', 'pro'), name='unique3'),
        ),
        migrations.AddConstraint(
            model_name='mat_to_project',
            constraint=models.UniqueConstraint(fields=('pro', 'mat'), name='uniquec'),
        ),
        migrations.AddConstraint(
            model_name='machine_to_project',
            constraint=models.UniqueConstraint(fields=('barcode', 'pro'), name='uniquec2'),
        ),
    ]
