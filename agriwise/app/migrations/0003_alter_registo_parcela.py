# Generated by Django 4.2 on 2024-04-13 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_parcela_registo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registo',
            name='parcela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parcelas', to='app.parcela'),
        ),
    ]