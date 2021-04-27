// server模块（各模块）api
import {get, post, reUrl} from '../axiosconfig/axiosconfig'

// 返回在vue模板中的调用接口
export default {
    //----GET-------------------------------------------------------------
    //测试 get 请求
    testGet: function (params) {
        return get(reUrl + '/test_get/', params)
    },
    //----POST------------------------------------------------------------
    //测试 post 请求
    testPost: function (params) {
        return post(reUrl + '/test_post/', params, {showLoad: true})
    }
}
