<template>
    <div id="grid">
        <div class="Titles font-20">Icon 图标</div>
        <div class="summary font-18">概述</div>
        <div class="summaryContent font-14">为保证视觉效果与美观，要求默认图标可点击热区比实际大小要多8px/4px/2px。图标建议使用矢量图标文字库或svg格式
            文件，防止图标失真模糊。可参考view UI图标库。
        </div>
        <div class="transverse">
        </div>
        <div class="transverse-Inco">
            <div class="icon-Tips font-14">
                如大小为16px*16px的图标，图形不规则时可适当调整大小。可点击热区为24*24px。
            </div>
            <div class="icon-24px img-24">
            </div>
            <div class="icon-24px">
                <Icon type="ios-expand"/>
            </div>
            <div class="icon-24px">
                <Icon type="ios-browsers-outline"/>
            </div>
            <div class="icon-24px">
                <Icon type="ios-redo-outline"/>
            </div>
            <div class="icon-24px">
                <Icon type="ios-close-circle-outline"/>
            </div>
            <div class="icon-24px">
                <Icon type="ios-heart-outline"/>
            </div>
            <div class="icon-24px">
                <Icon type="ios-checkmark-circle-outline"/>
            </div>
            <div class="icon-24px">
                <Icon type="ios-search-outline"/>
            </div>
        </div>
        <div class="icon-Size-sty font-14">建议使用图标大小：</div>
        <div class="icon-Size-sty font-14">80px*80px、</div>
        <div class="icon-Size-sty font-14">40px*40px、</div>
        <div class="icon-Size-sty font-14">32px*32px、</div>
        <div class="icon-Size-sty font-14">20px*20px、</div>
        <div class="icon-Size-sty font-14">16px*16px、</div>
        <div class="icon-Size-sty font-14">12px*12px （图标大小仅参考）</div>
        <div class="icon-Size-sty font-14">不够地方用透明补全。长宽不相等时，可适当增加宽度或高度使图标在视觉上大小统一。</div>
    </div>
</template>

<script>
    export default {
        name: 'icon'
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

        .icon-Size-sty {
            height: 25px;
            width: 100%;
            line-height: 20px;
            margin-top: 2px;
        }

        .transverse {
            margin-left: 4px;
            /*border: 1px solid red;*/
            width: 61%;
            background: url("../../assets/base/img/icons.svg") no-repeat;
            background-size: contain;
            height: 88px !important;

            .transverseIcons {
                width: 25%;
                height: 50%;
                float: left;
            }
        }

        .transverse-Inco {
            margin-left: 4px;
            width: 100%;
            height: 20% !important;

            .icon-Tips {
                width: 100%;
                height: 40px;
                margin-top: 32px;
                line-height: 40px;
            }

            .icon-24px {
                width: 5%;
                height: 24px;
                font-size: 24px;
                margin-top: 22px;
                line-height: 18px;
                float: left;
            }

            .img-24 {
                background: url("../../assets/base/img/icon24PX.svg") no-repeat;
                background-size: 100% 100%;
            }
        }

        .vertical {
            height: 40px;
            width: 100%;
            line-height: 20px;
            margin-top: 20px;
        }

        .summaryContent {
            height: 40px;
            width: 100%;
            margin-left: 5px;
            line-height: 20px;
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
