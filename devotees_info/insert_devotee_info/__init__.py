from devotees_info.models import DevoteesServiceInfo, DevoteesSpiritualInfo, DevoteeParentInfo, DevoteesMaterialInfo, \
    DevoteesSpouseInfo, DevotessChildrenInfo


def insert_devotee_info_into_db(devotee_info_dict):
    devotee_material_info_obj = DevoteesMaterialInfo(name=devotee_info_dict['devotee_name'],
                                                     email=devotee_info_dict['email'],
                                                     date_of_birth=devotee_info_dict['date_of_birth'],
                                                     phone_number=devotee_info_dict['phone_number'],
                                                     Profession=devotee_info_dict['profession'],
                                                     current_address=devotee_info_dict['current_address'])
    devotee_material_info_obj.save()
    devotee_spiritual_info_obj = DevoteesSpiritualInfo(devotee=devotee_material_info_obj,
                                                       spiritual_name=devotee_info_dict['spiritual_name'],
                                                       diksha_guru=devotee_info_dict['diksha_guru'],
                                                       chanting_rounds=devotee_info_dict['chanting_rounds'],
                                                       shiksha_guru=devotee_info_dict['shiksha_guru'],
                                                       life_member=devotee_info_dict['life_member'])
    devotee_spiritual_info_obj.save()
    devotee_service_info = DevoteesServiceInfo(devotee=devotee_material_info_obj,
                                               services=devotee_info_dict['services'])
    devotee_service_info.save()
    devotee_parent_info = DevoteeParentInfo(devotee=devotee_material_info_obj,
                                            father_name=devotee_info_dict['father_name'],
                                            mother_name=devotee_info_dict['mother_name'])
    devotee_parent_info.save()
    devotee_spouse_info = DevoteesSpouseInfo(devotee=devotee_material_info_obj, name=devotee_info_dict['spouse_name'],
                                             Profession=devotee_info_dict['spouse_profession'], )
    devotee_spouse_info.save()
    devotee_children_info = DevotessChildrenInfo(devotee=devotee_material_info_obj,
                                                 name=devotee_info_dict['children_name'])
    devotee_children_info.save()


