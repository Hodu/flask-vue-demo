<template>
  <el-row>
    <el-button @click="getUser()" plain>获取用户信息</el-button>
    <el-button @click="clear()" plain>清除</el-button>
  </el-row>
  <el-table
      :data="users"
      style="width: 100%">
      <el-table-column
        prop="user_id"
        label="id"
        width="180">
      </el-table-column>
      <el-table-column
        prop="username"
        label="姓名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="mobile"
        label="手机">
      </el-table-column>
      <el-table-column
        prop="create_time"
        label="创建时间">
      </el-table-column>
      <el-table-column
        prop="update_time"
        label="更新时间">
      </el-table-column>
    </el-table>
  </template>

<script>
  import { getUsers } from "../request/user"
  export default {
    name: "User",
    data() {
      return {
        users: [],
      }
    },
    methods: {
      getUser() {
        console.log("=========> getUser")
        let that = this
        getUsers().then(function (response) {
          console.log("======>", response)
          that.users = response;
        }).catch(function (exp) {
          console.log("========> e ", exp)
        })
      },
      clear() {
        this.users = [];
      }
    }
  }
</script>

<style>

</style>
