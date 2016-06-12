from devotees_info.models import DevoteesServiceInfo, DevoteesSpiritualInfo, DevoteeParentInfo, DevoteesMaterialInfo, \
    DevoteesSpouseInfo, DevotessChildrenInfo
from collections import defaultdict
from pandas import DataFrame


def search_devotee(search_words):
    print search_words , "efreg"
    devotee_info = DevoteesMaterialInfo.objects.filter(phone_number=search_words)
    if not devotee_info:
        devotee_info = DevoteesMaterialInfo.objects.filter(name=search_words)
    print devotee_info
    if not devotee_info:
        devotee_info = DevoteesSpiritualInfo.objects.filter(spiritual_name=search_words)
    if not devotee_info:
        return None
    info_dict = {}
    info_frame = []
    for info in devotee_info[:1]:
        info_dict['name'] = info.name
        info_dict['phone_number'] = info.phone_number
        info_dict['current_address'] = info.current_address
    info_frame = DataFrame(data=[info_dict] ,index=False)
    return info_frame

