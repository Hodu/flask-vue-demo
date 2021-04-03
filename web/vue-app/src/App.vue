<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <Test />
  <User />

  <router-view></router-view>
</template>

<script>
import Test from '@/components/Test.vue'
import User from "@/page/User";

export default {
  name: 'App',
  components: {
    Test,
    User
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
