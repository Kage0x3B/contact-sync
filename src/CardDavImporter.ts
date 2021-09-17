import {createDAVClient, DAVClient} from "tsdav";

export class CardDavImporter {
    private client: any;

    constructor() {
    }

    public async connect(options: {
        serverUrl: string;
        credentials: {
            username: string;
            password: string;
        }
    }): Promise<void> {
        const client = new DAVClient({
            ...options,
            authMethod: 'Basic',
            defaultAccountType: 'carddav'
        });

        await client.login();

        const calendars = await client.fetchCalendars();

        const calendarObjects = await client.fetchCalendarObjects({
            calendar: calendars[0],
        });
    }
}
