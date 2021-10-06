import axios from "axios";
import {message} from "ant-design-vue";
import { VueAxios } from "./axios";

message.config({
  maxCount: 2,
});

//创建axios实例
const axiosInstance = axios.create({
  timeout: 6000
})

const error = (error) => {
  if (!error.response){
    message.error('请检查网络连接')
    return Promise.reject(error)
  }
  return Promise.reject(error)
}

axiosInstance.interceptors.request.use(config => {
  config.method = config.method || 'get'

  if (config.method === 'get' && config.data) {
    config.params = Object.assign( {}, config.params, config.data)
  }

  return config
}, error)

axiosInstance.interceptors.response.use( (response) => {
  if (response.data.success === false && response.data.message) {
    message.error(response.data.message)
  }else{
    return response.data
  }
})

const installer = {
  vm: {},
  install (Vue) {
    Vue.use(VueAxios, axiosInstance)
  }
}

export default axiosInstance;

export {
  installer as VueAxios,
  axiosInstance as axios
}
