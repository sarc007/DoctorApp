import datetime
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from Pathology.GetValueFromPowerAI import *
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Pathology.forms import *


def home(request):
    return render(request, 'Home.html')


def about_us(request):
    return render(request, 'About_Us.html')


def contact_us(request):
    return render(request, 'Contact_Us.html')


def test_in_pathology(request):
    test_list = []
    patient_name = ''
    global len_value
    global value
    if request.method == 'POST':
        print('in post')
        value = request.POST.getlist('test')
        len_value = len(value)
        print(len_value)
        print(value)
        return HttpResponseRedirect('/image_upload/')

    else:
        tests = Test_Pathology.objects.all()
        for test in tests:
            test_list.append(test)
        patients = Patient_Details.objects.all()
        length = len(patients) - 1
        print(length)
        patient_name = patients[length]
        print(patient_name)

    return render(request, 'test_in_pathology.html', {'tests': test_list, 'patient_name': patient_name})


def report_view(request):
    test_list = []
    # if request.method == 'POST':
    # form = Reports_Form(request.POST)
    # if form.is_valid():
    #     form.save()
    location = Location.objects.all()
    loc_length = len(location) - 1
    l1 = location[loc_length]

    # Patient = Patient_Details.objects.all()
    # p_length = len(Patient) - 1
    # p1 = Patient[p_length]

    results = AI_Usecase_Occurences.objects.all().values_list('Image_Output_1', flat=True)
    conf = AI_Usecase_Occurences.objects.all().values_list('confidence', flat=True)
    heatmap = AI_Usecase_Occurences.objects.all().values_list('heatmap', flat=True)
    results_list = list(results)
    conf_list = list(conf)
    heat_list = list(heatmap)
    # len_results_list = len(results_list)

    value

    for i in value:
        print(i)

    newlist = results_list[-len_value:]
    confList = conf_list[-len_value:]
    heatList = heat_list[-len_value:]

    # for n in newlist:
    #     print(n)

    #     return HttpResponseRedirect('/final_report/')
    # else:
    tests = Test_Pathology.objects.all()
    for test in tests:
        test_list.append(test)
    patients = Patient_Details.objects.all()
    length = len(patients) - 1
    print(length)
    patient_name = patients[length]
    print(patient_name)

    # form = Reports_Form()

    # return render(request, 'report.html', {'form': form})
    return render(request, 'report.html',
                  {'heatList': heatList, 'confList': confList, 'newlist': newlist, 'value': value, 'patient_name': patient_name,
                   'Location': l1})  # {'Location': l1, 'Patient':p1}   #, 'tests': test_list,


def image_upload_view(request):
    test_list = []
    if request.method == 'POST':
        form = Image_Input_Forms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            global url
            value
            for val in value:
                test = Test_Pathology.objects.get(some_test='{0}'.format(val))
                url = test.api_url
                # print(test)
                # print(url)
                length = len(Image_Input.objects.all())
                image = Image_Input.objects.filter(id=length)
                for img in image:
                    img = str(img)
                    sli = slice(16, -1)
                    img = img[sli] + "g"
                    # filename = '/home/kernel/Lab_Working_1/media/Patient_reports/' + img
                    import os
                cwd = '/home/kernel/shazan/11dec2019/Lab_Working_1/media/Patient_reports/'
                filename = cwd + img
                # 'E:\Lab_Working_1\media\Patient_reports\' + img
                output = detect_image_label(filename, url)
                print('new', output)
                conf = str(output[2])
                # Reports.objects.create(location_id=1, patient_details_id='1', image_output=output[1], description='report_description', test_id=1)

                # / home / kernel / shazan / 11
                # dec2019 / Lab_Working_1 / Pathology / static / heatmap

                import urllib.request
                urllib.request.urlretrieve(output[3], "/home/kernel/shazan/11dec2019/Lab_Working_1/Pathology/static/heatmap/heatmap.png")

                AI_Usecase_Occurences.objects.create(time=datetime.now(), Image_Output_1=output[1], confidence=conf,
                                                     heatmap="/home/kernel/shazan/11dec2019/Lab_Working_1/Pathology/static/heatmap/heatmap.png")
            return redirect('/report/')
    else:
        tests = Test_Pathology.objects.all()
        for test in tests:
            test_list.append(test)
        patients = Patient_Details.objects.all()
        length = len(patients) - 1
        print(length)
        patient_name = patients[length]
        print(patient_name)
        form = Image_Input_Forms()

    return render(request, 'Image_Upload.html', {'form': form, 'patient_name': patient_name})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def patient_details_view(request):
    if request.method == 'POST':
        form = Patient_Details_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/test/')
    else:
        form = Patient_Details_Form()

    return render(request, 'patient_details.html', {'form': form})


def final_reports_view(request):
    # patient = Patient_Details.objects.all()
    # reports = Reports.objects.all()
    # length_report = len(reports) - 1
    # length_patient = len(patient) - 1
    # patient_name = patient[length_patient]
    # print(patient_name)
    # print('------------------------------------------')
    # print(reports[length_report])
    # context = {
    #     'reports': reports[length_report],
    #     'patient': patient_name
    # }
    return render(request, 'final_report_view.js')


def location_view(request):
    if request.method == 'POST':
        form = Location_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/report/')
    else:
        form = Location_Form()

    return render(request, 'location.html', {'form': form})


def test_view(request):
    if request.method == 'POST':
        form = Test_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/test/')
    else:
        form = Test_Form()
    return render(request, 'test.html', {'form': form})

# def blood_test_view(request):
#     if request.method == 'POST':
#         form = Blood_Test_Form(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/test/')
#     else:
#         form = Blood_Test_Form()
#     return render(request, 'blood_test_view.html', {'form': form})
#
#
# def urine_test_view(request):
#     if request.method == 'POST':
#         form = Urine_Test_Form(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/test/')
#     else:
#         form = Urine_Test_Form()
#     return render(request, 'urine_test_view.html', {'form': form})

# def Image_upload_view(request):
#     # print(test_name)
#     if request.method == 'POST':
#         form = Image_Input_Forms(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             length = len(Image_Input.objects.all())
#             image = Image_Input.objects.filter(id=length)
#             for img in image:
#                 img = str(img)
#                 sli = slice(16, -1)
#                 img = img[sli] + "g"
#             filename = '/home/siraj/Lab/media/Patient_reports/' + img
#             output = detect_image_label(filename)
#             Reports.objects.create(location_id=1, patient_details_id='1', image_output=output[1], description='report_description', test_id=1)
#             AI_Usecase_Occurences.objects.create(time=datetime.now(), Image_Output_1=output[0] + "-" + output[1])
#             return redirect('/report/')
#     else:
#         form = Image_Input_Forms()
#
#     return render(request, 'Image_Upload.html', {'form': form})


# def new_view(request):
#     test_f = Test.objects.all()
#     length_test= len(test_f)
#     latest_test = length_test - 1
#     b = test_f[latest_test]
#     return b(

# def new_view(request):
#     script = Lab_Api.objects.get
#     if request.method == 'POST':
#         form = Image_Input_Forms(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             length = len(Image_Input.objects.all())
#             image = Image_Input.objects.filter(id=length)
#             for img in image:
#                 img = str(img)
#                 sli = slice(16, -1)
#                 img = img[sli] + "g"
#                 filename = '/home/siraj/Lab/media/Patient_reports/' + img
#                 output = detect_image_label(filename, test_link)
#                 # Reports.objects.create(location_id=1, patient_details_id='1', image_output=output[1], description='report_description', test_id=1)
#                 AI_Usecase_Occurences.objects.create(time=datetime.now(), Image_Output_1=output[0] + "-" + output[1])
#                 return redirect('/report/')
#         else:
#             form = Image_Input_Forms()
#
#         return render(request, 'Image_Upload.html', { 'form': form })
# conn = Lab_Api.objects.all()
# return str(conn)
