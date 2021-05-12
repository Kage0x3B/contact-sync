import os
from dotenv import load_dotenv
from carddav_importer import CardDavImporter
from docspell_api import DocspellApi
import vcard_reader
from src import docspell_api


def main():
    load_dotenv()

    carddav_importer = CardDavImporter(os.getenv("WEBDAV_HOST"), os.getenv("WEBDAV_LOGIN"),
                                       os.getenv("WEBDAV_PASSWORD"), os.getenv("CARDDAV_PATH"))

    carddav_importer.connect()
    # TODO For testing only, downloading all takes pretty long
    # carddav_importer.download_contacts()
    vcard_reader.load_from_temp()

    # docspell = DocspellApi(os.getenv("DOCSPELL_HOST"))
    # docspell.authenticate(os.getenv("DOCSPELL_USERNAME"), os.getenv("DOCSPELL_PASSWORD"))

    print("categories:", vcard_reader.list_category_names())


if __name__ == "__main__":
    main()
