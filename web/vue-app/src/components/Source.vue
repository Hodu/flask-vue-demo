<template>
  <div>
  <el-row :gutter="20">
    <el-col :span="16"><div class="grid-content bg-purple">111</div></el-col>
    <el-col :span="8"><div class="grid-content bg-purple">222</div></el-col>
  </el-row>
  <el-row :gutter="20">
    <el-col :span="8"><div class="grid-content bg-purple">333</div></el-col>
    <el-col :span="8"><div class="grid-content bg-purple">444</div></el-col>
    <el-col :span="4"><div class="grid-content bg-purple">5555</div></el-col>
    <el-col :span="4"><div class="grid-content bg-purple">666</div></el-col>
  </el-row>
  <el-row :gutter="20">
    <el-col :span="4"><div class="grid-content bg-purple">777</div></el-col>
    <el-col :span="16"><div class="grid-content bg-purple">888</div></el-col>
    <el-col :span="4"><div class="grid-content bg-purple">999</div></el-col>
  </el-row>
  </div>
</template>


<style>
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>