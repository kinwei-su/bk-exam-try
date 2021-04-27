<template>
    <div id='app' @click="cancel">
        <Header :menu-list="headerList"></Header>
        <Container :menu-list="menuList" class="container-style"></Container>
    </div>
</template>

<script>
    import Header from '@/components/base/header'
    import Container from '@/components/base/container'

    export default {
        name: 'App',
        components: {
            Header,
            Container
        },
        mounted() {
            this.$CustomerType = 0;
        },
        created() {
            this.getHeight();
        },
        data() {
            return {
                headerHeight: 60,
                //框架原始左侧导航栏
                menuList: [
                    {
                        name: 'Grid',
                        cnName: '栅格',
                        to: '/grid',
                        icon: 'ios-grid-outline',
                        hasChild: false,
                        children: []
                    },
                    {
                        name: 'Layout',
                        cnName: '布局',
                        to: '/layout',
                        icon: 'ios-browsers-outline',
                        hasChild: false,
                    },
                    {
                        name: 'Color',
                        cnName: '色彩',
                        to: '/color',
                        icon: 'ios-color-fill-outline',
                        hasChild: false,
                    },
                    {
                        name: 'Font',
                        cnName: '字体',
                        to: '/font',
                        icon: 'ios-at-outline',
                        hasChild: false,
                    },
                    {
                        name: 'Icon',
                        cnName: '图标',
                        to: '/icon',
                        icon: 'ios-heart-outline',
                        hasChild: false,
                    }, {
                        name: 'Card',
                        cnName: '卡片',
                        to: '/card',
                        icon: 'ios-card-outline',
                        hasChild: false,
                    }, {
                        name: 'Collapse',
                        cnName: '折叠面板',
                        to: '/collapse',
                        icon: 'ios-albums-outline',
                        hasChild: false,
                    },
                    {
                        name: 'Apply',
                        cnName: '应用',
                        to: '/apply',
                        icon: 'ios-at-outline',
                        hasChild: false,
                    }, {
                        name: 'Button',
                        cnName: '按钮',
                        to: '/button',
                        icon: 'ios-radio-button-off',
                        hasChild: false,
                    }, {
                        name: 'Border',
                        cnName: '边框',
                        to: '/border',
                        icon: 'ios-bookmark-outline',
                        hasChild: false,
                    }, {
                        name: 'InstancePage',
                        cnName: '示例',
                        to: '/instancePage',
                        icon: 'ios-document-outline',
                        hasChild: true,
                        children: [{
                            cnName: '示例页面',
                            hasChild: false,
                            key: 1,
                            to: '/instancePage'
                        }],
                    }
                ],
                //顶部导航栏
                headerList: [
                    {
                        name: 'Grid',
                        cnName: '栅格',
                        to: '/grid',
                        icon: 'ios-grid-outline',
                        hasChild: false,
                        children: []
                    },
                    {
                        name: 'Layout',
                        cnName: '布局',
                        to: '/layout',
                        icon: 'ios-browsers-outline',
                        hasChild: false,
                    },
                    {
                        name: 'Color',
                        cnName: '色彩',
                        to: '/color',
                        icon: 'ios-color-fill-outline',
                        hasChild: false,
                    },
                    {
                        name: 'Font',
                        cnName: '字体',
                        to: '/font',
                        icon: 'ios-at-outline',
                        hasChild: false,
                    },
                    {
                        name: 'Icon',
                        cnName: '图标',
                        to: '/icon',
                        icon: 'ios-heart-outline',
                        hasChild: false,
                    }, {
                        name: 'InstancePage',
                        cnName: '示例',
                        to: '/instancePage',
                        icon: 'ios-document-outline',
                        hasChild: true,
                        children: [{
                            cnName: '示例页面',
                            hasChild: false,
                            key: 1,
                            to: '/instancePage'
                        }],
                    }],
            }
        },
        methods: {
            cancel() {
            },
            getHeight() {
                let headerHeight = 60;
                if (window.innerHeight) {
                    this.winHeight = window.screen.availHeight - (window.outerHeight - window.innerHeight);
                }
                // if (document.documentElement && document.documentElement.clientHeight && document.documentElement.clientWidth) {
                //     this.winHeight = document.documentElement.clientHeight;
                // }
                this.winHeight = this.winHeight - headerHeight + 'px'
            }
        }
    }
</script>
<style lang="scss">
    html, body {
        height: 100%;
    }

    .container-style {
        @media (max-width: 1920px) {
            height: calc(100% - 60px);
        }
        @media (min-width: 1920px) {
            height: calc(100% - 64px);
        }
    }

    ::-webkit-scrollbar-thumb:window-inactive {
        background: rgba(255, 0, 0, .4)
    }

    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
        background-color: rgba(255, 255, 255, .07)
    }

    ::-webkit-scrollbar-thumb {
        -webkit-border-radius: 10px;
        border-radius: 10px;
        background: rgba(11, 54, 106, .52);
        -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, .5)
    }

    ::-webkit-scrollbar-thumb:window-inactive {
        background-color: rgba(255, 255, 255, .07)
    }

    .pm-title {
        margin-left: 10px;

        .pm-title-block {
            width: 20px;
            height: 22px;
            margin-top: 2px;
            float: left;
        }

        .ivu-icon-md-settings {
            font-size: 22px;
            color: #1facdd;
        }
    }

    .pm-top {
        border: 1px solid rgb(227, 227, 227);
        background-color: white;
        height: 80px;

        > div {
            > div, > span, > button {
                vertical-align: middle;
            }
        }
    }

    .planpage {
        background-color: white;
        height: 100%;
        width: 100%;
        box-sizing: border-box;
        overflow: auto;
        position: relative;
        overflow-x: hidden;
        padding: 10px;
    }

    .base {
        position: absolute;
        width: 98%;
        left: 1%;
        top: 42px;
        padding: 10px;
        z-index: 9;
        border: 1px solid #e3e3e3;
        font-size: 0;
        text-align: center;

        .base_box {
            display: inline-block;
            padding-right: 30px;
            vertical-align: top;

            > span {
                display: inline-block;
                font-size: 12px;
                float: left;
                line-height: 32px;
                height: 64px;
                overflow: auto;
            }
        }
    }

    .flow {
        position: absolute;
        width: 98%;
        top: 0;
        left: 1%;
        height: 100%;
        padding-top: 160px;
        font-size: 0;

        > div {
            font-size: 12px;
            display: inline-block;
            height: 200px;
            vertical-align: top;
        }

        .pre, .next {
            width: 2%;
            cursor: pointer;
            position: relative;
            background: #fff;
            height: 200px;
            color: #333;

            > i {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
            }
        }

        .pre:hover, .next:hover {
            background-color: #999;

            > i {
                color: #fff;
            }
        }

        .flow_body {
            width: 96%;
            height: 100%;
            overflow-x: hidden;
            position: relative;

            #flow_box {
                position: absolute;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
                white-space: nowrap;
                transition: all 0.5s ease
            }

            #flow_box1 {
                /*position: absolute;*/
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
                white-space: nowrap;
                transition: all 0.5s ease
            }

            .step_box {
                display: inline-block;
                width: 25.6%;
                font-size: 0;

                > div {
                    font-size: 12px;
                    display: inline-block;
                    vertical-align: middle;
                }

                .step_base {
                    background: #f3f3f3;
                    color: #fff;
                    width: 90%;
                    padding: 10px;
                    border: none;
                    position: relative;
                    color: #333;

                    .number_box {
                        background: #bbb;
                        position: absolute;
                        left: 0;
                        top: 0;
                        width: 50px;
                        text-align: center;
                        height: 100%;
                        line-height: 94px;
                        font-size: 18px;
                        font-weight: bold;
                    }

                    .node_body {
                        position: absolute;
                        top: 100%;
                        left: 1px;
                        width: 100%;
                        color: #000;

                        .node_base {
                            width: 100%;
                            padding-left: 40px;
                            border: 1px solid #d7d7d7;
                            font-size: 14px;
                            padding: 5px;
                            padding-right: 24px;
                            text-align: center;
                            overflow-x: hidden;
                            white-space: nowrap;
                            word-break: break-all;
                            text-overflow: ellipsis;
                            position: relative;
                            margin: 8px 0;

                            .icon_box {
                                position: absolute;
                                left: 0;
                                top: 0;
                                width: 40px;
                                height: 41px;
                                background: #bbb;
                                color: #fff;

                                i {
                                    line-height: 40px;
                                }
                            }

                            .icon_box.finish {
                                background-color: green;
                            }

                            .icon_box.wait {
                                background-color: #d7d7d7;
                            }

                            .icon_box.error {
                                background-color: #ffb400;
                            }

                            .icon_box.run {
                                background-color: #fff;
                                border-right: 1px solid #d7d7d7;
                                color: #000;
                            }

                            .icon_box.fail {
                                background-color: red;
                            }

                            .icon_box.pause {
                                background-color: #fff;
                                border-right: 1px solid #d7d7d7;
                                color: #000;
                            }

                            .icon_box.stop {
                                background-color: #fff;
                                border-right: 1px solid #d7d7d7;
                                color: #000;
                            }

                            > span {
                                display: inline-block;
                                width: 100%;
                                padding: 5px;
                                cursor: pointer;
                                display: inline-block;
                                height: 31px;
                            }

                            .operate_node {
                                position: absolute;
                                top: 0;
                                right: 0;
                                cursor: pointer;
                            }

                            .detail_url {
                                position: absolute;
                                right: 0;
                                top: 0;
                                line-height: 40px;
                                width: 24px;
                            }
                        }
                    }

                    .operate {
                        position: absolute;
                        top: 0;
                        right: 0;
                        cursor: pointer;
                        padding: 3px;
                    }
                }

                .plus {
                    width: 10%;
                    height: 100%;
                    text-align: center;
                    cursor: pointer;
                }
            }

            .firm.step_box {
                .step_base {
                    div {
                        margin-bottom: 10px;
                        line-height: 64px;
                        font-size: 18px;
                        text-align: center;
                    }
                }
            }
        }
    }

    #node_detail {
        position: absolute;
        right: 0;
        width: 50%;
        top: 0;
        z-index: 10;
        height: 100%;
        background-color: #fff;
        border-left: 1px solid #d7d7d7;
        padding: 20px;
        box-shadow: 0 5px 5px rgba(170, 170, 170, .32);
        transition: all 0.5s ease;
        overflow: auto;

        .left_box {
            position: absolute;
            left: -100%;
            width: 100%;
            height: 100%;
            top: 0;
            display: block;
        }

        .ops_cell {
            width: 100%;
            height: auto;
            max-height: 300px;
            overflow-y: auto;

            > div {
                padding: 0 10px;
                width: 20%;
                float: left;
                margin: 10px 5% 10px 0;
                height: 45px;
                text-align: center;
                line-height: 45px;
                border: 1px solid #d7d7d7;
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
                word-break: break-all;
                cursor: pointer;
            }

            > div.action {
                border: 2px solid green
            }
        }
    }

    #node_detail.right_hiden {
        right: -50%;

        .left_box {
            display: none;
        }
    }
</style>

