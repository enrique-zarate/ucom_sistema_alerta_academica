import { IUserProfile, IStudent } from '@/interfaces';
import { AdminState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const mutations = {
    setUsers(state: AdminState, payload: IUserProfile[]) {
        state.users = payload;
    },
    setUser(state: AdminState, payload: IUserProfile) {
        const users = state.users.filter((user: IUserProfile) => user.id !== payload.id);
        users.push(payload);
        state.users = users;
    },
    setStudents(state: AdminState, payload: IStudent[]) {
        state.students = payload;
    },
    setStudent(state: AdminState, payload: IStudent) {
        const students = state.students.filter((student: IStudent) => student.id !== payload.id);
        students.push(payload);
        state.students = students;
    },
};

const { commit } = getStoreAccessors<AdminState, State>('');

export const commitSetUser = commit(mutations.setUser);
export const commitSetUsers = commit(mutations.setUsers);

export const commitSetStudent = commit(mutations.setStudent);
export const commitSetStudents = commit(mutations.setStudents);
