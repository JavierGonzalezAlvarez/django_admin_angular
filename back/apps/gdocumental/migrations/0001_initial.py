# Generated by Django 3.2 on 2021-08-23 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps_empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GDClasificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('clasificacion', models.CharField(max_length=50, unique=True, verbose_name='Clasificacion')),
                ('observacion', models.TextField(blank=True, max_length=250, verbose_name='Observaciones')),
                ('usuario_crea', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_modifica', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Clasificacion Documental',
            },
        ),
        migrations.CreateModel(
            name='GDocumental',
            fields=[
                ('estado', models.BooleanField(default=True, verbose_name='Activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Número de Registro Documental')),
                ('fecha_alta', models.DateTimeField(auto_now_add=True, verbose_name='Fecha alta')),
                ('descripcion', models.CharField(max_length=150, verbose_name='Descripción')),
                ('observacion', models.TextField(blank=True, max_length=250, verbose_name='Observación')),
                ('fichero_pdf', models.FileField(upload_to='./pdf', verbose_name='Adjuntar documento (.pdf)')),
                ('pk_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_empresas.empresa', verbose_name='Empresa')),
                ('pk_gdclasificacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apps_gdocumental.gdclasificacion', verbose_name='Clasificacion')),
                ('usuario_crea', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_modifica', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Gestión Documental',
            },
        ),
    ]
