# Generated by Django 3.1.7 on 2021-03-14 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Musica', '0004_canciones_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='autorcancion',
            name='genero',
            field=models.CharField(blank=True, choices=[('ROCK', 'ROCK'), ('POP', 'POP'), ('ALTERNATIVA', 'ALTERNATIVA')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='autorcancion',
            name='autor',
            field=models.ForeignKey(default='Undefinided', on_delete=django.db.models.deletion.CASCADE, to='Musica.autor'),
        ),
        migrations.CreateModel(
            name='lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancionL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musica.autorcancion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('usuariocreatedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usercreacion', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
