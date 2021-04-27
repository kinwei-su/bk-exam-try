<template>
    <div id="grid">
        <div class="Titles font-20">Layout 布局</div>
        <div class="summary font-18">横版</div>
        <div class="transverse">
            <div class="transverseTop font-20 hightBackColor">全屏宽度</div>
            <div class="transverseContentleft"></div>
            <div class="transverseContent font-18"></div>
            <div class="transverseBottom">
                <div class="leftNavigation font-14 hightBackColor">侧边导航 216px</div>
                <div class="leftContent backColor font-14">内容区width</div>
            </div>
        </div>
        <div class="vertical font-18">竖版</div>
        <div class="transverse">
            <div class="transverseTop font-20 hightBackColor">顶部导航</div>
            <div class="transverseBottom">
                <div class="leftContentBottom backColor font-14">内容区width</div>
            </div>
        </div>
        <div class="Titles font-20">Flex 布局</div>
        <div class="summaryContent font-14">flex布局也叫“弹性布局”，增加div模型使用灵活性。<span class="font-14" style="color:#fea514">（col必须放在row里面。row设置flex属性后，子元素的float、clear和vertical-align
属性将失效）</span></div>
        <div class="transverse-layout"></div>
        <div class="layout-desc font-14">
            容器默认存在两根轴：水平主轴（main axis）和垂直的交叉轴（cross axis）。主轴的开
            始位置（与边框的交叉点）叫做main start，结束位置叫做main end；交叉轴的开始位置
            叫做cross start，结束位置叫做cross end。项目默认沿主轴排列。单个项目占据的主轴空
            间叫做main size，占据的交叉轴空间叫做cross size。
        </div>
        <div class="vertical font-18">示例</div>
        <div class="transverse" style="height:30%!important">
            <Card style="width:100%;height:100%">
                <p slot="title">基础布局</p>
                <div class="Examples">
                    <div class="Basics-layout">
                        <div class="Basics-layout-items hightBackColor">col-6</div>
                        <div class="Basics-layout-items lightBackColor">col-6</div>
                        <div class="Basics-layout-items hightBackColor">col-6</div>
                        <div class="Basics-layout-items lightBackColor">col-6</div>
                    </div>
                </div>
            </Card>
        </div>
        <div class="transverse" style="height:133%!important;margin-top:33px">
            <Card style="width:100%;height:100%">
                <div class="Examples-flex">
                    <li class="Basics-tips-flex font-14">子元素向左排列</li>
                    <div class="Basics-layout-flex">
                        <div class="Basics-layout-items-flex hightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex lightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex hightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex lightBackColor">col-4</div>
                    </div>
                </div>
                <div class="Examples-flex">
                    <li class="Basics-tips-flex font-14">子元素向右排列</li>
                    <div class="Basics-layout-flex">
                        <div class="Basics-layout-items-flex float-right hightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex float-right lightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex float-right hightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex float-right lightBackColor">col-4</div>
                    </div>
                </div>
                <div class="Examples-flex">
                    <li class="Basics-tips-flex font-14">子元素居中排列</li>
                    <div class="Basics-layout-flex">
                        <div class="Basics-layout-items-flex  greyColor"></div>
                        <div class="Basics-layout-items-flex  hightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex  lightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex  hightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex  lightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex  greyColor"></div>
                    </div>
                </div>
                <div class="Examples-flex">
                    <li class="Basics-tips-flex font-14">子元素等宽排列</li>
                    <div class="Basics-layout-flex">
                        <div class="Basics-layout-items-flex  hightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex Equal-width  lightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex Equal-width hightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex Equal-width lightBackColor">col-4</div>
                    </div>
                </div>
                <div class="Examples-flex">
                    <li class="Basics-tips-flex font-14">子元素分散排列</li>
                    <div class="Basics-layout-flex">
                        <div class="Basics-layout-items-flex dispersed hightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex dispersed  lightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex dispersed hightBackColor">col-4</div>
                        <div class="Basics-layout-items-flex dispersed lightBackColor">col-4</div>
                    </div>
                </div>
                <p slot="title">flex 布局</p>
            </Card>
        </div>
        <div class="transverse" style="height:103%!important;margin-top:33px">
            <Card style="width:100%;height:100%">
                <div class="Examples-alignment">
                    <li class="Basics-tips-alignment font-14">顶部对齐</li>
                    <div class="Basics-layout-alignment">
                        <div class="Basics-layout-items-alignment  greyColor"></div>
                        <div class="Basics-layout-items-alignment hightBackColor" style="height:88.666666%!important">
                            col-4
                        </div>
                        <div class="Basics-layout-items-alignment lightBackColor">col-4</div>
                        <div class="Basics-layout-items-alignment hightBackColor" style="height:100%!important">col-4
                        </div>
                        <div class="Basics-layout-items-alignment lightBackColor"  style="height:66.6666%!important">col-4</div>
                        <div class="Basics-layout-items-alignment  greyColor"></div>
                    </div>
                </div>
                <div class="Examples-alignment">
                    <li class="Basics-tips-alignment font-14">居中对齐</li>
                    <div class="Basics-layout-alignment">
                        <div class="Basics-layout-items-alignment  greyColor"></div>
                        <div class="Basics-layout-items-alignment hightBackColor" style="height:88.666666%!important;margin-top:17.5px">
                            col-4
                        </div>
                        <div class="Basics-layout-items-alignment center lightBackColor">col-4</div>
                        <div class="Basics-layout-items-alignment hightBackColor" style="height:100%!important">col-4
                        </div>
                        <div class="Basics-layout-items-alignment lightBackColor" style="height:66.6666%!important;margin-top:50px">col-4</div>
                        <div class="Basics-layout-items-alignment  greyColor"></div>
                    </div>
                </div>
                <div class="Examples-alignment">
                    <li class="Basics-tips-alignment font-14">底部对齐</li>
                     <div class="Basics-layout-alignment">
                        <div class="Basics-layout-items-alignment  greyColor"></div>
                        <div class="Basics-layout-items-alignment hightBackColor" style="height:88.666666%!important;margin-top:17px">
                            col-4
                        </div>
                        <div class="Basics-layout-items-alignment lightBackColor" style="margin-top:100px">col-4</div>
                        <div class="Basics-layout-items-alignment hightBackColor" style="height:100%!important">col-4
                        </div>
                        <div class="Basics-layout-items-alignment lightBackColor" style="height:66.6666%!important;margin-top:50px">col-4</div>
                        <div class="Basics-layout-items-alignment  greyColor"></div>
                    </div>
                </div>
                <p slot="title">flex 对齐</p>
            </Card>
        </div>
    </div>
</template>

<script>

    export default {
        name: 'layout'
    }
</script>

<style scoped lang="scss">
    #grid {
        width: 100%;
        height: 100%;
        overflow-y: auto;

        .Titles {
            height: 40px;
            width: 100%;
            line-height: 30px;
        }

        .transverse-layout {
            width: 100%;
            height: 70%;
            margin-top: 33px;
            background: url("../../assets/base/img/layout.svg") no-repeat;
            background-size: contain;
        }

        .layout-desc {
            width: 100%;
            height: 10%;
            margin-top: 12px;
        }

        .summary {
            height: 40px;
            width: 100%;
            line-height: 20px;
            margin-top: 10px;
        }

        .vertical {
            height: 40px;
            width: 100%;
            line-height: 20px;
            margin-top: 20px;
        }

        .transverse {
            width: 100%;
            height: 70%;

            .Examples-alignment {
                width: calc(100% - 16px);
                margin-left: 16px;
                height: 170px;
                margin-top: 16px;

                .Basics-tips-alignment {
                    width: 100%;
                    height: 20px;
                    line-height: 20px;
                    margin-top: 10px;
                }

                .Basics-layout-alignment {
                    margin-left: 16px;
                    margin-top: 10px;
                    width: calc(100% - 16px);
                    background-color: #e6e6e6;
                    height: 150px;

                    .Basics-layout-items-alignment {
                        width: 16.6666667%;
                        text-align: center;
                        line-height: 50px;
                        color: #ffffff;
                        font-size: 16px;
                        height: 33.3333333%;
                        float: left;
                    }

                    .center {
                        margin-top: 100px;
                    }

                    .dispersed {
                        margin-left: 7.33333%;
                    }

                    .Equal-width {
                        margin-left: 11.1111111%;
                    }
                }
            }

            .Examples-flex {
                width: calc(100% - 16px);
                margin-left: 16px;
                height: 140px;
                margin-top: 16px;

                .Basics-tips-flex {
                    width: 100%;
                    height: 20px;
                    line-height: 20px;
                    margin-top: 10px;
                }

                .Basics-layout-flex {
                    margin-left: 16px;
                    margin-top: 10px;
                    width: calc(100% - 16px);
                    background-color: #e6e6e6;
                    height: 50px;

                    .Basics-layout-items-flex {
                        width: 16.6666667%;
                        text-align: center;
                        line-height: 50px;
                        color: #ffffff;
                        font-size: 16px;
                        height: 100%;
                        float: left;
                    }

                    .dispersed {
                        margin-left: 7.33333%;
                    }

                    .Equal-width {
                        margin-left: 11.1111111%;
                    }
                }
            }

            .Examples {
                width: calc(100% - 16px);
                margin-left: 16px;
                height: 100px;

                .Basics-tips {
                    width: 100%;
                    height: 20px;
                    line-height: 20px;
                    margin-top: 10px;
                }

                .Basics-layout {
                    margin-left: 16px;
                    margin-top: 10px;
                    width: calc(100% - 16px);
                    height: 50px;

                    .Basics-layout-items {
                        width: 25%;
                        text-align: center;
                        line-height: 50px;
                        color: #ffffff;
                        font-size: 16px;
                        height: 100%;
                        float: left;
                    }
                }
            }

            .photo {
                vertical-align: middle;
                display: inline-block;
                width: 100%;
                height: 100%;
            }

            .transverseTop {
                width: 100%;
                color: #ffffff;
                text-align: center;
                line-height: 60px;
                height: 60px;
            }

            .transverseContentleft {
                width: 216px;
                height: 4%;
                float: left;
            }

            .transverseContent {
                width: calc(100% - 248px);
                margin-left: 16px;
                margin-right: 16px;
                text-align: center;
                float: right;
                height: 4%;
                line-height: 35px;
            }

            .verticalContentText {
                width: calc(100% - 248px);
                margin-left: 16px;
                margin-right: 16px;
                text-align: center;
                height: 10%;
                line-height: 35px;
            }

            .transverseBottom {
                width: 100%;
                height: 300px;

                .leftNavigation {
                    width: 216px;
                    text-align: center;
                    color: #ffffff;
                    line-height: 300px;
                    float: left;
                    height: 100%;
                }

                .leftContentBottom {
                    width: 100%;
                    height: 100%;
                    display: inline-block;
                    color: #ffffff;
                    text-align: center;
                    line-height: 300px;
                    float: left;
                }

                .leftContent {
                    width: calc(100% - 216px);
                    height: 100%;
                    display: inline-block;
                    color: #ffffff;
                    text-align: center;
                    line-height: 300px;
                    float: left;

                    .content100 {
                        width: 100%;
                        line-height: 45px;
                        height: calc(25% - 20px);
                    }

                    .contentItem {
                        width: 100%;
                        height: calc(25% - 20px);
                        margin-top: 26px;

                        .contentSty {
                            float: left;
                            height: 100%;
                            line-height: 50px;
                        }

                        .content-50-left {
                            width: calc(50% - 8px);
                        }

                        .content-50-right {
                            width: calc(50% - 8px);
                            margin-left: 16px;
                        }

                        .content-33-left {
                            width: calc(33.33% - 10.66px);;
                        }

                        .content-33-center {
                            width: calc(33.33% - 10.66px);;
                            margin-left: 16px;
                        }

                        .content-33-right {
                            width: calc(33.33% - 10.66px);;
                            margin-left: 16px;
                        }

                        .content-25-left {
                            width: calc(25% - 12px);;
                        }

                        .content-25-left-center {
                            width: calc(25% - 12px);;
                            margin-left: 16px;
                        }

                        .content-25-right {
                            width: calc(25% - 12px);;
                            margin-left: 16px;
                        }
                    }
                }
            }
        }

        .tipSty {
            width: 100%;
            margin-top: 16px;
            height: 80px;
            line-height: 35px;
        }

        .rule {
            width: 100%;
            margin-top: 16px;
            margin-bottom: 16px;
            height: 80px;
            line-height: 35px;
        }

        .formula {
            width: 100%;
            margin-top: 16px;
            height: 65px;
            line-height: 35px;
        }
    }
</style>
<style scoped>
    .backColor {
        background-color: #88c4ff;
    }

    .float-right {
        float: right !important;
    }

    .lightBackColor {
        background-color: #b0d7ff;
    }

    .greyColor {
        background-color: #e6e6e6;
    }

    .hightBackColor {
        background-color: #399CFF;
    }

    .textSty {
        text-align: center;
        font-size: 14px;
        color: #ffffff;
    }
</style>
