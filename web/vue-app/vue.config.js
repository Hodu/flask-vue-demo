
const publicPath = process.env.VUE_APP_BASE
// 设置端口
const port = process.env.DEV_PORT

const backend_url =  process.env.BACKEND_URL

module.exports={
    devServer:{
        publicPath,
        port,
        proxy:{
            ["/dev-api"]:{
            target: backend_url,
              changeOrigin: true,
                pathRewrite: {
                    ['^' + "/dev-api"]: ''
                }
            }
        }
    },
    chainWebpack: config => {
        // 修复HMR  解决 cli3 热更新失效 https://github.com/vuejs/vue-cli/issues/1559
        config.resolve.symlinks(true)

        config
        // 开发环境
        .when(process.env.NODE_ENV === 'development',
            // sourcemap不包含列信息
            config => config.devtool('cheap-source-map')
        )
    },
}
