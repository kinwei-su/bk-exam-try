<template>
    <div id="font">
        <div class="Titles font-20">Font 字体</div>
        <div class="summary font-18">概述</div>
        <div class="summaryContent font-14">字体大小使用以下规范，不随屏幕分辨率改变而变化。行高要求：在网页开发时在
            body全局元素里对行高
            reset，保证兼容性。行高在原字体大小基础上增加8px，如辅助文字大小12px，行高line-height：20px。
        </div>
        <div class="summaryContent font-16">字体预览
        </div>
        <div class="fontSty">
            <div class="chineseFont">
                <div class="chineseFont-title font-14">
                    <li>中文字体</li>
                </div>
                <div class="chineseContent">
                    <div class="chineseContent-item">
                        <div class="mainFont PingFang">用数据说话</div>
                        <div class="mainFontfamily PingFang">PingFang SC</div>
                        <div class="mainFontdesc PingFang">优先字体</div>
                    </div>
                    <div class="chineseContent-item">
                        <div class="mainFont Source">用数据说话</div>
                        <div class="mainFontfamily Source">Source Han Sans</div>
                        <div class="mainFontdesc Source">备用字体</div>
                    </div>
                    <div class="chineseContent-item">
                        <div class="mainFont Microsoft">用数据说话</div>
                        <div class="mainFontfamily Microsoft">Microsoft YaHei</div>
                        <div class="mainFontdesc Microsoft">次级备用字体</div>
                    </div>
                </div>
            </div>
            <div class="chineseFont">
                <div class="chineseFont-title font-14">
                    <li>英文字体</li>
                </div>
                <div class="chineseContent">
                    <div class="chineseContent-item">
                        <div class="mainFont HelveticaNeue">Aa</div>
                        <div class="mainFontfamily HelveticaNeue">Helvetica Neue</div>
                        <div class="mainFontdesc HelveticaNeue">优先字体</div>
                    </div>
                    <div class="chineseContent-item">
                        <div class="mainFont Helvetica">Aa</div>
                        <div class="mainFontfamily Helvetica">Helvetica</div>
                        <div class="mainFontdesc Helvetica">备用字体</div>
                    </div>
                    <div class="chineseContent-item">
                        <div class="mainFont Arial">Aa</div>
                        <div class="mainFontfamily Arial">Arial</div>
                        <div class="mainFontdesc Arial">次级备用字体</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="useSpecification">
            <div class="useSpecification-tips">
                <div class="useSpecification-tips-left font-16">字号：</div>
                <div class="useSpecification-tips-right font-14">字体加粗字重font-weight：600。</div>
            </div>
            <Table :columns="columns1" :data="data1"></Table>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'font',
        data() {
            return {
                columns1: [
                    {
                        title: '层级',
                        key: 'Hierarchy'
                    },
                    {
                        title: '字体大小',
                        key: 'fontsize'
                    },
                    {
                        title: '粗细',
                        key: 'thickness'
                    },
                    {
                        title: '举例',
                        key: 'example',
                        render: (h, params) => {
                            let texts = ''; //表格列显示文字大小
                            let fontcolor = '5F6568'; //表格文字颜色
                            if (params.row.Hierarchy === '特大标题') {
                                texts = '32px'
                                fontcolor = '#282A2B'
                            } else if (params.row.Hierarchy === '主标题') {
                                texts = '20px'
                                fontcolor = '#282A2B'
                            } else if (params.row.Hierarchy === '标题') {
                                texts = '18px'
                                fontcolor = '#282A2B'
                            } else if (params.row.Hierarchy === '小标题') {
                                texts = '16px'
                                fontcolor = '#282A2B'
                            } else if (params.row.Hierarchy === '正文') {
                                texts = '14px'
                            } else if (params.row.Hierarchy === '正文(小)') {
                                texts = '13px'
                            } else if (params.row.Hierarchy === '辅助文字') {
                                texts = '12px'
                                fontcolor = '#C5CACF'
                            }
                            return h('div', {
                                style: {
                                    fontSize: texts,
                                    color: fontcolor,
                                }
                            }, params.row.example);
                        }
                    }
                ],
                data1: [
                    {
                        'Hierarchy': '特大标题', 'fontsize': '32px', 'thickness': '默认/加粗', 'example': '我是特大标题'
                    }, {
                        'Hierarchy': '主标题', 'fontsize': '20px', 'thickness': '默认/加粗', 'example': '我是主标题'
                    }, {
                        'Hierarchy': '标题', 'fontsize': '18px', 'thickness': '默认/加粗', 'example': '我是标题'
                    }, {
                        'Hierarchy': '小标题', 'fontsize': '16px', 'thickness': '默认/加粗', 'example': '我是小标题'
                    }, {
                        'Hierarchy': '正文', 'fontsize': '14px', 'thickness': '默认', 'example': '我是正文'
                    }, {
                        'Hierarchy': '正文(小)', 'fontsize': '13px', 'thickness': '默认', 'example': '我是小正文'
                    }, {
                        'Hierarchy': '辅助文字', 'fontsize': '12px', 'thickness': '默认', 'example': '提示：失效文字'
                    }
                ],
            }
        },
    }
</script>

<style scoped lang="scss">
    #font {
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

        .summaryContent {
            height: 40px;
            width: 100%;
            margin-left: 5px;
            line-height: 20px;
            margin-top: 10px;
        }

        .fontSty {
            height: 60%;
            width: 100%;
            margin-left: 5px;
            line-height: 20px;
            margin-top: 10px;

            .chineseFont {
                height: 50%;
                width: 100%;

                .chineseFont-title {
                    width: calc(100% - 16px);
                    margin-left: 16px;
                    height: 30px;
                }

                .chineseContent {
                    height: calc(100% - 30px);
                    width: 100%;

                    .chineseContent-item {
                        width: calc(33.33% - 16px);
                        height: 100%;
                        float: left;
                        text-align: center;
                        margin-right: 16px;

                        .mainFont {
                            font-size: 56px;
                            height: 68px;
                            line-height: 68px;
                            color: #474c5a;
                        }

                        .mainFontfamily {
                            font-size: 16px;
                            height: 26px;
                            line-height: 26px;
                            color: #acaab6;
                            margin-top: 10px;
                        }

                        .mainFontdesc {
                            font-size: 16px;
                            height: 37px;
                            color: #acaab6;
                            margin-top: 10px;
                            line-height: 37px;
                        }
                    }
                }
            }
        }

        .useSpecification {
            .useSpecification-tips {
                height: 10%;
                /*border: 1px solid;*/
                width: 100%;

                .useSpecification-tips-left {
                    height: 100%;
                    float: left;
                    font-weight: 600;
                    line-height: 24px;
                }

                .useSpecification-tips-right {
                    float: left;
                    line-height: 24px;
                    height: 100%;
                    font-weight: 600;
                }
            }

            height: 60%;
            width: 100%;
            margin-left: 5px;
            margin-top: 10px;
        }
    }
</style>
<style scoped>
    .backColor {
        background-color: #61B0ff;
    }

    .textSty {
        text-align: center;
        font-size: 14px;
        color: #ffffff;
    }
</style>
