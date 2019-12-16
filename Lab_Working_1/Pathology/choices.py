# from .models import *
# from Pathology.models import xray


# def get_xray():
#     all_test = xray.objects.all()
#     length = len(all_test)
#     while length > 1:
#         for i in range(1, length + 1):
#             b = (
#                 (i, xray.objects.filter(id=i))
#             )
#     return b


# def get_blood():
#     all_test = B_Test.objects.all()
#     length = len(all_test)
#     while length > 1:
#         for i in range(1, length + 1):
#             b = (
#                 (i, B_Test.objects.filter(id=i))
#             )
#     return b

# def get_urine_test():
#     all_test = U_Test.objects.all()
#     length = len(all_test)
#     while length > 1:
#         for i in range(1, length + 1):
#             b = (
#                 (i, U_Test.objects.filter(id=i))
#             )
#     return b




GENDER_CHOICES = (('MALE', 'MALE'),
                  ('FEMALE', 'FEMALE'))

Blood_Test = (

    ('FBC blood test', 'FBC blood test'),
    ('UE blood test', 'UE blood test'),
    ('GFR blood test', 'GFR blood test'),
    ('LFT blood test', 'LFT blood test'),
    ('Blood sugar (glucose) level', 'Blood sugar (glucose) level'),
    ('HbA1c blood test', 'HbA1c blood test'),
    ('GTT', 'GTT'),
    ('Blood clotting tests', 'Blood clotting tests'),
    ('Tests for inflammation', 'Tests for inflammation'),
    ('Blood cholesterol level', 'Blood cholesterol level'),
    ('Immunology', 'Immunology'),
    ('Blood grouping', 'Blood grouping'),
    ('TSH blood test', 'TSH blood test'),
    ('Ca 125 blood test', 'Ca 125 blood test'),
    ('PSA blood test', 'PSA blood test'),
    ('BNP blood test', 'BNP blood test'),
    ('ANA blood test', 'ANA blood test'),
    ('MCH blood test', 'MCH blood test'),
    ('MCV blood test', 'MCV blood test'),
    ('INR blood test', 'INR blood test'),
    ('CK blood test', 'CK blood test'),
    ('B12 blood test', 'B12 blood test'),
    ('FSH blood test', 'FSH blood test'),
    ('CEA blood test', 'CEA blood test'),
    ('LDH blood test', 'LDH blood test'),
)

Urine_Test = (
    ('Dipstick Urine Test', 'Dipstick Urine Test'),
    ('Urine albumin-to-creatinine ratio(UACR)', 'Urine albumin-to-creatinine ratio(UACR)'),
    ('Urine Pregnancy Test', 'Urine Pregnancy Test'),
    ('Urinary Drug Test', 'Urinary Drug Test'),
    ('Urine Tests for Sexsually Transmitted Infections', 'Urine Tests for Sexsually Transmitted Infections'),
)

XRAY = (
    ('Pneumonia X-rays', 'Pneumonia X-rays'),
    ('Standard Computed Tomography', 'Standard Computed Tomography'),
    ('Chest X-rays', 'Chest X-rays'),
    ('Lungs X-rays', 'Lungs X-rays'),
    ('Abdomen X-rays', 'Abdomen X-rays'),

)

MRI = (
    ('Magnetic Resonance Venography(MRV)', 'Magnetic Resonance Venography(MRV)'),
    ('Magnetic Resonance Aniography(MRA)', 'Magnetic Resonance Aniography(MRA)'),
    ('Functional MRI(fMRI)', 'Functional MRI(fMRI)'),
    ('Cardiac MRI', 'Cardiac MRI'),
    ('Breast Scans', 'Breast Scans'),
    ('MRI of Brain', 'MRI of Brain'),
    ('Magnetic Resonance Neurography(MRN)', 'Magnetic Resonance Neurography(MRN)'),
)

CT_SCANS = (
    ('CT SCAN ABDOMEN', 'CT SCAN ABDOMEN'),
    ('CT ANGIOGRAPHY', 'CT ANGIOGRAPHY'),
    ('CT SCAN ARTHROGRAPHY', 'CT SCAN ARTHROGRAPHY'),
    ('CT SCAN BONES', 'CT SCAN BONES'),
    ('CT SCAN BRAIN', 'CT SCAN BRAIN'),
    ('CT SCAN CHEST', 'CT SCAN CHEST'),
    ('CT SCAN NECK', 'CT SCAN NECK'),
    ('CT SCAN PELVIS', 'CT SCAN PELVIS'),
    ('CT SCAN RENAL STONES', 'CT SCAN RENAL STONES'),
    ('CT SCAN SINUS', 'CT SCAN SINUS'),
    ('CT SCAN SPINE', 'CT SCAN SPINE'),

)
