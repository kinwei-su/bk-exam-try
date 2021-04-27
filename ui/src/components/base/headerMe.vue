<template>
    <div id="header-menu">
        <Menu class="el-menu-demo PingFang .font-14 elMenu-Sty" mode="horizontal" theme="light"
              :active-name="activeIndex">
            <MenuItem v-for="item in menuList"
                      :key="item.name"
                      :name="item.name"
                      :to="item.to"
                      v-if="!item.hasChild">
                <Icon :type="item.icon"/>
                {{item.cnName}}
            </MenuItem>
            <Submenu v-if="item.hasChild"
                     v-for="(item,index) in menuList"
                     :key="item.name" :name="index">
                <template slot="title">
                    <Icon :type="item.icon"/>
                    {{item.cnName}}
                </template>
                <div style="width:200px" v-for="(child,childIndex) in item.children"
                     :key="child.name">
                    <MenuItem
                        :name="index+ '-' + childIndex"
                        v-if="!child.hasChild"
                        :to="child.to">{{child.cnName}}
                    </MenuItem>
                    <Submenu v-if="child.hasChild"
                             :to="child.to">
                        <template slot="title">{{child.cnName}}</template>
                        <MenuItem
                            v-for="(third,thirdIndex) in child.children"
                            :name="index+ '-' + childIndex + '-' +thirdIndex"
                            :key="third.name"
                            :to="third.to">{{third.cnName}}
                        </MenuItem>
                    </Submenu>
                </div>
            </Submenu>
        </Menu>
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

    .elMenu-Sty:hover {
        background-color: #fff !important;
    }
</style>
<style scoped>
    /deep/ .ivu-select-dropdown {
        overflow: auto !important;
        margin: 5px 0 !important;
        width: auto !important;
        max-height: none !important;
        padding: 5px 0 !important;
        background-color: #fff !important;
        right: -70px !important;
        box-sizing: border-box !important;
        border-radius: 4px !important;
        box-shadow: 0 1px 6px rgba(0, 0, 0, .2) !important;
        position: absolute !important;
        z-index: 900 !important;
    }
</style>
