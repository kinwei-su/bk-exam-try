<template>
    <div id="grid">
        <div class="Titles font-20">Grid 栅格</div>
        <Card style="width: 100%;height: 70%;">
            <img src="../../assets/base/img/grid.svg">
        </Card>
<!--        <div class="transverse transversevertical">-->
<!--            </div>-->
        <div class="tipSty PingFang font-14">
            嘉为蓝鲸SaaS目前分两种布局方式: 均按全屏分辨率大小布局展示;分割的 布局按24栅格划分。以8为原子单位 (以8n为单位分布、间隔)。 侧边导航固定宽度:<span
            style="color:#0085e7">216px</span>，内容区左
            右两边安全距离<span style="color:#0085e7">16px</span>。侧边导航收起时宽度<span style="color:#0085e7">64px</span>，图标位置刚好居中。
        </div>
        <div class="formula PingFang font-14">
            栅格计算公式<span style="color:#99aab0">(以分辨率1366*768px为例)</span>
            <div>(a+i)*24-i=W</div>
        </div>
        <div class="rule PingFang font-14">
            内容宽度以导航位置不定 每个栅格 a:32/40px 间隔 i:16px
        </div>
    </div>
</template>

<script>

    export default {
        name: 'grid'
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
            background: url("../../assets/base/img/grid.svg") no-repeat;
            background-size: 100% 100%;

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
                line-height: 100px;
                height: 25%;
            }

            .transverseContentleft {
                width: 216px;
                height: 8%;
                float: left;
            }

            .transverseContent {
                width: calc(100% - 248px);
                margin-left: 16px;
                margin-right: 16px;
                text-align: center;
                float: right;
                height: 8%;
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

            .verticalContent {
                height: 90%;
                width: calc(100% - 32px);
                margin-left: 16px;
                margin-right: 16px;
                background-image: linear-gradient(90deg, #f5f5f5 4.16666667%, transparent 0, transparent 8.33333333%, #f5f5f5 0, #f5f5f5 12.5%, transparent 0, transparent 16.66666667%, #f5f5f5 0, #f5f5f5 20.83333333%, transparent 0, transparent 25%, #f5f5f5 0, #f5f5f5 29.16666667%, transparent 0, transparent 33.33333333%, #f5f5f5 0, #f5f5f5 37.5%, transparent 0, transparent 41.66666667%, #f5f5f5 0, #f5f5f5 45.83333333%, transparent 0, transparent 50%, #f5f5f5 0, #f5f5f5 54.16666667%, transparent 0, transparent 58.33333333%, #f5f5f5 0, #f5f5f5 62.5%, transparent 0, transparent 66.66666667%, #f5f5f5 0, #f5f5f5 70.83333333%, transparent 0, transparent 75%, #f5f5f5 0, #f5f5f5 79.16666667%, transparent 0, transparent 83.33333333%, #f5f5f5 0, #f5f5f5 87.5%, transparent 0, transparent 91.66666667%, #f5f5f5 0, #f5f5f5 95.83333333%, transparent 0);

                .vertical100 {
                    width: 100%;
                    line-height: 45px;
                    height: calc(25% - 20px);
                }

                .verticalItem {
                    width: 100%;
                    height: calc(25% - 20px);
                    margin-top: 26px;

                    .verticalSty {
                        float: left;
                        height: 100%;
                        line-height: 50px;
                    }

                    .vertical-50-left {
                        width: calc(50% - 8px);
                    }

                    .vertical-50-right {
                        width: calc(50% - 8px);
                        margin-left: 16px;
                    }

                    .vertical-33-left {
                        width: calc(33.33% - 10.66px);;
                    }

                    .vertical-33-center {
                        width: calc(33.33% - 10.66px);;
                        margin-left: 16px;
                    }

                    .vertical-33-right {
                        width: calc(33.33% - 10.66px);;
                        margin-left: 16px;
                    }

                    .vertical-25-right {
                        width: calc(25% - 8px);;
                    }

                    .vertical-75-right {
                        width: calc(75% - 8px);;
                        margin-left: 16px;
                    }
                }
            }

            .transverseBottom {
                width: 100%;
                height: 67%;

                .leftNavigation {
                    width: 216px;
                    text-align: center;
                    color: #ffffff;
                    line-height: 220px;
                    float: left;
                    height: 100%;
                }

                .leftContent {
                    width: calc(100% - 248px);
                    margin-left: 16px;
                    margin-right: 16px;
                    height: 100%;
                    display: inline-block;
                    float: left;
                    background-image: linear-gradient(90deg, #f5f5f5 4.16666667%, transparent 0, transparent 8.33333333%, #f5f5f5 0, #f5f5f5 12.5%, transparent 0, transparent 16.66666667%, #f5f5f5 0, #f5f5f5 20.83333333%, transparent 0, transparent 25%, #f5f5f5 0, #f5f5f5 29.16666667%, transparent 0, transparent 33.33333333%, #f5f5f5 0, #f5f5f5 37.5%, transparent 0, transparent 41.66666667%, #f5f5f5 0, #f5f5f5 45.83333333%, transparent 0, transparent 50%, #f5f5f5 0, #f5f5f5 54.16666667%, transparent 0, transparent 58.33333333%, #f5f5f5 0, #f5f5f5 62.5%, transparent 0, transparent 66.66666667%, #f5f5f5 0, #f5f5f5 70.83333333%, transparent 0, transparent 75%, #f5f5f5 0, #f5f5f5 79.16666667%, transparent 0, transparent 83.33333333%, #f5f5f5 0, #f5f5f5 87.5%, transparent 0, transparent 91.66666667%, #f5f5f5 0, #f5f5f5 95.83333333%, transparent 0);

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

    .lightBackColor {
        background-color: #b0d7ff;
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
