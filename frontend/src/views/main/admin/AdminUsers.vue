<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Administrar usuarios
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/users/create">Crear usuario</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="users">
      <template slot="items" slot-scope="props">
        <!-- <td>{{ props.item.name }}</td> -->
        <td>{{ props.item.email }}</td>
        <td>{{ props.item.full_name }}</td>
        <td><v-icon v-if="props.item.is_active">checkmark</v-icon></td>
        <td><v-icon v-if="props.item.is_superuser">checkmark</v-icon></td>
        <!-- Add prop for Roles -->
        <td>{{ props.item.roles }}</td>
        <td class="justify-center layout px-0">
          <v-tooltip top>
            <span>Edit</span>
            <v-btn slot="activator" flat :to="{name: 'main-admin-users-edit', params: {id: props.item.id}}">
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
import { Store } from 'vuex';
import { IUserProfile } from '@/interfaces';
import { readAdminUsers } from '@/store/admin/getters';
import { dispatchGetUsers } from '@/store/admin/actions';

@Component
export default class AdminUsers extends Vue {
  public headers = [
    // {
    //   text: 'Name',
    //   sortable: true,
    //   value: 'name',
    //   align: 'left',
    // },
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
    {
      text: 'Es superusuario',
      sortable: true,
      value: 'isSuperuser',
      align: 'left',
    },
    {
      text: 'Roles',
      value: 'roles'
    },
    {
      text: 'Acciones',
      value: 'id',
    },
  ];
  get users() {
    return readAdminUsers(this.$store);
  }

  public async mounted() {
    await dispatchGetUsers(this.$store);
  }
}
</script>
