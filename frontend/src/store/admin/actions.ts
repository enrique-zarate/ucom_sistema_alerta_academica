import { api } from '@/api';
import { ActionContext } from 'vuex';
import { IUserProfileCreate, IUserProfileUpdate } from '@/interfaces';
import { State } from '../state';
import { AdminState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { commitSetUsers, commitSetUser, commitSetStudents, commitSetStudent } from './mutations';
import { dispatchCheckApiError } from '../main/actions';
import { commitAddNotification, commitRemoveNotification } from '../main/mutations';

type MainContext = ActionContext<AdminState, State>;

export const actions = {
    // Users.
    async actionGetUsers(context: MainContext) {
        try {
            const response = await api.getUsers(context.rootState.main.token);
            if (response) {
                console.log('Before mutation, users:', context.state.users);
                commitSetUsers(context, response.data);
                console.log('After mutation, users:', context.state.users);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateUser(context: MainContext, payload: { id: number, user: IUserProfileUpdate }) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateUser(context.rootState.main.token, payload.id, payload.user),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetUser(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'User successfully updated', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionCreateUser(context: MainContext, payload: IUserProfileCreate) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createUser(context.rootState.main.token, payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetUser(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'User successfully created', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },

    // Students.
    async actionGetStudents(context: MainContext) {
        try {
            const response = await api.getStudents();
            if (response) {
                console.log('Before mutation, students:', context.state.students);
                commitSetStudents(context, response.data);
                console.log('After mutation, students:', context.state.students);
            }
            else {
                console.log('No fetched students');
            }
        } catch (error) {
            console.log('Error fetching students:', error);
            await dispatchCheckApiError(context, error);
        }
    },

    async actionUpdateStudent(context: MainContext, payload: { id: number, user: IUserProfileUpdate }) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateStudent(context.rootState.main.token, payload.id, payload.user),
                await new Promise<void>((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetStudent(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Student successfully updated', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },

    async actionCreateStudent(context: MainContext, payload: IUserProfileCreate) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createStudent(context.rootState.main.token, payload),
                await new Promise<void>((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetUser(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Student successfully created', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },

    async actionAddGrade(context: MainContext, payload: { studentId: number, grade: number }) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.addGrade( payload.studentId, payload.grade),
                await new Promise<void>((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetStudent(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Grade successfully added', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },

};


const { dispatch } = getStoreAccessors<AdminState, State>('');

// Users.
export const dispatchCreateUser = dispatch(actions.actionCreateUser);
export const dispatchGetUsers = dispatch(actions.actionGetUsers);
export const dispatchUpdateUser = dispatch(actions.actionUpdateUser);
// Students.
export const dispatchGetStudents = dispatch(actions.actionGetStudents);
export const dispatchUpdateStudent = dispatch(actions.actionUpdateStudent);
export const dispatchCreateStudent = dispatch(actions.actionCreateStudent);
// Grades.
export const dispatchAddGrade = dispatch(actions.actionAddGrade);
