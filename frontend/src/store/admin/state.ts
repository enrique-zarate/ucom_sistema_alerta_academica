import { IUserProfile } from '@/interfaces';
import { IStudent } from '@/interfaces';

export interface AdminState {
    users: IUserProfile[];
    students: IStudent[];
}
