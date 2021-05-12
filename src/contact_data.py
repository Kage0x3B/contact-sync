import vobject
from util import normalize_string


class ContactData:
    def __init__(self, uid, name, categories):
        self.uid = uid
        self.name = name
        self.categories = categories


def normalize_vcard_contact(vcard_data: vobject.base.Component) -> ContactData:
    uid = "0"
    categories = ['uncategorized']

    if "fn" in vcard_data.contents:
        name = normalize_string(vcard_data.fn.value)
    else:
        raise RuntimeError("Contact has no name")

    if "categories" in vcard_data.contents:
        categories = vcard_data.categories.value

    contact = ContactData(uid, name, categories)

    return contact
