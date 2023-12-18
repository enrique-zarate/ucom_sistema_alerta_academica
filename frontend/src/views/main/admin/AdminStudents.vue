<template>
    <div>
      <v-data-table :headers="headers" :items="students">
        <template v-slot:item="{ props }">
          <td>{{ props.item.email }}</td>
          <td>{{ props.item.full_name }}</td>
          <!-- Add more columns as needed -->
        </template>
      </v-data-table>
    </div>
  </template>
  
  <script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';
  // import { IStudentProfile } from '@/interfaces'; // Update this to your actual Student interface
  import { readAdminStudents } from '@/store/admin/getters'; // Update this to your actual getter
  import { dispatchGetStudents } from '@/store/admin/actions'; // Update this to your actual action
  
  @Component
  export default class AdminStudents extends Vue {
    public headers = [
      {
        text: 'Email',
        sortable: true,
        value: 'email',
        align: 'left',
      },
      {
        text: 'Nombre completo',
        sortable: true,
        value: 'full_name',
        align: 'left',
      },
      {
        text: 'Está activo',
        sortable: true,
        value: 'isActive',
        align: 'left',
      },
    ];
  
    // get user is used to get the user from the store
    get students() {
      return readAdminStudents(this.$store);
    }

    // mounted is used to dispatch the action to get the students
    public async mounted() {
      dispatchGetStudents(this.$store);
    }
    
  }
  </script>