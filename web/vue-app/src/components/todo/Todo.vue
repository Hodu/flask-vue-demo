<template>
  <div class="popup-box" v-if="popupShow">
    <todo-input :placeHolder="testPlaceHolder" @getInput="inputTodo"></todo-input>
    <div class="main-box">
      <todo-show-box :contents="contents" @updateTodo="updateTodo"></todo-show-box>
      <div class="td-footer">
        <div class="td-left">{{contents.length}} todos left</div>
        <div class="td-oper">
          <el-button type="text" @click="all" autofocus>all</el-button>
          <el-button type="text" @click="active">active</el-button>
          <el-button type="text" @click="completed">completed</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TodoInput from "@/components/todo/TodoInput";
import TodoShowBox from "@/components/todo/TodoShowBox";

export default {
  name: "Todo",
  components: {TodoShowBox, TodoInput},
  props: {
    maxLine: {
      type: Number,
      default: 5
    },
    minLine: {
      type: Number,
      default: 1,
    },
    show: {
      type: Boolean,
      default: false,
    },
  },
  watch: {
    show(val) {
      this.popupShow = val;

    }
  },
  data() {
    return {
      popupShow: false,
      testPlaceHolder: "what do you want todo...",
      contents: []
    };
  },
  methods: {
    inputTodo(value) {
      let len = this.contents.length;
      this.contents.push({id: len + 1, content: value});
    },
    updateTodo(value){
      console.log("=====> update .. ", value)
      this.contents = this.contents.filter(a => a.id !== value.id);
    },
    all(){
      console.log("all---->", this.contents)
    },
    active(){
      console.log("active---->", this.contents)
    },
    completed(){
      console.log("completed---->", this.contents)
    }
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
  box-shadow: 0 2px 4px 0 rgb(0 0 0 / 20%), 0 25px 50px 0 rgb(0 0 0 / 10%);

  .main-box{

    .td-footer{
      display: flex;
      align-items: center;
      .td-left {
        display: flex;
        width: 40%;
      }
      .td-oper {
        button:hover, button:focus{
          border: 1px solid;
          border-radius: 3px;
          border-color: rgba(175, 47, 47, 0.2);
        }
      }
    }
  }

  .header {
    height: 20px;

    .close {
      color: #444;
      width: 20px;
      height: 20px;
      background: red;
      float: right;

      &::before {
        content: "X";
      }
    }
  }
}
</style>
