import dotenv from 'dotenv';
import { getEnv, getEnvOptional } from './util/envUtil';

dotenv.config();

export default {
    isProduction: process.env.NODE_ENV === 'production',
    isTest: process.env.NODE_ENV === 'test',
    isDevelopment: process.env.NODE_ENV === 'development',
    cardDav: {
        serverUrl: getEnv('CARDDAV_HOST'),
        credentials: {
            username: getEnv('CARDDAV_USERNAME'),
            password: getEnv('CARDDAV_PASSWORD')
        },
        addressBook: getEnvOptional('CARDDAV_ADDRESS_BOOK')
    }
};
