module.exports = {
  //关闭eslint
  lintOnSave: false,
  devServer: {
    port: 13520,
    proxy: {
      "/air": {
        target: "http://127.0.0.1:13140", // 跨域目标主机，自行修改
        ws: true, // 代理 websockets
        changeOrigin: true,
        pathRewrite: {
          "^/air": "/v1/air" // 重写地址
        },
        logLevel: 'debug'
      },
      "/testconn": {
        target: "http://127.0.0.1:13140", // 跨域目标主机，自行修改
        ws: true, // 代理 websockets
        changeOrigin: true,
        logLevel: 'debug'
      }
    }
  }
};
