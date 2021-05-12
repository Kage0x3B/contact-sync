import os
import vobject
from contact_data import normalize_vcard_contact

CONTACT_INFO_TYPE_MAP = {
    "mobile": "Mobile",
    "home": "Phone",
    "work": "Phone",
    "fax": "Fax",
    "email": "Email",
    "website": "Website"
}


class ContactInformation:
    def __init__(self):
        pass


def list_category_names():
    category_name_list = []

    contact_list = load_from_temp()

    for contact_data in contact_list:
        for category in contact_data.categories:
            category_name_list.append(category)

    return list(set(category_name_list))


def load_from_temp():
    vcard_path = os.getcwd() + "/tmp"

    contact_list = []

    for file_name in os.listdir(vcard_path):
        file_path = os.path.join(vcard_path, file_name)

        with open(file_path) as file:
            vcard_string = file.read()
            vcard_data: vobject.base.Component = vobject.readOne(vcard_string)

            try:
                contact = normalize_vcard_contact(vcard_data)

                contact_list.append(contact)
            except Exception:
                print("Contact " + file_name + " could not be parsed")

    print("fn_amount:" + str(fn_amount))
    print("n_amount:" + str(n_amount))

    return contact_list
