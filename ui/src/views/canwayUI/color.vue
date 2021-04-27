<template>
    <div id="color">
        <div class="Titles font-20">Color 色彩</div>
        <div class="summary font-18">概述</div>
        <div class="summaryContent font-14">推荐使用以下调色板的颜色作为设计和开发规范，以保证页面和组件之间视觉一致</div>
        <div class="mainColor">
            <div class="mainColor-title font-18">主色</div>
            <div class="mainColor-describe font-14">嘉为蓝鲸平台SaaS采用较为安全、科技的蓝色作为主色调。二层颜色可用于不同场景辅助。</div>
            <div class="mainColor-content">
                <div class="contentitems mainLight">
                    <div class="itemType">Light</div>
                    <div class="itemRGB">#61B0FF</div>
                </div>
                <div class="SecondSty">
                    <div class="contentitems mainPrimary">
                        <div class="itemType">Primary</div>
                        <div class="itemRGB">#399CFF</div>
                    </div>
                    <div class="sccondfloor">
                        <div class="sccondfloor-item radiusStyleft primaryleft"></div>
                        <div class="sccondfloor-item primarycenter"></div>
                        <div class="sccondfloor-item primaryCenterRight"></div>
                        <div class="sccondfloor-item radiusStyRight primaryright"></div>
                    </div>
                </div>
                <div class="contentitems mainDark">
                    <div class="itemType">Dark</div>
                    <div class="itemRGB">#0D90FC</div>
                </div>
            </div>
        </div>
        <div class="mainColor">
            <div class="mainColor-title font-18">辅助色</div>
            <div class="mainColor-describe font-14">除主色外的场景色，具有代表性。常用于信息提示，比如成功、警告、失败。二层色值从左到右依次应用于
                toast信息窗:背景框描边、背景色。
            </div>
            <div class="mainColor-content">
                <div class="SecondSty width-25">
                    <div class="contentitems auxiliaryInfo">
                        <div class="itemType">Info</div>
                        <div class="itemRGB">#40C6EF</div>
                    </div>
                    <div class="sccondfloor" style="display: flex">
                        <div class="dis-three radiusStyleft info-hover"></div>
                        <div class="dis-three info-border"></div>
                        <div class="dis-three radiusStyRight info-back"></div>
                    </div>
                </div>
                <div class="SecondSty width-25">
                    <div class="contentitems auxiliarySuccess">
                        <div class="itemType">Success</div>
                        <div class="itemRGB">#3DE586</div>
                    </div>
                    <div class="sccondfloor" style="display: flex">
                        <div class="dis-three radiusStyleft success-hover"></div>
                        <div class="dis-three success-border"></div>
                        <div class="dis-three radiusStyRight success-back"></div>
                    </div>
                </div>
                <div class="SecondSty width-25">
                    <div class="contentitems auxiliaryWarning">
                        <div class="itemType">Warning</div>
                        <div class="itemRGB">#FEA30D</div>
                    </div>
                    <div class="sccondfloor" style="display: flex">
                        <div class="dis-three radiusStyleft warn-hover"></div>
                        <div class="dis-three warn-border"></div>
                        <div class="dis-three radiusStyRight warn-back"></div>
                    </div>
                </div>
                <div class="SecondSty width-25">
                    <div class="contentitems auxiliaryError">
                        <div class="itemType">Error</div>
                        <div class="itemRGB">#ED3F3F</div>
                    </div>
                    <div class="sccondfloor" style="display: flex">
                        <div class="dis-three radiusStyleft error-hover"></div>
                        <div class="dis-three error-border"></div>
                        <div class="dis-three radiusStyRight error-back"></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="mainColor" style="margin-top:20px">
            <div class="mainColor-title font-18">中性色</div>
            <div class="mainColor-describe font-14">
                中性色常用于文本、背景、边框、阴影等，可以体现出页面的层次结构。
            </div>
            <div class="mainColor-content">
                <div class="SecondSty width-25">
                    <div class="contentitems MainCharacters">
                        <div class="itemType">主要文字/标题</div>
                        <div class="itemRGB">#282A2B</div>
                    </div>
                </div>
                <div class="SecondSty width-25">
                    <div class="contentitems GeneralText">
                        <div class="itemType">常规文字/正文</div>
                        <div class="itemRGB">#5F6568</div>
                    </div>
                </div>
                <div class="SecondSty width-25">
                    <div class="contentitems SecondaryText">
                        <div class="itemType">次要文字</div>
                        <div class="itemRGB">#888E94</div>
                    </div>
                </div>
                <div class="SecondSty width-25">
                    <div class="contentitems PlaceholderText">
                        <div class="itemType">占位文字/失效</div>
                        <div style="color:#e2e4e6" class="itemRGB">#C5CACF</div>
                    </div>
                </div>
                <div class="SecondSty width-25">
                    <div class="contentitems BorderText">
                        <div style="color:#727171" class="itemType">边框 Border</div>
                        <div style="color:#9b9c9e" class="itemRGB">#DADEE2</div>
                    </div>
                </div>
                <div class="SecondSty width-25">
                    <div class="contentitems DividingLine">
                        <div style="color:#727171" class="itemType">分割线</div>
                        <div style="color:#a0a1a3" class="itemRGB">#E7EBEE</div>
                    </div>
                </div>
                <div class="SecondSty width-25">
                    <div class="contentitems backgroundColor">
                        <div style="color:#595757" class="itemType">背景</div>
                        <div style="color:#959596" class="itemRGB">#EFF2F5</div>
                    </div>
                </div>
                <div class="SecondSty width-25">
                    <div class="contentitems AuxiliaryBackground">
                        <div style="color:#727171" class="itemType">辅助背景</div>
                        <div style="color:#a7a7a7" class="itemRGB">#F7F8F9</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'color'
    }
</script>

<style scoped lang="scss">
    #color {
        width: 100%;
        height: 100%;
        overflow-y: auto;

        .info-hover {
            background-color: $info-hover;
        }

        .info-border {
            background-color: $info-border;
        }

        .info-back {
            background-color: $info-back;
        }

        .success-hover {
            background-color: $success-hover;
        }

        .success-border {
            background-color: $success-border;
        }

        .success-back {
            background-color: $success-back;
        }

        .warn-hover {
            background-color: $warn-hover;
        }

        .warn-border {
            background-color: $warn-border;
        }

        .warn-back {
            background-color: $warn-back;
        }

        .error-hover {
            background-color: $error-hover;
        }

        .error-border {
            background-color: $error-border;
        }

        .error-back {
            background-color: $error-back;
        }


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

        .mainColor {
            width: 100%;
            height: 40%;

            .mainColor-title {
                height: 15%;
                width: 100%;
                line-height: 30px;
            }

            .mainColor-describe {
                height: 15%;
                width: calc(100% - 5px);
                line-height: 30px;
                margin-left: 5px;
            }

            .mainColor-content {
                height: 60%;
                width: calc(100% - 5px);
                line-height: 30px;
                margin-left: 5px;

                .SecondSty {
                    width: calc(33.33% - 10px);
                    margin-right: 10px;
                    display: inline-block;
                    height: 100%;

                    .sccondfloor {
                        width: 100%;
                        height: 38%;

                        .sccondfloor-item {
                            width: 25%;
                            height: calc(100% - 10px);
                            float: left;
                        }

                        .dis-three {
                            flex: 1;
                            height: calc(100% - 10px);
                        }
                    }

                    .contentitems {
                        width: 100%;
                        border-radius: 4px;
                        display: inline-block;
                        height: 80px;
                        margin-top: 10px;
                    }
                }

                .contentitems {
                    width: calc(33.33% - 13.67px);
                    border-radius: 4px;
                    margin-right: 10px;
                    display: inline-block;
                    height: 80px;
                    margin-top: 10px;

                    .itemType {
                        color: #ffffff;
                        font-size: 18px;
                        margin-left: 10px;
                        width: calc(100% - 10px);
                        margin-top: 10px;
                    }

                    .itemRGB {
                        color: #ffffff;
                        width: calc(100% - 10px);
                        margin-left: 10px;
                        font-size: 14px;
                    }

                    /*background-color: #61B0FF;*/
                }
            }
        }
    }
</style>
<style scoped>
    .backColor {
        background-color: #61B0ff;
    }

    .transversevertical {
        height: 45% !important;
    }

    .width-25 {
        width: calc(25% - 13px) !important;
    }

    .primaryleft {
        background-color: #94c4fa;
    }

    .primarycenter {
        background-color: #b7d7fb;
    }

    .primaryCenterRight {
        background-color: #daebfd;
    }

    .primaryright {
        background-color: #edf5fe;
    }

    .auxiliaryInfo {
        background-color: #40C6EF;
    }

    .auxiliarySuccess {
        background-color: #3DE586;
    }

    .auxiliarySuccess-left {
        background-color: #def6e8;
    }

    .auxiliarySuccess-right {
        background-color: #eefaf3;
    }

    .auxiliaryInfo-left {
        background-color: #d8f4ff;
    }


    .auxiliaryInfo-right {
        background-color: #ebf9ff;
    }


    .auxiliaryWarning {
        background-color: #FEA30D;
    }

    .auxiliaryWarning-left {
        background-color: #ffedcf;
    }

    .auxiliaryWarning-right {
        background-color: #fdf5e6;
    }

    .auxiliaryError {
        background-color: #ED3F3F;
    }

    .auxiliaryError-left {
        background-color: #fbd9d9;
    }

    .auxiliaryError-right {
        background-color: #fdebeb;
    }

    .mainLight {
        background-color: #61B0FF;
    }

    .radiusStyleft {
        border-top-left-radius: 4px;
        border-bottom-left-radius: 4px;
    }

    .radiusStyRight {
        border-top-right-radius: 4px;
        border-bottom-right-radius: 4px;
    }

    .mainPrimary {
        background-color: #399CFF;
    }

    .mainDark {
        background-color: #0D90FC;
    }

    .MainCharacters {
        background-color: #282A2B;
    }

    .GeneralText {
        background-color: #5F6568;
    }

    .SecondaryText {
        background-color: #888E94;
    }

    .PlaceholderText {
        background-color: #C5CACF;
    }

    .BorderText {
        background-color: #DADEE2;
    }

    .DividingLine {
        background-color: #E7EBEE;
    }

    .backgroundColor {
        background-color: #EFF2F5;
    }

    .AuxiliaryBackground {
        background-color: #F7F8F9;
        color: black;
    }

    .textSty {
        text-align: center;
        font-size: 14px;
        color: #ffffff;
    }
</style>
