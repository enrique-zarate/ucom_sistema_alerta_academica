// Purpose: export all interfaces from one place


/*
User profile interface.
*/

export interface IUserProfile {
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    full_name: string;
    id: number;
}

export interface IUserProfileUpdate {
    email?: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}


/*
Student  interface.
*/

export interface IStudent {
    email: string;
    is_active: boolean;
    full_name: string;
    id: number;
}

export interface IStudentUpdate {
    email?: string;
    full_name?: string;
    is_active?: boolean;
}

export interface IStudentCreate {
    email: string;
    full_name?: string;
    is_active?: boolean;
}
