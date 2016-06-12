from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from devotees_info.insert_devotee_info import insert_devotee_info_into_db
from dateutil.parser import parse
from devotees_info.search_devotee_info import search_devotee


# Create your views here.

@csrf_exempt
def devotee_info(request):
    return render_to_response('devotee_info_form.html')


@csrf_exempt
def store_devotee_info(request):
    devotee_info_dict = {}
    devotee_info_dict['devotee_name'] = request.POST['devotee_name']
    devotee_info_dict['date_of_birth'] = request.POST['date_of_birth']
    devotee_info_dict['email'] = request.POST['email']
    devotee_info_dict['phone_number'] = request.POST['phone_number']
    devotee_info_dict['current_address'] = request.POST['current_address']
    devotee_info_dict['profession'] = request.POST['profession']
    devotee_info_dict['spiritual_name'] = request.POST['spiritual_name']
    devotee_info_dict['diksha_guru'] = request.POST['diksha_guru']
    devotee_info_dict['services'] = request.POST['services']
    devotee_info_dict['chanting_rounds'] = request.POST['chanting_rounds']
    devotee_info_dict['shiksha_guru'] = request.POST['shiksha_guru']
    devotee_info_dict['life_member'] = request.POST['life_member']
    devotee_info_dict['father_name'] = request.POST['father_name']
    devotee_info_dict['mother_name'] = request.POST['mother_name']
    devotee_info_dict['father_services'] = request.POST['father_services']
    devotee_info_dict['mother_service'] = request.POST['mother_service']
    devotee_info_dict['spouse_name'] = request.POST['spouse_name']
    devotee_info_dict['spouse_spiritual_name'] = request.POST['spouse_spiritual_name']
    devotee_info_dict['spouse_profession'] = request.POST['spouse_profession']
    devotee_info_dict['children_name'] = request.POST['children_name']
    devotee_info_dict['spouse_service_info'] = request.POST['spouse_service_info']
    insert_devotee_info_into_db(devotee_info_dict)
    return HttpResponse("Thanks")


@csrf_exempt
def search_devotee_info(request):
    search_keywords = request.GET.get('search_keywords')
    print search_keywords
    devotee_info = search_devotee(search_keywords)
    if devotee_info is None:
        devotee_info = ""
    return render_to_response('devotee_info_search_form.html',{'devotee_info':devotee_info})
