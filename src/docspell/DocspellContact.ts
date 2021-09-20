import { vCard } from 'vcardz.ts';
import { ContactType } from './ContactType';

const contactTypeMap: { [key: string]: ContactType } = {
    text: ContactType.MOBILE,
    voice: ContactType.MOBILE,
    fax: ContactType.FAX,
    cell: ContactType.MOBILE,
    video: ContactType.PHONE,
    pager: ContactType.PHONE,
    textphone: ContactType.PHONE
};

export class DocspellContact {
    public id?: string;
    public name: string;
    public organization?: {
        id?: string;
        name: string;
    };
    public address: {
        street: string;
        zip: string;
        city: string;
        country: string;
    };
    public contacts: {
        id?: string;
        value: string;
        kind: ContactType;
    }[] = [];
    public notes: string = '';
    public use: 'correspondent' | 'concerning' | 'both' | 'disabled' = 'correspondent';
    public created?: Date;

    static fromVCard(data: vCard): DocspellContact {
        const contact = new DocspellContact();

        const category = data.CATEGORIES[0].value;
        let additionalInfo = '';
        let name = `${data.N?.first || ''} ${data.N?.last || ''}`.trim();
        const displayName = data.FN[0]?.value;

        // Additional info after the name for remembering the person with a detail or exact group, for example 'Some Person (10a)' for the exact school class
        if (name.indexOf('(') !== -1) {
            additionalInfo += name.substring(name.indexOf('(') + 1, name.lastIndexOf(')'));

            name = name.substring(0, name.indexOf('(')).trim();
        }
        if (displayName.indexOf('(') !== -1) {
            const displayNameInfo = displayName.substring(displayName.indexOf('(') + 1, displayName.lastIndexOf(')'));

            if (displayNameInfo.trim() !== additionalInfo.trim()) {
                additionalInfo += (additionalInfo ? ', ' : '') + displayNameInfo;
            }
        }

        if (data.TEL) {
            for (const contactData of data.TEL) {
                const telephoneNumber = contactData.value;
                const contactType = contactData.tag?.attr.TYPE ? contactData.tag?.attr.TYPE[0] : undefined;

                contact.contacts.push({
                    value: telephoneNumber,
                    kind: contactType ? contactTypeMap[contactType.toLowerCase()] : ContactType.MOBILE
                });
            }
        }

        if (data.EMAIL) {
            contact.contacts.push({
                value: data.EMAIL[0].value,
                kind: ContactType.EMAIL
            });
        }

        if (data.URL) {
            contact.contacts.push({
                value: data.URL[0].value,
                kind: ContactType.WEBSITE
            });
        }

        if (data.NOTE) {
            contact.notes += data.NOTE[0].value;
        }

        contact.name = name;
        contact.notes += (contact.notes ? '\n' : '') + `Kategorie: ${category}`;
        contact.notes += additionalInfo ? `, Info: ${additionalInfo}` : '';

        return contact;
    }
}
