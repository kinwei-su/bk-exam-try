<template>
    <div id="main-container">
        <LeftMenu v-if="showLeftMenu"
                  :style="{width: leftWidth}"
                  @colChange="colChange"
                  :menu-list="menuList"></LeftMenu>
        <div :class="{'full-width':!showLeftMenu,'col-left':colState}" style="width: calc(100% - 216px);">
            <div class="top-menu" v-if="showLeftMenu&&IsFarme">
                <Breadcrumb separator="<span class='menu-bread'>></span>">
                    <BreadcrumbItem v-for="(item,index) in breadList" :key="index" :to="item.path">{{item.name}}
                    </BreadcrumbItem>
                </Breadcrumb>
            </div>
            <router-view
                :class="{'router-style':true,'content-body':showLeftMenu&&IsFarme,'farme-style':!IsFarme}"/>
        </div>
    </div>
</template>

<script>
    // import LeftMenu from '@/components/base/leftMenu'
    import LeftMenu from '@/components/base/eleLeft.vue'
    import {frameRouter} from '@/router/frameRouter.js'

    export default {
        name: 'main-container',
        props: {
            menuList: {}
        },
        components: {
            LeftMenu
        },
        data() {
            return {
                showLeftMenu: true,
                coMenu: '',
                IsFarme: true,
                appType: '',
                breadList: [],
                headerHeight: '60px',
                leftWidth: '65px',
                nowTitle: '',
                colState: false
            }
        },
        created() {
            this.isShowLeftMenu();
            this.judgeFarme()
            this.getBreadcrumb()
        },
        methods: {
            //判断是否是框架的页面 不用可以注释
            judgeFarme() {
                for (let item in frameRouter) {
                    if (this.$route.name === frameRouter[item].name) {
                        this.IsFarme = false
                    }
                    if (this.$route.name === 'InstancePage') {
                        this.IsFarme = true
                    }
                }
            },
            //是否展示左边导航栏
            isShowLeftMenu() {
                if (this.$route.path === '/' || this.$route.path === '/home') {
                    this.showLeftMenu = false;
                    this.colChange(false)
                } else {
                    this.showLeftMenu = true;
                }
            },
            /*
            新开发时 建议在跳转页面的子页面时 路由里面增加children 页面里面增加 <route-view></route-view>
            重新开发框架 就利用路由元信息 吧路径结构配置在Route meat属性中  自行更改：例如
             meta: {
                breadList: [{
                    name: "首页",
                    path: "/home"
                }, {
                    name: "系统设置",
                    path: "/setting"
                }, {
                    name: "用户管理",
                    path: "/setting/usermanage"
                }]
            }
            可以参照公共组件：https://paas.cwbk.com/o/cw-public/#/activeDetail?id=581&operation=myActive
             */
            //获取路由路径
            getBreadcrumb() {
                // let matched = this.$route.matched; //获取路由记录 包含当前路由的所有嵌套路径片段的路由记录
                this.breadList = this.$route.meta.breadList;
            },
            isHome(route) {
                return route.name === '/';
            },
            //左边导航栏是否伸缩
            colChange(data) {
                if (this.showLeftMenu) {
                    this.colState = data
                    this.leftWidth = data ? '64px' : '216px'
                } else {
                    this.colState = false
                }
            }
        },
        watch: {
            $route: function () {
                this.judgeFarme()
                this.getBreadcrumb()
                this.isShowLeftMenu()
            }
        },
    }
</script>

<style lang="scss" scoped>
    $headerHeight: 60px;
    #main-container {
        width: 100%;
        background: #fff;
        @media (max-width: 1920px) {
            top: 60px !important;
        }
        @media (min-width: 1920px) {
            top: 64px !important;
        }
        position: absolute;
        display: flex;
        overflow: hidden;

        .full-width {
            width: 100% !important;
        }

        .col-left {
            width: calc(100% - 64px) !important;
        }

        .router-style {
            background-color: $background-color;
            height: calc(100% - 30px) !important;
            color: $font-second;
        }

        .farme-style {
            padding: 16px !important;
            height: calc(100% - 0px) !important;
            background-color: #fff!important;
        }

        .content-body {
            height: calc(100% - 30px) !important;
            width: calc(100%) !important;;
            padding: 0px 16px 16px 16px;
            background-color: $background-color;
        }

        .top-menu {
            height: 32px;
            background-color: $background-color;
            font-size: 14px;
            line-height: 32px;
            padding-left: 16px;
            vertical-align: bottom;

            /deep/ .menu-bread {
                color: $font-color;
            }
        }
    }
</style>
