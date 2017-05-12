from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# drop downs: http://stackoverflow.com/questions/31130706/dropdown-in-django-model
#             http://stackoverflow.com/questions/1117564/set-django-integerfield-by-choices-name
class Person(models.Model):
    MR = 0
    MRS = 1
    MISS = 2
    MS = 3
    PERSON_TITLES = (
        (MR, 'Mr'),
        (MRS, 'Mrs'),
        (MISS, 'Miss'),
        (MS, 'Ms'),
    )
    title = models.IntegerField(choices=PERSON_TITLES, default=MR)
    MALE = 0
    FEMALE = 1
    SEX = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    sex = models.IntegerField(choices=SEX, default=MALE)
    ASIAN_B = 0
    ASIAN_C = 1
    ASIAN_I = 2
    ASIAN_O = 3
    ASIAN_P = 4
    BLACK_A = 5
    BLACK_C = 6
    BLACK_O = 7
    MIXED = 8
    OTHER = 9
    TBC = 10
    TRAVEL = 11
    WHITE_E = 12
    WHITE_I = 13
    WHITE_O = 14
    WHITE_S = 13
    WHITE_W = 14
    ETHNICITY = (
        (ASIAN_B, 'Asian (Bangladesh)'),
        (ASIAN_C, 'Asian (Chinese)'),
        (ASIAN_I, 'Asian (Indian)'),
        (ASIAN_O, 'Asian (Other)'),
        (ASIAN_P, 'Asian (Pakistan)'),
        (BLACK_A, 'Black (African)'),
        (BLACK_C, 'Black (Caribbean)'),
        (BLACK_O, 'Black (Other)'),
        (MIXED, 'Mixed Background'),
        (OTHER, 'Other Ethinicity'),
        (TBC, 'TBC'),
        (TRAVEL, 'Traveller/Gypsy'),
        (WHITE_E, 'White (English)'),
        (WHITE_I, 'White (Irish)'),
        (WHITE_O, 'White (Other)'),
        (WHITE_S, 'White (Scottish)'),
        (WHITE_W, 'White (Welsh)'),
    )
    ethnicity = models.IntegerField(choices=ETHNICITY, default=WHITE_S)
    first_name = models.CharField(max_length=100, default='')
    middle_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    known_as = models.CharField(max_length=100, default='')
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
       return self.first_name + " " + self.last_name

class Note(models.Model):
    note = models.CharField(max_length=100, default='')
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, editable=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)