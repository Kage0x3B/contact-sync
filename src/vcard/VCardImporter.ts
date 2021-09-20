import { DAVVCard } from 'tsdav/dist/types/models';
import { vCardReader } from 'vcardz.ts';
import { DocspellContact } from '../docspell/DocspellContact';

class VCard {
    constructor(public id: string, public data: any) {}
}

export class VCardImporter {
    private vcards: VCard[] = [];

    public readVCards(davVCards: DAVVCard[]): void {
        let i = 0;
        for (const vCard of davVCards) {
            const vCardData = vCardReader.fromString((vCard.data as string).split('\n'));

            if (!vCardData.CATEGORIES || !vCardData.CATEGORIES.length) {
                continue;
            }

            const contactData = DocspellContact.fromVCard(vCardData);
            console.log(vCardData);
            console.log(contactData);
            if (i > 10) break;
            i++;
        }
    }
}
