

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(default=datetime.date.today, null=True, verbose_name='Дата рождения')),
                ('gender', models.SmallIntegerField(choices=[(0, 'Женский'), (1, 'Мужской')], default=1, verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Физическое лицо',
                'verbose_name_plural': 'Физические лица',
            },
        ),
    ]
