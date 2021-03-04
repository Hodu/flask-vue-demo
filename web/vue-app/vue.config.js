module.exports={
    devServer:{
        proxy:{
            ["/dev-api"]:{
            target:'http://localhost:8001/api/v1.0',
              changeOrigin:true,
                pathRewrite: {
                    ['^' + "/dev-api"]: ''
                }
            }
        }
    },
    chainWebpack: config => {
        // 修复HMR
        config.resolve.symlinks(true);
    },
}