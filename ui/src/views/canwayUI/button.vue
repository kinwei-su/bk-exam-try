<template>
    <div id="button" class="PingFang">
        <div class="Titles font-20">Button 按钮</div>
        <div class="summary font-18">概述</div>
        <div class="summaryContent font-14">用于一个即时操作，触发业务逻辑时使用。按钮默认使用尺寸高度32px，圆角固定4px，文字大小12px，按钮字
            数一般2-4个为宜。按钮宽度根据实际场景调整，要求文字左右两边最小安全距离16px。
        </div>
        <div class="BtnTypes">
            <div class="font-16">按钮类型大致分为：</div>
            <li class="margin-left10 margin-top10 font-14">主按钮：一个操作区域只能有一个主按钮，用于主要操作动作。</li>
            <li class="margin-left10 margin-top10 font-14">默认按钮：用于没有主次之分的操作行动。</li>
            <li class="margin-left10 margin-top10 font-14">虚线按钮：主要用于添加操作。</li>
            <li class="margin-left10 margin-top10 font-14">文字按钮：用于次要或外链的行动操作。</li>
        </div>
        <div class="transverse">
            <Card style="width:100%;height:100%">
                <div slot="title">
                    <div style="font-size:16px">按钮类型</div>
                    <div class="margin-top10"> 按钮类型有：默认按钮、主按钮、虚线按钮、文字按钮以及四种颜色按钮。</div>
                </div>
                <Button class="margin-left10 margin-top30" type="primary">主要按钮</Button>
                <Button class="margin-left10 margin-top30">默认按钮</Button>
                <Button class="margin-left10 margin-top30" type="dashed">虚线按钮</Button>
                <Button class="margin-left10 margin-top30" type="text">文字按钮</Button>
                <Button class="margin-left10 margin-top30" type="info">主要按钮</Button>
                <Button class="margin-left10 margin-top30" type="success">主要按钮</Button>
                <Button class="margin-left10 margin-top30" type="warning">主要按钮</Button>
                <Button class="margin-left10 margin-top30" type="error">主要按钮</Button>
            </Card>
        </div>
        <div class="transverse">
            <Card style="width:100%;height:100%">
                <div slot="title">
                    <div style="font-size:16px">图标按钮</div>
                    <div class="margin-top10">通过设置icon属性在button内嵌一个icon，或直接在button内使用icon组件，与文字同时使用时，icon位置在左边
                    </div>
                </div>
                <Button class="margin-left10" type="primary" shape="circle" icon="ios-search"></Button>
                <Button type="primary" icon="ios-search">Search</Button>
                <Button type="primary" shape="circle" icon="ios-search">Search</Button>
                <Button type="primary" shape="circle">Circle</Button>
                <br><br>
                <Button class="margin-left10" shape="circle" icon="ios-search"></Button>
                <Button icon="ios-search">Search</Button>
                <Button shape="circle" icon="ios-search">Search</Button>
                <Button shape="circle">Circle</Button>
            </Card>
        </div>
        <div class="transverse" style="height:40%">
            <Card style="width:100%;height:100%">
                <div slot="title">
                    <div style="font-size:16px">按钮尺寸</div>
                    <div class="margin-top10">按钮有大、中、小三种尺寸。默认使用中尺寸，根据需要自行设置按钮高度。长按钮是设置按钮宽度与其父级相同
                    </div>
                </div>
                <Button class="margin-left10" style="height:40px!important" type="primary">主要按钮</Button>
                <Button type="primary" style="width:200px">主要按钮</Button>
                <br><br>
                <Button class="margin-left10" style="height:32px!important" type="primary">主要按钮</Button>
                <Button type="success" style="width:200px">其他按钮</Button>
                <br><br>
                <Button class="margin-left10" style="height:24px!important" type="primary">主要按钮</Button>
            </Card>
        </div>
        <div class="transverse">
            <Card style="width:100%;height:100%">
                <div slot="title">
                    <div style="font-size:16px">幽灵按钮</div>
                    <div class="margin-top10">
                        将按钮的内容反色，背景变为透明，常用在有色背景上。
                    </div>
                </div>
                <div class="ghost-Style">
                    <Button class="margin-left10 " type="primary" ghost>主要按钮</Button>
                    <Button type="default" ghost>默认按钮</Button>
                    <Button type="dashed" ghost>Dashed</Button>
                    <Button type="text" ghost>Text</Button>
                </div>
            </Card>
        </div>
        <div class="transverse">
            <Card style="width:100%;height:100%">
                <div slot="title">
                    <div style="font-size:16px">加载中状态</div>
                    <div class="margin-top10">
                        通过添加loading属性可以让按钮处于加载中状态，后两个按钮在点击时进入加载状态。
                    </div>
                </div>
                <div>
                    <Button type="primary" loading>Loading...</Button>
                    <Button type="primary" :loading="loading" @click="toLoading">
                        <span v-if="!loading">Click me!</span>
                        <span v-else>Loading...</span>
                    </Button>
                    <Button type="primary" :loading="loading2" icon="ios-power" @click="toLoading2">
                        <span v-if="!loading2">Click me!</span>
                        <span v-else>Loading...</span>
                    </Button>
                    <Button loading shape="circle"></Button>
                    <Button loading shape="circle" type="primary"></Button>
                </div>
            </Card>
        </div>
        <div class="transverse" style="height:60%">
            <Card style="width:100%;height:100%">
                <div slot="title">
                    <div style="font-size:16px">按钮组</div>
                    <div class="margin-top10">
                        讲多个button放到按钮组内，可通过设置按钮组属性改变按钮横纵向。
                    </div>
                </div>
                <ButtonGroup class="margin-left10 ">
                    <Button>选择一</Button>
                    <Button>选择二</Button>
                    <Button>选择三</Button>
                </ButtonGroup>
                <ButtonGroup class="margin-left10 ">
                    <Button icon="ios-color-wand-outline"></Button>
                    <Button icon="ios-sunny-outline"></Button>
                    <Button icon="ios-crop"></Button>
                    <Button icon="ios-color-filter-outline"></Button>
                </ButtonGroup>
                <ButtonGroup class="margin-left10 " vertical>
                    <Button icon="logo-facebook"></Button>
                    <Button icon="logo-twitter"></Button>
                    <Button icon="logo-googleplus"></Button>
                    <Button icon="logo-tumblr"></Button>
                </ButtonGroup>
                <br><br>
                <ButtonGroup class="margin-left10 ">
                    <Button type="primary">选择一</Button>
                    <Button>选择二</Button>
                    <Button>选择三</Button>
                </ButtonGroup>
                <ButtonGroup class="margin-left10 ">
                    <Button type="primary" icon="ios-color-wand-outline"></Button>
                    <Button icon="ios-sunny-outline"></Button>
                    <Button icon="ios-crop"></Button>
                    <Button icon="ios-color-filter-outline"></Button>
                </ButtonGroup>
                <ButtonGroup class="margin-left10 " vertical>
                    <Button type="primary" icon="logo-facebook"></Button>
                    <Button icon="logo-twitter"></Button>
                    <Button icon="logo-googleplus"></Button>
                    <Button icon="logo-tumblr"></Button>
                </ButtonGroup>
            </Card>
        </div>
        <div class="transverse">
            <Card style="width:100%;height:100%">
                <div slot="title">
                    <div style="font-size:16px">不可用状态</div>
                    <div class="margin-top10">通过添加 <span style="color:#399CFF">
                        disabled
                    </span> 属性可将按钮设置为不可用状态。
                    </div>
                </div>
                <Button disabled class="margin-left10 margin-top30" type="primary">主要按钮</Button>
                <Button disabled class="margin-left10 margin-top30">默认按钮</Button>
                <Button disabled class="margin-left10 margin-top30" type="dashed">虚线按钮</Button>
                <Button disabled class="margin-left10 margin-top30" type="text">文字按钮</Button>
                <Button disabled class="margin-left10 margin-top30" type="info">主要按钮</Button>
                <Button disabled class="margin-left10 margin-top30" type="success">主要按钮</Button>
                <Button disabled class="margin-left10 margin-top30" type="warning">主要按钮</Button>
                <Button disabled class="margin-left10 margin-top30" type="error">主要按钮</Button>
            </Card>
        </div>
        <div class="transverse">
            <Card style="width:100%;height:100%">
                <div slot="title">
                    <div style="font-size:16px">状态按钮</div>
                    <div class="margin-top10">通过添加 <span style="color:#399CFF">
                        disabled
                    </span> 属性可将按钮设置为不可用状态。
                    </div>
                </div>
                <Button class="margin-left10 margin-top30" type="info">信息按钮</Button>
                <Button class="margin-left10 margin-top30 infoStyle">
                    信息按钮
                </Button>
                <Button class="margin-left10 margin-top30 infoStyle-border">信息按钮</Button>
                <Button class="margin-left10 margin-top30 infoStyle-text">信息按钮</Button>
                <Button disabled class="margin-left10 margin-top30" type="info">信息按钮</Button>
            </Card>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'button',
        data() {
            return {
                loading: false,
                loading2: false
            }
        },
        methods: {
            toLoading() {
                this.loading = true;
            },
            toLoading2() {
                this.loading2 = true;
            }
        }
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
            /*height: 30%;*/

            .ghost-Style {
                background: rgb(190, 200, 200);
                height: 80px;
                line-height: 80px;
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
