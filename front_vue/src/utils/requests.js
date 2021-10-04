import Vue from "vue";
import axios from "axios";
import {message, notification} from "ant-design-vue";
import { VueAxios } from "axios";

message.config({
  maxCount: 2,
});

//创建axios实例
const service = axios.create({
  timeout: 12000
})

const error = (error) => {
  if (!error.response){
    message.error('请检查网络连接')
    return Promise.reject(error)
  }
  return Promise.reject(error)
}

service.interceptors.request.use(config => {
  config.method = config.method || 'get'

  if (config.method === 'get' && config.data) {
    config.params = Object.assign( {}, config.params, config.data)
  }

  return config
}, error)

service.interceptors.response.use( (response) => {
  if (response.data.success === false && response.data.message) {
    message.error(response.data.message)
  }
})

const installer = {
  vm: {},
  install (Vue) {
    Vue.use(VueAxios, service)
  }
}

export {
  installer as VueAxios,
  service as axios
}
