import { CardDavImporter } from './vcard/CardDavImporter';
import config from './config';
import { VCardImporter } from './vcard/VCardImporter';

async function main() {
    const cardDavImporter = new CardDavImporter();
    await cardDavImporter.connect(config.cardDav);

    const addressBooks = await cardDavImporter.fetchAddressBooks();

    if (!config.cardDav.addressBook) {
        console.info('No address book name given!');
        console.info(
            `Available address books on ${config.cardDav.serverUrl} with user ${config.cardDav.credentials.username}:`
        );

        addressBooks.forEach((ab) => console.info(` - ${ab.displayName}`));

        return;
    }

    const addressBook = addressBooks.find(
        (ab) => ab.displayName?.toLowerCase() === config.cardDav.addressBook?.toLowerCase()
    );

    if (!addressBook) {
        throw new Error(`No address book found with display name matching ${config.cardDav.addressBook}`);
    }

    const vcardImporter = new VCardImporter();
    vcardImporter.readVCards(await cardDavImporter.fetchVCards(addressBook));
}

main();
