<template>
    <div id="header-menu">
        <el-menu
            :default-active="activeIndex"
            class="el-menu-demo PingFang .font-14"
            mode="horizontal"
            menu-trigger="hover"
            @open="handleopen"
            @close="handleclose"
            show-timeout="10"
            hide-timeout="400"
            router>
            <el-menu-item
                v-for="item in menuList"
                :key="item.name"
                class="elMenu-Sty"
                :index="item.to"
                v-if="!item.hasChild">{{item.cnName}}
            </el-menu-item>
            <el-submenu v-if="item.hasChild"
                        v-for="item in menuList"
                        :key="item.name"
                        :index="item.to">
                <template slot="title">{{item.cnName}}</template>
                <div v-for="child in item.children"
                     :key="child.name">
                    <el-menu-item
                        v-if="!child.hasChild"
                        :index="child.to">{{child.cnName}}
                    </el-menu-item>
                    <el-submenu v-if="child.hasChild"
                                :index="child.to">
                        <template slot="title">{{child.cnName}}</template>
                        <el-menu-item
                            v-for="third in child.children"
                            :key="third.name"
                            :index="third.to">{{third.cnName}}
                        </el-menu-item>
                    </el-submenu>
                </div>
            </el-submenu>
        </el-menu>
    </div>
</template>
<script>
    export default {
        name: 'headerMenu',
        props: {
            menuOption: {},
            menuList: {},
            height: 0,
        },
        data() {
            return {
                theme1: 'light',
                activeIndex: '/home',
            };
        },
        mounted() {
            this.activeIndex = this.$route.name;
            if (this.$route.path === '/') {
                this.activeIndex = '/home'
            }
        },
        methods: {
            handleopen(key, keyPath) {
            },
            handleclose(key, keyPath) {
            },
        }
    }
</script>
<style lang="scss">
    .elMenu-Sty {
        margin: 0 40px 0 0 !important;
        @media (max-width: 1920px) {
            height: 60px !important;
            line-height: 59px !important;
        }
        @media (min-width: 1920px) {
            height: 64px !important;
            line-height: 63px !important;
        }
    }
</style>
