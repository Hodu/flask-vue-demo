<template>
    <div class="popup-box" v-if="popupShow">
        <div class="header" @click="close()">
          <div class="close"></div>
        </div>
        <div class="header">
          <li v-for="item in arr" :key="item">
            <span>{{item.name}} == {{item.age}}</span>
          </li>
        </div>
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
      arr: Array,
    },
    watch:{
      show(val, oldVal){
        console.log("+======================show: ", val, oldVal)
        this.popupShow = val;
      }
    },
    data() {
      return {
        user: {
          username: '',
          mobile: ''
        },
        popupShow: false,

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
      close(){
        console.log("close, ", this.popupShow)
        console.log("close, arr = ", this.$props.arr)
        this.popupShow = false;
        this.$emit("cancel", false)
        console.log("close, 2", this.$props.show)
        this.$props.arr[0] = {"name":"c", "age":3}

      },
    }

}
</script>
<style lang="less" scoped>
  .popup-box {

    position: absolute;
    width: 500px;
    background: #f7f7f7;
    padding: 10px;
    z-index: 999;
    top: 40%;
    left: 30%;

    .header {
      height: 20px;
      .close {
        color: #444;
        width: 20px;
        height: 20px;
        background: red;
        float: right;
        &::before{
          content: "X";
        }
      }
    }
  }
</style>
