import { AdminState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    // Users.
    adminUsers: (state: AdminState) => state.users,
    adminOneUser: (state: AdminState) => (userId: number) => {
        const filteredUsers = state.users.filter((user) => user.id === userId);
        if (filteredUsers.length > 0) {
            return { ...filteredUsers[0] };
        }
    },
    // Students.
    adminStudents: (state: AdminState) => state.students,
    adminOneStudent: (state: AdminState) => (studentId: number) => {
        const filteredStudents = state.students.filter((student) => student.id === studentId);
        if (filteredStudents.length > 0) {
            return { ...filteredStudents[0] };
        }
    }
};

const { read } = getStoreAccessors<AdminState, State>('');

// Users.
export const readAdminUsers = read(getters.adminUsers);
export const readAdminOneUser = read(getters.adminOneUser);
// Students.
export const readAdminStudents = read(getters.adminStudents);
export const readAdminOneStudent = read(getters.adminOneStudent);