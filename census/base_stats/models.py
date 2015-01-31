# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class CensusLearnSql(models.Model):
    age = models.IntegerField(blank=True, null=True)
    class_of_worker = models.CharField(db_column='class of worker', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    industry_code = models.CharField(db_column='industry code', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    occupation_code = models.CharField(db_column='occupation code', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    education = models.CharField(max_length=1000, blank=True)
    wage_per_hour = models.CharField(db_column='wage per hour', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    last_education = models.CharField(db_column='last education', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    marital_status = models.CharField(db_column='marital status', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    major_industry_code = models.CharField(db_column='major industry code', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    major_occupation_code = models.CharField(db_column='major occupation code', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    mace = models.CharField(max_length=1000, blank=True)
    hispanice = models.CharField(max_length=1000, blank=True)
    sex = models.CharField(max_length=1000, blank=True)
    member_of_labor = models.CharField(db_column='member of labor', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    reason_for_unemployment = models.CharField(db_column='reason for unemployment', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    fulltime = models.CharField(max_length=1000, blank=True)
    capital_gain = models.CharField(db_column='capital gain', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    capital_loss = models.CharField(db_column='capital loss', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    dividends = models.CharField(max_length=1000, blank=True)
    income_tax_liability = models.CharField(db_column='income tax liability', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    previous_residence_region = models.CharField(db_column='previous residence region', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    previous_residence_state = models.CharField(db_column='previous residence state', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    household_with_family = models.CharField(db_column='household-with-family', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    household_simple = models.CharField(db_column='household-simple', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    weight = models.CharField(max_length=1000, blank=True)
    msa_change = models.CharField(db_column='msa-change', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    reg_change = models.CharField(db_column='reg-change', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    within_reg_change = models.CharField(db_column='within-reg-change', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    lived_here = models.CharField(db_column='lived-here', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    migration_prev_res_in_sunbelt = models.CharField(db_column='migration prev res in sunbelt', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    num_persons_worked_for_employer = models.CharField(db_column='num persons worked for employer', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    family_members_under_118 = models.CharField(db_column='family members under 118', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    father_birth_country = models.CharField(db_column='father birth country', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    mother_birth_country = models.CharField(db_column='mother birth country', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    birth_country = models.CharField(db_column='birth country', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    citizenship = models.CharField(max_length=1000, blank=True)
    own_business_or_self_employed = models.CharField(db_column='own business or self employed', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    fill_questionnaire_for_veteran_s_admin = models.CharField(db_column=u"fill questionnaire for veteran's admin", max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    veterans_benefits = models.CharField(db_column='veterans benefits', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    weeks_worked_in_year = models.CharField(db_column='weeks worked in year', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.
    year = models.CharField(max_length=1000, blank=True)
    salary_range = models.CharField(db_column='salary range', max_length=1000, blank=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'census_learn_sql'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
