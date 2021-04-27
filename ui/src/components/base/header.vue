<template>
    <div id="cw-header" :style="{height: headerHeight}">
        <div class="logo">
            <router-link to="/">
                <img :src="require('../../assets/base/img/logo.png')" class="CW-Logo" alt="嘉为蓝鲸">
            </router-link>
        </div>
        <div class="title PingFang">
            <router-link to="/">
                VUE框架
            </router-link>
        </div>
        <div class="menu">
            <HeaderMenu :menu-option="menuOption" :height="headerHeight" :menu-list="menuList"
                        v-if="showMenu"></HeaderMenu>
        </div>
        <div class="user">
            <ul>
                <li class="NameHover">
                    <Dropdown placement="right-start">
                        <span class="username Helvetica-Neue">{{userData.username}}</span>
                        <a style="margin-left: 10px" href="javascript:void(0)">
                            <Icon class="UserIcon" type="ios-arrow-down"></Icon>
                        </a>
                        <template slot="list">
                            <div class="detail">
                                <div @click="OutLogin" class="login-out-sty">
                                    <div class="icon-Sty">
                                        <Icon style="font-size:20px" type="ios-exit-outline"/>
                                    </div>
                                    <div class="font-Sty">退出登录</div>
                                </div>
                            </div>
                        </template>
                    </Dropdown>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    import $ from 'jquery'
    import HeaderMenu from '@/components/base/headerMenu'
    import userPath from '../../assets/base/img/logo.png'
    import whiteLogo from '../../assets/base/img/white_logo.png'

    export default {
        name: 'cw-header',
        props: {
            menuOption: {},
            menuList: {},
        },
        components: {
            HeaderMenu
        },
        data() {
            return {
                userData: {},
                username: '123',
                headerHeight: '60px',
                logout_url: '',
                src: whiteLogo,
                cusChange: false,
                showMenu: true
            }
        },
        created() {
            this.loginUser();
            if (this.headTheme === 'light') {
                this.src = userPath
            } else {
                this.src = whiteLogo
            }
        },
        watch: {
            $route: function () {
                let data = this.$route.meta.title;
                this.$emit('menuChange', data)
            }
        },
        methods: {
            loginUser() {
                this.$api.User.homeInfo().then(res => {
                    if (res.result) {
                        this.userData = res.data;
                    }
                });
            },
            OutLogin() {
                window.location.href = this.logout_url
            },
            goHome() {
                this.$router.push('/home')
            }
        }
    }
</script>

<style lang="scss" scoped>
    $headBackgroundColor: if($head-theme=='light', #fff, $base-color);
    $font-color: if($head-theme=='light', $base-color, #fff);
    $name-hover: if($head-theme=='light', #f7f8f9, $base-color);
    $header-font: if($head-theme=='light', $font-second, #D7EBFF);
    #cw-header {
        width: 100%;
        height: $headerHeight;
        border-bottom: 1px solid #ddd;
        position: absolute;
        z-index: 999;
        @media (max-width: 1920px) {
            height: 60px !important;
        }
        @media (min-width: 1920px) {
            height: 64px !important;
        }
        color: $font-color;
        background: $headBackgroundColor;
        display: flex;
        align-items: center;

        /deep/ .el-menu--horizontal > .el-submenu .el-submenu__title {
            @media (max-width: 1920px) {
                height: 60px !important;
                line-height: 60px !important;
            }
            @media (min-width: 1920px) {
                height: 64px !important;
                line-height: 64px !important;
            }
        }

        .logo {
            align-items: center;
            text-align: center;

            img {
                object-fit: scale-down;
            }

            .CW-Logo {
                width: 160px;
                height: 32px;
                margin-left: 20px
            }
        }

        .title {
            width: 200px;
            color: $font-color !important;
            font-size: 20px;
            padding: 1px 40px 0;

            a {
                color: $font-color !important;
            }
        }

        .menu {
            flex: 1;
        }

        .user {
            height: 100%;
            float: right;
            margin-right: 20px;

            .NameHover:hover {
                background-color: if($head-theme=='light', #fff, $base-color);
                border-bottom: 2px solid $font-color;

                .username, .UserIcon {
                    color: if($head-theme=='light', $base-color, #fff);
                }

            }

            ul {
                height: 100%;

                li {
                    height: 100%;
                    float: left;
                    line-height: 58px;
                }

                li:last-child {
                    /*width: 90px;*/
                    padding: 0 16px;
                    cursor: pointer;
                }

                .photo {
                    width: 46px;
                    height: 46px;
                    border-radius: 50px;
                    vertical-align: middle;
                    display: inline-block;
                    border: 1px solid #ddd;
                }

                .customer {
                    height: 60%;
                    margin-top: 20%;
                    border-radius: 10px;
                    color: $font-color;
                    padding: 0 5px;
                    text-align: center;
                    line-height: 40px;
                    background-color: #37b9ed;
                }

                .username {
                    font-size: 14px;
                    max-width: 100px;
                    white-space: nowrap;
                    text-overflow: ellipsis;
                    color: $header-font;
                    display: inline-block;
                    float: left;
                    overflow: hidden;
                }

                .UserIcon {
                    color: $header-font;
                }

                .detail {
                    height: 50px;
                    width: 110px !important;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    display: -webkit-flex;

                    .login-out-sty:hover {
                        background-color: $background-color;
                    }

                    .login-out-sty {
                        width: 100%;
                        padding: 1px;
                        height: 34px;
                        color: #000000;
                        text-align: center;

                        .icon-Sty {
                            width: 40%;
                            float: left;
                            height: 100%;
                            color: $font-second;
                            line-height: 34px;
                        }

                        .font-Sty {
                            width: 60%;
                            float: left;
                            height: 100%;
                            line-height: 38px;
                            color: $font-second;
                            font-size: 14px;
                        }
                    }
                }

                .login-out {
                    background: url("../../assets/base/img/下箭头.svg") no-repeat;
                    background-size: contain;
                    font-size: 20px;
                    width: 31px;
                    margin-top: 21px;
                    height: 20px;
                    /*border: 1px solid;*/
                    cursor: pointer;
                    /*vertical-align: sub;*/
                    display: inline-block;
                }

                .icon-logout:before {
                    color: if($head-theme=='light', #ccc, #fff);
                }

                .icon-logout:hover {
                    color: $white-color !important;
                }

            }
        }
    }
</style>
<style scoped>
    /deep/ .ivu-select-dropdown {
        will-change: top, left, right !important;
        right: 19px !important;
        width: 112px !important;
        left: initial !important;
        padding: 0px !important;
        margin: 0px !important;
        top: 63px !important;
    }
</style>
