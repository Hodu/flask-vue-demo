<template>
    <div class="popup-box" v-if="show">
        <el-form :model="user" ref="user" :rules="rules">
            <el-form-item
                prop="username"
                label="姓名"

            >
            <el-input v-model="user.username"></el-input>
            </el-form-item>
             <el-form-item
                prop="mobile"
                label="手机"

            >
            <el-input v-model="user.mobile"></el-input>
            </el-form-item>

             <el-form-item>
                <el-button type="primary" @click="submitForm('user')">提交</el-button>
                <el-button @click="resetForm('user')">重置</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    name: 'create-user',
    props: {
      show:{
        type: Boolean,
        default: false,
      },

    },
    watch:{
      show(val){
        console.log("+======================show: ", val)
      }
    },
    data() {
      return {
        user: {
          username: '',
          mobile: ''
        },

        rules:{
          username:[
              { required: true, message: '请输入姓名', trigger: 'blur' },
          ],
          mobile:[
              { required: true, message: '请输入手机', trigger: 'blur' },
          ]
        }

      };
    },
    methods: {
      submitForm(formName) {
        console.log("===============formNAME ", formName)
        console.log("------------<1" , this.user)
        let user = { ...this.user }
        console.log("------------<2" , user)
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!');
            this.$emit('createdUser', user);
            this.user = {}
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
    }

}
</script>
<style>
  .popup-box{

    position: absolute;
    width: 500px;
    background: #f7f7f7;
    padding: 10px;
    z-index: 999;
    top: 40%;
    left: 30%;

  }
</style>
