import {join} from 'path';

export function getEnv(key: string): string {
    if (typeof process.env[key] === 'undefined') {
        throw new Error(`Environment variable ${key} is not set.`);
    }

    return process.env[key] as string;
}

export function getEnvOptional(key: string): string | undefined {
    return process.env[key];
}

function getPath(path: string): string {
    return join(process.cwd(), path);
}

function getPaths(paths: string[]): string[] {
    return paths.map(getPath);
}

export function getEnvPath(key: string): string {
    return getPath(getEnv(key));
}

export function toNumber(value: string): number {
    return parseInt(value, 10);
}

export function toBool(value: string): boolean {
    return value === 'true';
}
