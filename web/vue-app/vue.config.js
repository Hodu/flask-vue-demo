module.exports={
    devServer:{
        host:'localhost',   //选填
        port: 8010, //选填
        proxy:{     //必填
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