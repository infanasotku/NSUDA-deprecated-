export interface NavigationContent {
    link: string,
    content: string,
    id: number
}

export type Action = () => void;

export enum AuthType {
    NoAuth,
    Google
}

export interface UserBaseModel {
    name: string,
    surname: string,
    email: string,
    picture_uri: string
}

export class UserOIDCModel implements UserBaseModel {
    name: string;
    surname: string;
    email: string;
    picture_uri: string;

    constructor(name?: string, surname?: string, 
        email?: string, picture_uri?: string) {
        this.name = name ?? ''
        this.surname = surname ?? ''
        this.email = email ?? ''
        this.picture_uri = picture_uri ?? ''
    }
}