<template>
  <div>
    <el-checkbox-group v-model="checked" @change="handleCheckedChange">
      <div v-for="item in contents" :key="item.id" class="todo_item">
        <div class="ct_item">
          <el-checkbox :label="item.id" ></el-checkbox>
          <el-input v-model="item.content" :readonly="readonlies.indexOf(item.id) == -1"
                    @dblclick="doubleCheck(item.id)" :class="selected.indexOf(item.id) != -1 ? 'del': ''">
            <template #suffix>
              <i class="el-input__icon el-icon-delete" @click="delTodo(item)"></i>
            </template>
          </el-input>
        </div>
<!--        <div class="ct_del" ref="cccc" v-if="selected.indexOf(item.id) != -1">-->
<!--          <el-button icon="el-icon-delete" :data-id="item.id" @click="delTodo(item)" title="点击删除该内容"></el-button>-->
<!--        </div>-->
      </div>
    </el-checkbox-group>

  </div>
</template>

<script>

export default {
  name: "TodoShowBox",
  props: {
    contents:{
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      checked: [],
      readonlies: [],
      selected:[],
      todos: [],
    }
  },
  created() {
  },
  methods:{
    handleCheckedChange(value){
      console.log("====>", value)
      this.selected = value;
    },

    doubleCheck(id){
      console.log("===>", id)
      this.readonlies.push(id);
    },
    delTodo(_todo){
      console.log("ready to del 1:", _todo);
      console.log("ready to del 2:",this.$props.contents);
      // console.log(this.$props.contents.indexOf(_todo));
      this.$emit("updateTodo", _todo)
      this.$props.contents = this.$props.contents.filter(a => a.id !== _todo.id);
      console.log("ready to del 4:",this.$props.contents);
    },
  },
  watch:{
    todos(val){
      if(val) {
        console.log("======>wwww", val);
      }else{
        console.log("www.....", val)
      }
    }
  }
}
</script>

<style lang="less" scoped>
  .todo_item {
    display: flex;
    align-items: baseline;

  .ct_item {
    width: 100%;
    display: flex;
    align-items: baseline;

    /deep/ .el-input.del {
      .el-input__inner {
        color: #d9d9d9;
        text-decoration: line-through;
      }
    }

    /deep/ .el-input:hover {
      .el-input__inner {
        color: #000000;
        border-color: #77a0cb;
      }
      .el-input__suffix {
        display: inline-block;
      }
    }

    /deep/ .el-checkbox__inner {
      border-radius: 50%;
      width: 20px;
      height: 20px;
      margin-right: 8px;
    }
    /deep/ .el-input__suffix {
      display: none;
    }
    /deep/ .el-input__suffix:hover {
      color: #409EFF;
    }

    /deep/ .el-checkbox__inner::after {
      height: 10px;
      left: 6px;
      width: 5px;
    }

    /deep/ .el-checkbox__label {
      display: none;
    }

    .ct_del {

    }
  }

  }
</style>
