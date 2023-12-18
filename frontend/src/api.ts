import axios from 'axios';
import { apiUrl } from '@/env';
import { IUserProfile, IUserProfileUpdate, IUserProfileCreate, IStudent, IStudentCreate, IStudentUpdate } from './interfaces';

function authHeaders(token: string) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

export const api = {
  async logInGetToken(username: string, password: string) {
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);

    return axios.post(`${apiUrl}/api/v1/login/access-token`, params);
  },
  async getMe(token: string) {
    return axios.get<IUserProfile>(`${apiUrl}/api/v1/users/me`, authHeaders(token));
  },
  async updateMe(token: string, data: IUserProfileUpdate) {
    return axios.put<IUserProfile>(`${apiUrl}/api/v1/users/me`, data, authHeaders(token));
  },
  // Users.
  async getUsers(token: string) {
    return axios.get<IUserProfile[]>(`${apiUrl}/api/v1/users/`, authHeaders(token));
  },
  async updateUser(token: string, userId: number, data: IUserProfileUpdate) {
    return axios.put(`${apiUrl}/api/v1/users/${userId}`, data, authHeaders(token));
  },
  async createUser(token: string, data: IUserProfileCreate) {
    return axios.post(`${apiUrl}/api/v1/users/`, data, authHeaders(token));
  },

  // Students.
  // getStudents: gets all students from /api/v1/students/
  async getStudents(token: string) {
    return axios.get<IStudent[]>(`${apiUrl}/api/v1/students/`, authHeaders(token));
  },
  // updateStudent: updates a student from /api/v1/students/:studentId
  async updateStudent(token: string, studentId: number, data: IStudentUpdate) {
    return axios.put(`${apiUrl}/api/v1/students/${studentId}`, data, authHeaders(token));
  },
  // createStudent: creates a student from /api/v1/students/
  async createStudent(token: string, data: IStudentCreate) {
    return axios.post(`${apiUrl}/api/v1/students/`, data, authHeaders(token));
  },


  // Password recovery.
  async passwordRecovery(email: string) {
    return axios.post(`${apiUrl}/api/v1/password-recovery/${email}`);
  },
  async resetPassword(password: string, token: string) {
    return axios.post(`${apiUrl}/api/v1/reset-password/`, {
      new_password: password,
      token,
    });
  },
};
