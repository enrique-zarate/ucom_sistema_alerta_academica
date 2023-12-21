<template>
    <v-container fluid>
      <v-card class="ma-3 pa-3">
        <v-card-title primary-title>
          <div class="headline primary--text">Create Student</div>
        </v-card-title>
        <v-card-text>
          <template>
            <v-form v-model="valid" ref="form" lazy-validation>
              <v-text-field label="Full Name" v-model="fullName" required></v-text-field>
              <v-text-field label="E-mail" type="email" v-model="email" v-validate="'required|email'" data-vv-name="email" :error-messages="errors.collect('email')" required></v-text-field>
              <div class="subheading secondary--text text--lighten-2">Student is active <span v-if="isActive">(currently active)</span><span v-else>(currently not active)</span></div>
              <v-checkbox label="Is Active" v-model="isActive"></v-checkbox>
            </v-form>
          </template>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click="cancel">Cancel</v-btn>
          <v-btn @click="reset">Reset</v-btn>
          <v-btn @click="submit" :disabled="!valid">
                Save
              </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </template>
  
  <script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';
  import { IStudentCreate } from '@/interfaces'; // Update this to your actual interface
  import { dispatchGetStudents, dispatchCreateStudent } from '@/store/admin/actions'; // Update this to your actual actions
  
  @Component
  export default class CreateStudent extends Vue {
    public valid = false;
    public fullName: string = '';
    public email: string = '';
    public isActive: boolean = true;
  
    public async mounted() {
      await dispatchGetStudents(this.$store);
      this.reset();
    }
  
    public reset() {
      this.fullName = '';
      this.email = '';
      this.isActive = true;
      this.$validator.reset();
    }
  
    public cancel() {
      this.$router.back();
    }
  
    public async submit() {
      if (await this.$validator.validateAll()) {
        const newStudent: IStudentCreate = {
          full_name: this.fullName,
          email: this.email,
          is_active: this.isActive,
        };
        await dispatchCreateStudent(this.$store, newStudent);
        this.$router.push('/main/students');
      }
    }
  }
  </script>