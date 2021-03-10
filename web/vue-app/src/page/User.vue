<template>
  <div>
  <el-row>
    <el-button @click="getUser()" plain>获取用户信息</el-button>
    <el-button @click="clear()" plain>清除</el-button>
    <el-button @click="create()" plain >{{createUserOper}}</el-button>
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

    <UserCreate :show="showCreate" @createdUser="createdUser" />
  </div>
</template>

<script>
  import { getUsers } from "@/request/user"
  import UserCreate from "@/components/UserCreate";

  export default {
    name: "User",
    data() {
      return {
        users: [],

        showCreate: false,
        createUserOper: "创建用户",
      }
    },
    components:{
      UserCreate,
    },

    watch:{
      showCreate(val){
        if(val){
          this.createUserOper = "隐藏创建用户"
        }else{
          this.createUserOper = "创建用户"
        }
      }
    },
    methods: {
      getUser() {
        let that = this;
        getUsers().then(function (response) {
          that.users = response;
        }).catch(function (exp) {
          console.log("========> e ", exp)
        })
      },
      clear() {
        this.users = [];
      },
      create(){
        this.showCreate = !this.showCreate
        this.createUserOper = this.showCreate ? "隐藏创建用户" : "创建用户"
      },

      createdUser(value){
        this.showCreate = false
        this.users.push(value)
        // 获取users
      }
    }
  }
</script>

<style>

</style>
