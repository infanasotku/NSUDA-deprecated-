export interface NavigationContent
{
    link: string,
    content: string,
    id: number
}

export type Action = () => void;

export enum FormType {
    SignIn,
    SignUp
}

export interface UserAuthData 
{
    login: string,
    password: string
}