import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/home/home'
import instanceList from '../views/page/instanceList'
import instanceView from '../views/page/instanceView'

export let frameRouter = [
    {
        path: '/',
        name: 'instanceList',
        component: instanceList,
        meta: {
            title: '实例列表',
        }
    },
    {
        path: '/instanceView',
        name: 'instanceView',
        component: instanceView,
        meta: {
            title: '实例状态'
        }
    }
]
