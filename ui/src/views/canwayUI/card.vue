<template>
    <div id="card">
        <div class="font-20">卡片</div>
        <div>
            <div class="content">
                <div>无边框卡片</div>
                <div>
                    <Card :bordered="false">
                        <div class="card-one">
                            <div>
                                <div class="card-title font-20">我是数字数字</div>
                                <div>这里是标题</div>
                            </div>
                            <div>
                                <Icon type="md-notifications" size="32"/>
                            </div>
                        </div>
                    </Card>
                    <Card :bordered="false">
                        <p slot="title">这里是标题</p>
                        <p slot="extra">更多</p>
                        <p>这里是内容</p>
                        <p>这里是内容</p>
                        <p>这里是内容</p>
                    </Card>
                    <Card :bordered="false">
                        <div class="card-three">
                            <div>
                                <Icon type="md-notifications" size="32"/>
                            </div>
                            <div>这是一个简介卡片内容</div>
                        </div>
                    </Card>
                </div>
            </div>
            <div class="content">
                <div>边框卡片</div>
                <div>
                    <Card>
                        <div class="card-one">
                            <div>
                                <div class="card-title font-20">我是数字数字</div>
                                <div>这里是标题</div>
                            </div>
                            <div>
                                <Icon type="md-notifications" size="32"/>
                            </div>
                        </div>
                    </Card>
                    <Card>
                        <p slot="title">这里是标题</p>
                        <p slot="extra">更多</p>
                        <p>这里是内容</p>
                        <p>这里是内容</p>
                        <p>这里是内容</p>
                    </Card>
                    <Card>
                        <div class="card-three">
                            <div>
                                <Icon type="md-notifications" size="32"/>
                            </div>
                            <div>这是一个简介卡片内容</div>
                        </div>
                    </Card>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'card'
    }
</script>

<style scoped lang="scss">
    #card {
        height: 100%;
        overflow-y: auto;

        /deep/ .ivu-icon {
            font-size: 32px !important;
        }

        /deep/ .ivu-card-body {
            height: 100%;
        }

        /deep/ .ivu-card-extra {
            color: $base-color;
        }

        > > div:last-child {
            height: calc(100% - 50px);
            display: flex;
            flex-direction: column;
            justify-content: space-around;

            > > div:first-child {
                background-color: #eee;
            }

            .content {
                height: 45%;
                padding: 8px 16px 16px;

                > > div:first-child {
                    margin-bottom: 4px;
                }

                > > div:last-child {
                    display: flex;
                    justify-content: space-between;

                    > > div {
                        width: 30%;
                    }
                }

                .card-one {
                    display: flex;
                    height: 100%;
                    align-items: center;
                    justify-content: space-between;
                    padding: 0 8px;

                    > > div:first-child {
                        display: flex;
                        height: 100%;
                        flex-direction: column;
                        justify-content: space-evenly;
                    }

                    > > div:last-child {
                        color: $base-color;
                        background-color: #ebf5ff;
                        padding: 14px;
                        border-radius: 50%;
                    }
                }

                .card-three {
                    display: flex;
                    height: 100%;
                    align-items: center;
                    justify-content: space-evenly;
                    flex-direction: column;

                    > > div:first-child {
                        color: $base-color;
                      background-color: #ebf5ff;
                        padding: 8px;
                        border-radius: 50%;
                    }
                }
            }
        }
    }
</style>
