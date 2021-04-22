// server模块（各模块）api
import {get, post, reUrl} from '../axiosconfig/axiosconfig'

// 返回在vue模板中的调用接口
export default {
    //----GET-------------------------------------------------------------
    //测试 get 请求
    search_bussiness_topo: function (params) {
        return get(reUrl + '/search_bussiness_topo/', params)
    },
    query_detail: function (params) {
        return post(reUrl + '/query_detail/', params)
    },
    query_node_info: function (params) {
        return post(reUrl + '/query_node_info/', params)
    },
    search_bussiness: function (params) {
        return get(reUrl + '/search_bussiness/', params)
    },
    search_base_info: function (params) {
        return get(reUrl + '/search_base_info/', params)
    },
    search_host_list: function (params) {
        return post(reUrl + '/search_host_list/', params)
    },
    //----POST------------------------------------------------------------
    //测试 post 请求
    testPost: function (params) {
        return post(reUrl + '/test_post/', params, {showLoad: true})
    }
}
