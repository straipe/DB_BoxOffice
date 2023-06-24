# Generated by Django 3.2.18 on 2023-05-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_certificate_genre_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='CusGrade',
            fields=[
                ('cus_grade_no', models.IntegerField(primary_key=True, serialize=False)),
                ('cus_grade_nm', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'cus_grade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cus_no', models.IntegerField(primary_key=True, serialize=False)),
                ('resident_no', models.BigIntegerField()),
                ('phone_no', models.IntegerField()),
                ('cus_nm', models.CharField(max_length=30)),
                ('regi_date', models.DateField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('cus_pw', models.CharField(blank=True, max_length=64, null=True)),
                ('cus_point', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MovGrade',
            fields=[
                ('mov_grade_no', models.IntegerField(primary_key=True, serialize=False)),
                ('mov_grade_nm', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'mov_grade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pay_no', models.IntegerField(primary_key=True, serialize=False)),
                ('pay_state', models.BooleanField(blank=True, null=True)),
                ('pay_amount', models.IntegerField()),
                ('pay_date', models.DateField(blank=True, null=True)),
                ('pay_point', models.IntegerField(blank=True, null=True)),
                ('pay_detail', models.CharField(blank=True, max_length=1200, null=True)),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('pay_met_no', models.IntegerField(primary_key=True, serialize=False)),
                ('pay_met_nm', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'payment_method',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('sched_no', models.IntegerField(primary_key=True, serialize=False)),
                ('run_date', models.DateField(blank=True, null=True)),
                ('run_round', models.IntegerField(blank=True, null=True)),
                ('run_type', models.IntegerField(blank=True, null=True)),
                ('run_end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'schedule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('seat_no', models.CharField(max_length=3, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'seat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeatGrade',
            fields=[
                ('seat_grade_no', models.IntegerField(primary_key=True, serialize=False)),
                ('seat_grade_nm', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'seat_grade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('thea_no', models.IntegerField(primary_key=True, serialize=False)),
                ('thea_nm', models.CharField(max_length=30)),
                ('thea_loc', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'theater',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('tic_no', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('reserv_date', models.DateField(blank=True, null=True)),
                ('issue', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ticket',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Certificate',
        ),
    ]
