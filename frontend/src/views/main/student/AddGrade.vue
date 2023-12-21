<template>
    <div>
      <v-toolbar light>
        <v-toolbar-title>
          Add Grade for {{ student.full_name }}
        </v-toolbar-title>
      </v-toolbar>
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          v-model="grade"
          label="Grade"
          required
        ></v-text-field>
        <v-btn color="primary" @click="submit">Add Grade</v-btn>
      </v-form>
    </div>
  </template>
  
  <script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';
  import { dispatchAddGrade } from '@/store/admin/actions'; // Update this to your actual action
  
  @Component
  export default class AddGrade extends Vue {
    valid = true;
    student = {
        id: 0
      // Add other student properties as needed
    };
    grade = 0;

  
    created() {
      const id = this.$route.params.id;
      // Fetch the student data using the id
      this.student = {
        id: parseInt(id)
      };
    }
  
    submit() {
            if ((this.$refs.form as Vue & { validate: () => boolean }).validate()) {
            // Add the grade to the student
            dispatchAddGrade(this.$store, { studentId: this.student.id, grade: this.grade });
            this.$router.back();
        }
    }
  }
  </script>