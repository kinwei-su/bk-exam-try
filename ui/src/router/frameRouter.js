import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/home/home'
import Grid from '@/views/canwayUI/grid'
import Color from '@/views/canwayUI/color'
import Font from '@/views/canwayUI/font'
import Card from '@/views/canwayUI/card'
import Icon from '@/views/canwayUI/icon'
import Layout from '@/views/canwayUI/layout'
import Collapse from '@/views/canwayUI/collapse'
import Button from '@/views/canwayUI/button'
import Apply from '@/views/canwayUI/apply'
import Border from '@/views/canwayUI/border'
import InstancePage from '@/views/canwayUI/instancePage'

export let frameRouter = [
    {
        path: '/',
        name: 'Grid',
        component: Grid,
        meta: {
            title: '栅格',
        }
    },
    {
        path: '/grid',
        name: 'Grid',
        component: Grid,
        meta: {
            title: '栅格',
        }
    }, {
        path: '/color',
        name: 'Color',
        component: Color,
        meta: {
            title: '色彩',
        }
    }, {
        path: '/font',
        name: 'Font',
        component: Font,
        meta: {
            title: '字体',
        }
    }, {
        path: '/card',
        name: 'Card',
        component: Card,
        meta: {
            title: '卡片',
        }
    }, {
        path: '/icon',
        name: 'Icon',
        component: Icon,
        meta: {
            title: '图标',
        }
    }, {
        path: '/layout',
        name: 'Layout',
        component: Layout,
        meta: {
            title: '布局',
        }
    }, {
        path: '/collapse',
        name: 'Collapse',
        component: Collapse,
        meta: {
            title: '折叠面板',
        }
    }, {
        path: '/button',
        name: 'Button',
        component: Button,
        meta: {
            title: '按钮',
        }
    }, {
        path: '/apply',
        name: 'Apply',
        component: Apply,
        meta: {
            title: '应用',
        }
    },
    {
        path: '/border',
        name: 'Border',
        component: Border,
        meta: {
            title: '边框',
        }
    },
    {
        path: '/instancePage',
        name: 'InstancePage',
        component: InstancePage,
        meta: {
            breadList: [{
                name: '示例',
                path: '/instancePage'
            }, {
                name: '示例页面',
                path: '/instancePage'
            }]
        }
    }
]
