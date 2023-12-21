<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Administrar alumnos
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/students/create">Crear usuario</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="students">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.id }}</td>
        <td>{{ props.item.email }}</td>
        <td>{{ props.item.full_name }}</td>
        <td><v-icon v-if="props.item.is_active">checkmark</v-icon></td>
        <!-- Add prop for Roles -->
        <td>{{ props.item.roles }}</td>
        <td class="justify-center layout px-0">
          <v-tooltip top>
            <span>Add Grade</span>
            <v-btn slot="activator" flat :to="{name: 'main-students-add-grade', params: {id: props.item.id}}">
              <v-icon>add</v-icon>
            </v-btn>
          </v-tooltip>
          <v-tooltip top>
            <span>Edit</span>
            <v-btn slot="activator" flat :to="{name: 'main-students-edit', params: {id: props.item.id}}">
              <v-icon>edit</v-icon>
            </v-btn>
          </v-tooltip>
        </td>
      </template>
    </v-data-table>
  </div>
</template>
  
<script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';
  // import { IStudentProfile } from '@/interfaces'; // Update this to your actual Student interface
  import { readAdminStudents } from '@/store/admin/getters';
  import { dispatchGetStudents } from '@/store/admin/actions'; // Update this to your actual action
  
  @Component
  export default class AdminStudents extends Vue {
    public headers = [
      { text: 'ID', value: 'id' },
      { text: 'Nombre', value: 'full_name' },
      { text: 'Email', value: 'email' },
      { text: 'Activo', value: '  ' },
    ]
  
    
    // get user is used to get the user from the store
    get students() {
      console.log('AdminStudents.vue 1');
      return readAdminStudents(this.$store);
    }
    
    // mounted is used to dispatch the action to get the students
    public async mounted() {
      console.log('AdminStudents.vue 2');
      dispatchGetStudents(this.$store);
    }
    
  }
  </script>