from django.contrib import admin
from Pathology.models import *

admin.site.register(Patient_Details)
admin.site.register(Image_Input)
admin.site.register(Lab_Api)
admin.site.register(Scripts)
admin.site.register(Lab_Api_Scripts)
admin.site.register(Lab_Api_On_Image_Input)
admin.site.register(AI_Usecase_Occurences)
admin.site.register(Location)
admin.site.register(Test_Pathology)
admin.site.register(Reports)
# admin.site.register(B_Test)
# admin.site.register(U_Test)
admin.site.register(Test)
#admin.site.register(Name)

