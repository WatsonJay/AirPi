import model from './model'; // 导入接口域名列表
import axiosInstance from '@/utils/requests'; // 导入http中创建的axios实例

const air = {
    // 新闻列表
    getDashData () {
        return axiosInstance.get(`${model.air}/getDashData`);
    },
    getHistoryData () {
        return axiosInstance.get(`${model.air}/getHistoryData`);
    },
}

export default air;
