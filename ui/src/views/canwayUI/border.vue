<template>
    <div id="button" class="PingFang">
        <div class="Titles font-20">Border 边框</div>
        <div class="summary font-18">概述</div>
        <div class="summaryContent font-14">边框用于按钮、卡片、弹窗等组件里。
        </div>
        <div class="transverse">
            <Card style="width:100%;height:100%">
                <div slot="title">
                    <div style="font-size:16px">边框
                    </div>
                </div>
                <div class="border-table">
                    <div class="border-name">名称</div>
                    <div class="border-size">粗细</div>
                    <div class="border-example">举例</div>
                </div>
                <div class="border-table">
                    <div class="border-name">实线</div>
                    <div class="border-size">1px</div>
                    <div class="border-example">
                        <div class="border-example-solid"></div>
                    </div>
                </div>
                <div class="border-table">
                    <div class="border-name">虚线</div>
                    <div class="border-size">1px</div>
                    <div class="border-example">
                        <div class="border-example-dashed"></div>
                    </div>
                </div>
            </Card>
        </div>
        <div class="transverse">
            <Card style="width:100%;height:100%">
                <div slot="title">
                    <div style="font-size:16px">圆角
                    </div>
                </div>
                <div class="border-radios">
                    默认圆角:
                    <br><br>
                    Border-radius:4px
                    <div class="border-radios4">
                    </div>
                </div>
                <div class="border-radios">
                    小圆角:
                    <br><br>
                    Border-radius:3px
                    <div class="border-radios3">
                    </div>
                </div>
            </Card>
        </div>
        <div class="transverse">
            <Card style="width:100%;height:100%">
                <div slot="title">
                    <div style="font-size:16px">投影
                    </div>
                </div>
                <div class="border-radios">
                    基础投影:
                    <br><br>
                    0 2px 6px rgba(0,0,0,0.12)
                    <div class="border-radios4" style="box-shadow:  0 2px 6px rgba(0,0,0,0.12);border:none">
                    </div>
                </div>
                <div class="border-radios">
                    彩色投影:
                    <br><br>
                    0 2px 6px rgba(57,156,255,0.12)
                    <div class="border-radios3" style="box-shadow:  0 2px 6px rgba(57,156,255,0.12);border:none">
                    </div>
                </div>
                <div class="border-radios">
                    弹窗投影:
                    <br><br>
                    0 0px 8px rgba(0,0,0,0.26)
                    <div class="border-radios3" style="box-shadow:  0 0px 8px rgba(0,0,0,0.26);border:none">
                    </div>
                </div>
            </Card>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'border'
    }
</script>

<style scoped lang="scss">
    #button {
        width: 100%;
        height: 100%;
        overflow-y: auto;
        color: $font-second;

        .Titles {
            height: 40px;
            width: 100%;
            line-height: 30px;
            color: $font-color;
        }

        .summary {
            height: 40px;
            width: 100%;
            line-height: 20px;
            margin-top: 10px;
        }

        .BtnTypes {
            width: 100%;
            height: 30%;
            margin-top: 16px;
        }

        .summaryContent {
            height: 40px;
            width: 100%;
            margin-left: 5px;
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
            margin-bottom: 32px;
            height: 40%;

            .border-radios {
                font-size: 20px;
                float: left;
                width: 25%;
                height: 100%;
                margin-left: 40px;

                .border-radios4 {
                    width: 200px;
                    height: 40px;
                    border: 1px solid $border-color;
                    border-radius: 4px;
                    margin-top: 10px
                }

                .border-radios3 {
                    width: 200px;
                    height: 40px;
                    border: 1px solid $border-color;
                    margin-top: 10px;
                    border-radius: 3px;
                }
            }

            .border-table {
                height: 40px;
                border-bottom: 1px solid $border-color;
                width: 100%;
                margin-bottom: 20px;

                .border-name {
                    text-align: center;
                    font-size: 22px;
                    width: 20%;
                    float: left;
                }

                .border-size {
                    text-align: center;
                    font-size: 22px;
                    width: 20%;
                    float: left;
                }

                .border-example {
                    text-align: center;
                    font-size: 22px;
                    width: 60%;
                    float: left;

                    .border-example-solid {
                        text-align: center;
                        height: 10px;
                        border-bottom: 1px solid $border-color;
                    }

                    .border-example-dashed {
                        text-align: center;
                        height: 10px;
                        border-bottom: 1px dashed $border-color;
                    }
                }
            }
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
