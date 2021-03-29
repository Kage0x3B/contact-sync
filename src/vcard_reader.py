import os
import vobject

CONTACT_INFO_TYPE_MAP = {
    "mobile": "Mobile",
    "home": "Phone",
    "work": "Phone",
    "fax": "Fax",
    "email": "Email",
    "website": "Website"
}


class ContactData:
    def __init__(self, uid, name, categories):
        self.uid = uid
        self.name = name
        self.categories = categories


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

    fn_amount = 0
    n_amount = 0
    for file_name in os.listdir(vcard_path):
        # print("Reading " + file_name)
        file_path = os.path.join(vcard_path, file_name)

        with open(file_path) as file:
            vcard_string = file.read()
            vcard_data: vobject.base.Component = vobject.readOne(vcard_string)
            # vcard_data.prettyPrint()

            uid = "0"
            name = ""
            categories = ['uncategorized']

            if "fn" in vcard_data.contents:
                name = vcard_data.fn.value
            else:
                print("Contact " + file_name + " has no name")
                vcard_data.prettyPrint()
                continue

            if "categories" in vcard_data.contents:
                categories = vcard_data.categories.value

            contact_list.append(ContactData(uid, name, categories))

    print("fn_amount:" + str(fn_amount))
    print("n_amount:" + str(n_amount))

    return contact_list
