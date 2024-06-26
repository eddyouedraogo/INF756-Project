# Generated by Django 4.2.5 on 2023-09-24 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RuleSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='RuleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('effect_on_health', models.IntegerField()),
                ('effect_on_mental', models.IntegerField()),
                ('effect_on_intelligence', models.IntegerField()),
                ('ruleSet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='simulation.ruleset')),
            ],
        ),
    ]
