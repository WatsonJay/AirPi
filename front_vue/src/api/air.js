import model from './model'; // 导入接口域名列表
import axios from '@/utils/requests'; // 导入http中创建的axios实例

const air = {
    // 新闻列表
    getDashData () {
        return axios.get(`${model.air}/getDashData`);
    },
}

export default air;
