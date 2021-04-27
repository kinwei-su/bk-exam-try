<template>
    <div id="apply">
        <div class="apply-row">
            <p>标签页</p>
            <div>
                <Tabs value="name1" :animated="false">
                    <TabPane label="标签一" name="name1">标签一的内容</TabPane>
                    <TabPane label="标签二" name="name2">标签二的内容</TabPane>
                    <TabPane label="标签三" name="name3">标签三的内容</TabPane>
                </Tabs>
                <Tabs type="card" :animated="false">
                    <TabPane label="标签一" name="name1">标签一的内容</TabPane>
                    <TabPane label="标签二" name="name2">标签二的内容</TabPane>
                    <TabPane label="标签三" name="name3">标签三的内容</TabPane>
                </Tabs>
            </div>
        </div>
        <div class="apply-row">
            <p>分页</p>
            <div style="flex-direction: column">
                <Page :total="10" show-total show-elevator/>
                <Page :total="100" show-total show-elevator/>
                <Page :total="100" show-total size="small" show-elevator/>
            </div>
        </div>
        <div class="apply-row">
            <p>面包屑</p>
            <div style="flex-direction: column">
                <Breadcrumb separator=">">
                    <BreadcrumbItem>一级页面</BreadcrumbItem>
                    <BreadcrumbItem>二级页面</BreadcrumbItem>
                    <BreadcrumbItem>当前页面</BreadcrumbItem>
                </Breadcrumb>
                <Breadcrumb>
                    <BreadcrumbItem>一级页面</BreadcrumbItem>
                    <BreadcrumbItem>二级页面</BreadcrumbItem>
                    <BreadcrumbItem>当前页面</BreadcrumbItem>
                </Breadcrumb>
                <Breadcrumb separator=">">
                    <BreadcrumbItem>
                        <Icon type="ios-home-outline"></Icon>
                        一级页面
                    </BreadcrumbItem>
                    <BreadcrumbItem>
                        <Icon type="logo-buffer"></Icon>
                        二级页面
                    </BreadcrumbItem>
                    <BreadcrumbItem>
                        <Icon type="logo-buffer"></Icon>
                        当前页面
                    </BreadcrumbItem>
                </Breadcrumb>
            </div>
        </div>
        <div class="apply-row">
            <p>进度条</p>
            <div style="flex-direction: column;height: auto">
                <Steps :current="1" style="width: 80%;margin-bottom: 20px">
                    <Step title="已完成" content="这里是该步骤的描述信息"></Step>
                    <Step title="进行中" content="这里是该步骤的描述信息"></Step>
                    <Step title="待进行" content="这里是该步骤的描述信息"></Step>
                    <Step title="待进行" content="这里是该步骤的描述信息"></Step>
                </Steps>
                <Steps :current="1" status="error" style="width: 80%;margin-bottom: 20px">
                    <Step title="已完成" content="这里是该步骤的描述信息"></Step>
                    <Step title="进行中" content="这里是该步骤的描述信息"></Step>
                    <Step title="待进行" content="这里是该步骤的描述信息"></Step>
                    <Step title="待进行" content="这里是该步骤的描述信息"></Step>
                </Steps>
                <div style="display: flex;width: 80%;">
                    <Steps :current="2" direction="vertical" style="width: 45%;">
                        <Step title="已完成" content="这里是该步骤的描述信息"></Step>
                        <Step title="已完成" content="这里是该步骤的描述信息"></Step>
                        <Step title="进行中" content="这里是该步骤的描述信息"></Step>
                        <Step title="待进行" content="这里是该步骤的描述信息"></Step>
                    </Steps>
                    <Timeline>
                        <TimelineItem color="green">
                            <p class="time">1976年</p>
                            <p class="content">Apple I 问世</p>
                        </TimelineItem>
                        <TimelineItem color="green">
                            <p class="time">1984年</p>
                            <p class="content">发布 Macintosh</p>
                        </TimelineItem>
                        <TimelineItem color="red">
                            <p class="time">2007年</p>
                            <p class="content">发布 iPhone</p>
                        </TimelineItem>
                        <TimelineItem color="blue">
                            <p class="time">2010年</p>
                            <p class="content">发布 iPad</p>
                        </TimelineItem>
                    </Timeline>
                </div>
            </div>
        </div>
        <div class="apply-row">
            <p>表单</p>
            <div style="height: auto">
                <iViewTwo></iViewTwo>
            </div>
        </div>
        <div class="apply-row">
            <p>弹出窗提示</p>
            <div>
                <div style="width: 40%;">
                    <Button @click="background('info',false)" class="margin-10">显示正常提示</Button>
                    <Button @click="background('info')" class="margin-10">显示普通提示</Button>
                    <Button @click="background('success')" class="margin-10">显示成功提示</Button>
                    <Button @click="background('warning')" class="margin-10">显示警告提示</Button>
                    <Button @click="background('error')" class="margin-10">显示错误提示</Button>
                </div>
                <div style="width: 30%;">
                    <Button @click="openConfirm('del')" class="margin-10">对话弹窗</Button>
                </div>
                <div style="width: 30%;">
                    <Button @click="show = true" class="margin-10">表单弹窗</Button>
                </div>
            </div>
        </div>
        <div class="apply-radio">
            <p>单选框</p>
            <div>
                <div style="width: 30%;">
                    <RadioGroup v-model="buttonSize" type="button">
                        <Radio label="large">Large</Radio>
                        <Radio label="default">Default</Radio>
                        <Radio label="small">small</Radio>
                    </RadioGroup>
                </div>
                <div style="width: 30%;">
                    <RadioGroup v-model="phone">
                        <Radio label="apple">
                            <Icon type="logo-apple"></Icon>
                            <span>Apple</span>
                        </Radio>
                        <Radio label="android">
                            <Icon type="logo-android"></Icon>
                            <span>Android</span>
                        </Radio>
                        <Radio label="windows">
                            <Icon type="logo-windows"></Icon>
                            <span>Windows</span>
                        </Radio>
                    </RadioGroup>
                </div>
            </div>
        </div>
        <div class="apply-row">
            <p>抽屉</p>
            <div>
                <div style="width: 45%;">
                    <Button @click="value1 = true" class="margin-10">展示抽屉</Button>
                </div>
                <div style="width: 45%;">
                    <Button @click="value2 = true" class="margin-10">编辑抽屉</Button>
                </div>
            </div>
        </div>
        <div class="apply-row">
            <p>表格</p>
            <div style="height: 400px;">
                <CwTable :columns="pro_table_titles"
                         :data="tableList" style="width: 100%;"></CwTable>
            </div>
        </div>
        <div class="apply-row">
            <p>图表</p>
            <div style="height: 400px;">
                <div id="panChartLeft" :style="{width: '100%', height: '350px'}"></div>
            </div>
        </div>
        <Modal v-model="show"
               width="420"
               title="我是弹窗"
               draggable="true"
               mask="true"
               :mask-closable="false">
            <Form ref="forms" :model="formItem" :label-width="80">
                <FormItem label="输入框"
                          prop="input"
                          :rules="{required: true, message: '输入框不能为空', trigger: 'blur'}">
                    <Input v-model="formItem.input" placeholder="请输入"></Input>
                </FormItem>
                <FormItem label="选择器">
                    <Select v-model="formItem.select" v-validate="'required'"
                            name="选择器">
                        <Option value="beijing">New York</Option>
                        <Option value="shanghai">London</Option>
                        <Option value="shenzhen">Sydney</Option>
                    </Select>
                </FormItem>
            </Form>
            <!--            <div slot="footer">-->
            <!--                <Button class="margin-left10">取消</Button>-->
            <!--                <Button type="primary"-->
            <!--                        @click="MountingOK()"-->
            <!--                >-->
            <!--                    确定-->
            <!--                </Button>-->
            <!--            </div>-->
        </Modal>
        <Drawer title="Basic Drawer" :closable="false" v-model="value1" width="600">
            <p>Some contents...</p>
            <p>Some contents...</p>
            <p>Some contents...</p>
        </Drawer>
        <Drawer title="Basic Drawer" :mask-closable="false" :closable="false" v-model="value2" width="600">
            <Form ref="forms" :model="formItem" :label-width="80">
                <FormItem label="输入框"
                          prop="input"
                          :rules="{required: true, message: '输入框不能为空', trigger: 'blur'}">
                    <Input v-model="formItem.input" placeholder="请输入" style="width: 320px;"/>
                </FormItem>
                <FormItem label="选择器">
                    <Select v-model="formItem.select" v-validate="'required'"
                            style="width: 320px;" name="选择器">
                        <Option value="beijing">New York</Option>
                        <Option value="shanghai">London</Option>
                        <Option value="shenzhen">Sydney</Option>
                    </Select>
                </FormItem>
            </Form>
            <div class="demo-drawer-footer">
                <Button type="primary" @click="value2 = false">提交</Button>
                <Button style="margin-right: 8px" @click="value2 = false">取消</Button>
            </div>
        </Drawer>
    </div>
</template>

<script>
    import CwTable from '../../components/table/cw-table';

    export default {
        name: 'apply',
        components: {CwTable},
        data() {
            return {
                show: false,
                value1: false,
                buttonSize: 'large',
                value2: false,
                formItem: {},
                pro_table_titles: [
                    {
                        type: 'selection',
                        key: 'log_type',
                        width: 60,
                        // fixed: 'left',
                        // sortable: true
                    },
                    {
                        title: '用户名',
                        key: 'userName',
                        align: 'left',
                        sortable: true,
                    },
                    {
                        title: '所属网络',
                        key: 'Network',
                        align: 'left',
                        sortable: true,
                    },
                    {
                        title: '身份',
                        key: 'identity',
                        align: 'left',
                        sortable: true,
                    },
                    {
                        title: 'IP',
                        key: 'IP',
                        align: 'left',
                        sortable: true,
                    },
                    {
                        title: '操作',
                        // fixed: 'right',
                        width: 250,
                        align: 'left',
                        render: (h, params) => {
                            let check = false
                            return h('div', [
                                h('Button', {
                                    class: 'detail-color',
                                    props: {
                                        type: 'text',
                                    },
                                    style: {
                                        marginRight: '5px'
                                    },
                                    on: {
                                        click: () => {
                                            this.update(params.index, params.row)
                                        }
                                    }
                                }, '修改'),
                                h('Button', {
                                    class: 'detail-color',
                                    props: {
                                        type: 'text',
                                    },
                                    style: {
                                        marginRight: '5px'
                                    },
                                    on: {
                                        click: () => {
                                            this.delete(params.index, params.row)
                                        }
                                    }
                                }, '删除')
                            ]);
                        }
                    }],
                tableList: [
                    {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {
                        userName: 'instance-00412937',
                        Network: '公有云',
                        identity: '超级管理员',
                        IP: '127.0.0.1'
                    }, {userName: 'instance-00412937', Network: '公有云', identity: '超级管理员', IP: '127.0.0.1'}],
                phone: 'apple',
            }
        },
        mounted() {
            this.drawLeft()
        },
        methods: {
            background(type, back = true) {
                this.$Message[type]({
                    background: back,
                    content: '这是一条带背景色的通知'
                });
            },
            openConfirm(type) {
                this.$CWConfirm({
                    type: type,
                    title: '删除',
                    content: '是否删除这条数据',
                    okText: '删除',
                    cancelText: '取消',
                }).then(() => {
                    console.log('确定')
                }).catch(() => {
                    console.log('取消')
                });
            },
            drawLeft() {
                //柱形图
                let panChartLeft = this.$echarts.init(document.getElementById('panChartLeft'));
                panChartLeft.setOption({
                    title: {
                        text: '某楼盘销售情况',
                    },
                    tooltip: {
                        trigger: 'axis',
                        backgroundColor: '#fff',
                        textStyle: {
                            color: '#5F6568' //设置文字颜色
                        },
                        padding: 10,
                        extraCssText: 'box-shadow: 0 2px 6px rgba(0, 0, 0, 0.12);'
                    },
                    legend: {
                        itemHeight: 12,
                        itemWidth: 12,
                        icon: 'rect',
                        data: ['意向', '预购', '成交'],
                        x: 'right',
                        padding: [10, 20]
                    },
                    grid: {
                        x: 50,
                        y: 50,
                        x2: 20,
                        y2: 20
                    },
                    xAxis: [
                        {
                            type: 'category',
                            boundaryGap: false,
                            data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value'
                        }
                    ],
                    series: [
                        {
                            name: '成交',
                            type: 'line',
                            smooth: true,
                            itemStyle: {normal: {areaStyle: {type: 'default'}}},
                            data: [10, 12, 21, 54, 260, 830, 710]
                        },
                        {
                            name: '预购',
                            type: 'line',
                            smooth: true,
                            itemStyle: {normal: {areaStyle: {type: 'default'}}},
                            data: [30, 182, 434, 791, 390, 30, 10]
                        },
                        {
                            name: '意向',
                            type: 'line',
                            smooth: true,
                            itemStyle: {normal: {areaStyle: {type: 'default'}}},
                            data: [1320, 1132, 601, 234, 120, 90, 20]
                        }
                    ]
                });
            },
        }
    }
</script>

<style scoped lang="scss">
    #apply {
        overflow-y: auto;

        .time {
            font-size: 14px;
            font-weight: bold;
        }

        .content {
            padding-left: 5px;
        }

        .apply-radio {
            > > p {
                font-size: 24px;
                margin-bottom: 8px;
                font-weight: bold;
            }

            > > div {
                height: 120px;

                > > div {
                    width: 45%;
                    margin-bottom: 24px;
                }
            }
        }

        .apply-row {
            margin-bottom: 20px;

            > > p {
                font-size: 24px;
                margin-bottom: 8px;
                font-weight: bold;
            }

            > > div {
                display: flex;
                justify-content: space-between;
                height: 120px;

                > > div {
                    width: 45%;
                }
            }
        }
    }

    .demo-drawer-footer {
        width: 100%;
        position: absolute;
        bottom: 0;
        left: 0;
        border-top: 1px solid #e8e8e8;
        padding: 10px 16px;
        text-align: left;
        background: #fff;
    }
</style>
