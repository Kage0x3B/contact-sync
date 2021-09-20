import { DAVAddressBook, DAVClient } from 'tsdav';
import { DAVVCard } from 'tsdav/dist/types/models';

export class CardDavImporter {
    private client?: DAVClient;

    constructor() {
    }

    public async connect(options: {
        serverUrl: string;
        credentials: {
            username: string;
            password: string;
        };
    }): Promise<void> {
        this.client = new DAVClient({
            ...options,
            authMethod: 'Basic',
            defaultAccountType: 'carddav'
        });

        await this.client.login();
    }

    public async fetchAddressBooks(): Promise<DAVAddressBook[]> {
        if (!this.client) {
            throw new Error('Connect to WebDav server first');
        }

        return await this.client.fetchAddressBooks();
    }

    public async fetchVCards(addressBook: DAVAddressBook): Promise<DAVVCard[]> {
        if (!this.client) {
            throw new Error('Connect to WebDav server first');
        }

        return await this.client.fetchVCards([{ addressBook }]);
    }
}
