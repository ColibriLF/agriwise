# Generated by Django 4.2 on 2024-04-13 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_registo_parcela'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registo',
            name='parcela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registo', to='app.parcela'),
        ),
    ]
