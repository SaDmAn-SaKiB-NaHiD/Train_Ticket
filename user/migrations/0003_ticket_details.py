from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticket_details',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('ticket_1', models.IntegerField()),
                ('ticket_2', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'ticket_details',
            },
        ),
    ]
