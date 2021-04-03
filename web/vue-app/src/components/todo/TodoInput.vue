<template>
  <div>
    <el-input v-model="input" :placeholder=placeHolder @change="inputTodo"></el-input>
  </div>
</template>

<script>
export default {
  name: "TodoInput",
  props: {
    placeHolder:{
      type: String,
      default: "请输入内容"
    },
  },
  data() {
    return {
      input: "",
    }
  },
  methods: {
    inputTodo(value){
      this.input = "";
      this.$emit("getInput", value)
    }
  }
}
</script>

<style scoped>

</style>
