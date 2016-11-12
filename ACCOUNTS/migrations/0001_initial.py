# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-12 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment_languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Programming_Language', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AssignmentID', models.CharField(max_length=20, null=True)),
                ('CreationDate', models.DateField(max_length=20)),
                ('StartTime', models.DateTimeField()),
                ('EndTime', models.DateTimeField()),
                ('Description', models.TextField()),
                ('Language', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AId', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='ACCOUNTS.AssignmentDetail')),
            ],
        ),
        migrations.CreateModel(
            name='AssistantDetail',
            fields=[
                ('TaId', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('Batch', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Course_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseId', models.CharField(max_length=20)),
                ('Year', models.CharField(max_length=4)),
                ('CourseName', models.CharField(max_length=20)),
                ('Description', models.TextField(max_length=200)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('Semester', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Courses_Ta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.DateField()),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ACCOUNTS.CourseDetail')),
                ('TaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ACCOUNTS.AssistantDetail')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorDetail',
            fields=[
                ('PId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('Qualification', models.TextField(max_length=20)),
                ('Interests', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionDetail',
            fields=[
                ('Qid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('QName', models.CharField(max_length=20)),
                ('QAuthor', models.CharField(max_length=20)),
                ('QDescription', models.CharField(max_length=20)),
                ('Image', models.ImageField(upload_to='images/albums/')),
                ('TestCaseInputFile1', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('TestCaseInputFile2', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('OutputFile1', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('OutputFile2', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('SId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=20)),
                ('Batch', models.CharField(max_length=20)),
                ('Branch', models.CharField(max_length=20)),
                ('Programme', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('SubmissionId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('PercentagePass', models.IntegerField()),
                ('Result', models.CharField(max_length=20)),
                ('SubmissionTime', models.DateTimeField()),
                ('StdOutError', models.TextField(null=True)),
                ('AssignmentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ACCOUNTS.AssignmentDetail')),
                ('QuestionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ACCOUNTS.QuestionDetail')),
                ('StudentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ACCOUNTS.StudentDetail')),
            ],
        ),
        migrations.AddField(
            model_name='coursedetail',
            name='PId',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='ACCOUNTS.ProfessorDetail'),
        ),
        migrations.AddField(
            model_name='course_student',
            name='CourseId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ACCOUNTS.CourseDetail'),
        ),
        migrations.AddField(
            model_name='course_student',
            name='SId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ACCOUNTS.StudentDetail'),
        ),
        migrations.AddField(
            model_name='assistantdetail',
            name='CourseId',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='ACCOUNTS.CourseDetail'),
        ),
        migrations.AddField(
            model_name='assignmentquestion',
            name='QId',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='ACCOUNTS.QuestionDetail'),
        ),
        migrations.AddField(
            model_name='assignmentdetail',
            name='Courseid',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='ACCOUNTS.CourseDetail'),
        ),
        migrations.AddField(
            model_name='assignment_languages',
            name='AssignmentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ACCOUNTS.AssistantDetail'),
        ),
    ]
