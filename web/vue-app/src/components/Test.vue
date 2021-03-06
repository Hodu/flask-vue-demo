<template>
  <div>
    <span>{{ serverResponse }} </span>
    <el-button @click="getData" round>GET DATA</el-button>
    <!-- <Source /> -->
  </div>
</template>

<script>
import { getMsg } from '@/request/test';
// import Source from "@/components/Source";

export default {
  name: "Test",
  components: {
    //  Source
  },
  data() {
    return {
      serverResponse: 'resp'
    }
  },
  methods: {

    getData() {
      console.log("================================")
      let that = this;

      getMsg().then(function (response) {
        // 这里服务器返回的 response 为一个 json object，可通过如下方法需要转成 json 字符串
        // 可以直接通过 response.data 取key-value
        // 坑一：这里不能直接使用 this 指针，不然找不到对象
        console.log("----> ", response)
        let msg = response.msg;
        // 坑二：这里直接按类型解析，若再通过 JSON.stringify(msg) 转，会得到带双引号的字串
        that.serverResponse = msg;

        // alert('Success ' + response.status + ', ' + response.data + ', ' + msg);
      }).catch(function (error) {
        alert('Error ' + error);
      })
      // axios.get(path).then(function (response) {
      //   // 这里服务器返回的 response 为一个 json object，可通过如下方法需要转成 json 字符串
      //   // 可以直接通过 response.data 取key-value
      //   // 坑一：这里不能直接使用 this 指针，不然找不到对象
      //   var msg = response.data.msg;
      //   // 坑二：这里直接按类型解析，若再通过 JSON.stringify(msg) 转，会得到带双引号的字串
      //   that.serverResponse = msg;
      //
      //   alert('Success ' + response.status + ', ' + response.data + ', ' + msg);
      // }).catch(function (error) {
      //   alert('Error ' + error);
      // })
    }
  }
}
</script>
