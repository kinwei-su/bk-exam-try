<template>
    <div id="grid" v-loading="loading">
        <div class="Titles font-20">业务拓扑</div>
        <div class="transverse">
            <div class="transverseContentleft"></div>
            <div class="transverseContent font-18"></div>
            <div class="transverseBottom">
                <div class="leftNavigation font-14 hightBackColor" style="height: auto">
                    <div style="margin: 0px">
                        <Select v-model="bussiness_id"
                                style="width: 214px;height: 100%"
                                @on-change="search_topo">
                            <Option v-for="(item, index) in bussiness_data"
                                    :key="item.biz+index"
                                    style="width: 214px;height: 100%"
                                    :value="item.biz"
                                    :label="item.name">
                            </Option>
                        </Select>
                    </div>
                    <div style="margin-left: 0px; text-align: left" v-if="bussiness_id">
                        <div style="height: 32px">
                            <el-input
                                placeholder="输入关键字进行过滤"
                                style="margin-bottom: 1px"
                                v-model="filterText">
                            </el-input>
                        </div>
                        <el-tree
                            class="filter-tree"
                            :data="topoData"
                            :props="defaultProps"
                            @node-click="query_detail"
                            default-expand-all
                            :filter-node-method="filterNode"
                            ref="tree">
                        </el-tree>
                    </div>
                </div>
                <div class="leftContent backColor font-14" style="height: auto">
                    <Tabs value="name1">
                        <TabPane label="主机列表" name="name1">
                            <div style="text-align: left" v-if="query_data">
                                <div style="width: 250px; display: inline-block">
                                    <Select v-model="attribute"
                                            style="width: 250px;">
                                        <Option v-for="(item, index) in select_data"
                                                :key="item.label+index"
                                                style="width: 250px;"
                                                :value="item.label"
                                                :label="item.value">
                                        </Option>
                                    </Select>
                                </div>
                                <div style="width: 250px; display: inline-block;">
                                    <Input v-model="searchData"
                                           style="width: 250px;"
                                           placeholder="请输入属性值"
                                           search
                                           @on-search="search_host_list"/>
                                </div>
                            </div>
                            <div>
                                <CwTable :columns="tableTitle"
                                         :data="table_data"
                                         :cwheight=0
                                         remote="true"
                                         :page-size="page_size"
                                         :current-page="page"
                                         :total="total"
                                         @sizeChange="sizeChange"
                                         @pageChange="currentChange"
                                ></CwTable>
                            </div>
                        </TabPane>
                        <TabPane label="节点信息" name="name2">
                            <div v-for="(item, index) in title" :key="item+index"
                                 style="margin-left: 30px; font-size: large">
                                <table style="margin-bottom: 30px">
                                    <tr>
                                        <td>{{ item }}</td>
                                    </tr>
                                    <tr v-for="(data_item, data_index) in title_data[item]"
                                        :key="data_item+data_index">
                                        <td v-for="(data_child_item, data_child_index) in data_item"
                                            style="display: inline-block; margin: 20px"
                                            :key="data_child_item+data_child_index">{{
                                                data_child_item.name
                                            }}:{{ data_child_item.value }}
                                        </td>
                                    </tr>
                                </table>
                            </div>
                        </TabPane>
                    </Tabs>
                </div>
            </div>
        </div>
        <Drawer :title="innerip" :closable="false" v-model="is_console" width="600">
            <table>
                <tr v-for="(host_info_data_item, host_info_data_index) in host_info_data"
                    :key="host_info_data_item+host_info_data_index">
                    <td>{{ host_info_data_item.bk_property_name }}:</td>
                    <td>{{ host_info_data_item.bk_property_value }}</td>
                </tr>
            </table>
        </Drawer>
    </div>
</template>

<script>
    import CwTable from '@/components/newTable/cw-table'


    export default {
        name: 'layout',
        components: {
            CwTable,
        },
        data() {
            return {
                attribute: '',
                loading: false,
                is_console: false,
                searchData: '',
                innerip: '',
                bussiness_id: '',
                title: [],
                title_data: [],
                total: 0,
                page: 1,
                page_size: 10,
                query_data: '',
                bussiness_data: [],
                table_data: [],
                filterText: '',
                host_info_data: [],
                tableTitle: [
                    {
                        title: '内网IP',
                        key: 'bk_host_innerip',
                        tooltip: true,
                        resizable: true,
                        // width: 150
                        render: (h, params) => {
                            return h('span', {
                                style: {
                                    cursor: 'pointer'
                                },
                                on: {
                                    click: () => {
                                        this.show_detail(params.row, '查看')
                                    }
                                }
                            }, params.row.bk_host_innerip);
                        }
                    },
                    {
                        title: '云区域',
                        key: 'bk_cloud_id',
                        // width: 100,
                        resizable: true,
                    },
                    {
                        title: '操作系统类型',
                        key: 'bk_os_type',
                        // width: 100,
                        resizable: true,
                    },
                    {
                        title: '主要维护人',
                        key: 'operator',
                        tooltip: true,
                        // width: 200,
                        resizable: true,
                    },
                    {
                        title: '模板名',
                        key: 'bk_module_name',
                        tooltip: true,
                        // width: 220,
                        resizable: true,
                    },
                    {
                        title: '集群名',
                        key: 'bk_set_name',
                        tooltip: true,
                        // width: 220,
                        resizable: true,
                    },
                ],
                topoData: [
                    {
                        title: 'parent 1',
                        expand: true,
                        children: [
                            {
                                title: 'parent 1-1',
                                expand: true,
                                children: [
                                    {
                                        title: 'leaf 1-1-1'
                                    },
                                    {
                                        title: 'leaf 1-1-2'
                                    }
                                ]
                            },
                            {
                                title: 'parent 1-2',
                                expand: true,
                                children: [
                                    {
                                        title: 'leaf 1-2-1'
                                    },
                                    {
                                        title: 'leaf 1-2-1'
                                    }
                                ]
                            }
                        ]
                    }
                ],
                defaultProps: {
                    children: 'children',
                    label: 'label'
                },
                select_data: [
                    {label: 'bk_isp_name', value: '所属运营商'},
                    {label: 'bk_sn', value: '设备SN'},
                    {label: 'operator', value: '主要维护人'},
                    {label: 'bk_outer_mac', value: '外网MAC'},
                    {label: 'bk_state_name', value: '所在国家'},
                    {label: 'bk_province_name', value: '所在省份'},
                    {label: 'import_from', value: '录入方式'},
                    {label: 'bk_sla', value: 'SLA级别'},
                    {label: 'bk_service_term', value: '质保年限'},
                    {label: 'bk_os_type', value: '操作系统类型'},
                    {label: 'bk_os_version', value: '操作系统版本'},
                    {label: 'bk_os_bit', value: '操作系统位数'},
                    {label: 'bk_mem', value: '内存容量'},
                    {label: 'bk_mac', value: '内网MAC地址'},
                    {label: 'bk_host_outerip', value: '外网IP'},
                    {label: 'bk_host_name', value: '主机名称'},
                    {label: 'bk_host_innerip', value: '内网IP'},
                    {label: 'bk_host_id', value: '主机ID'},
                    {label: 'bk_disk', value: '磁盘容量'},
                    {label: 'bk_cpu_module', value: 'CPU型号'},
                    {label: 'bk_cpu_mhz', value: 'CPU频率'},
                    {label: 'bk_cpu', value: 'CPU逻辑核心数'},
                    {label: 'bk_comment', value: '备注'},
                    {label: 'bk_cloud_id', value: '云区域'},
                    {label: 'bk_bak_operator', value: '备份维护人'},
                    {label: 'bk_asset_id', value: '固资编号'}
                ]
            }
        },
        methods: {
            initData() {
                this.loading = true;
                this.$api.Search.search_bussiness_topo().then(res => {
                    if (res.result) {
                        this.topoData = res.data
                    } else {
                        this.$message.error(res.message)
                    }
                    this.loading = false
                })
            },
            query_detail(data) {
                console.log('datadatadatadatadatadatadatadatadatadata')
                console.log(data)
                this.query_data = data
                this.loading = true
                this.$api.Search.query_detail(
                    {
                        'biz': this.bussiness_id,
                        'params': this.query_data,
                        'page': this.page,
                        'page_size': this.page_size
                    }
                ).then(res => {
                    if (res.result) {
                        this.table_data = res.data
                        this.total = res.total
                        this.$api.Search.query_node_info(
                            {
                                'biz': this.bussiness_id,
                                'params': this.query_data
                            }
                        ).then(res => {
                            if (res.result) {
                                this.title_data = res.data
                                this.title = res.title
                            } else {
                                this.$message.error(res.message)
                            }
                        })
                    } else {
                        this.$message.error(res.message)
                    }
                    this.loading = false
                })
            },
            search_topo() {
                this.loading = true;
                this.$api.Search.search_bussiness_topo({'biz': this.bussiness_id}).then(res => {
                    if (res.result) {
                        this.topoData = res.data
                    } else {
                        this.$message.error(res.message)
                    }
                    this.loading = false
                })
            },
            search_host_list() {
                this.loading = true;
                this.$api.Search.search_host_list({
                    'biz': this.bussiness_id,
                    'params': this.query_data,
                    'page': this.page,
                    'page_size': this.page_size,
                    'search_data': this.searchData,
                    'filter': this.attribute,
                }).then(res => {
                    if (res.result) {
                        this.table_data = res.data
                    } else {
                        this.$message.error(res.message)
                    }
                    this.loading = false
                })
            },
            search_bussiness() {
                this.loading = true;
                this.$api.Search.search_bussiness().then(res => {
                    if (res.result) {
                        this.bussiness_data = res.data
                    } else {
                        this.$message.error(res.message)
                    }
                    this.loading = false
                })
            },
            // search_host_info() {
            //     this.loading = true;
            //     this.$api.Search.search_host_info().then(res => {
            //         if (res.result) {
            //             this.bussiness_data = res.data
            //         } else {
            //             this.$message.error(res.message)
            //         }
            //         this.loading = false
            //     })
            // },
            show_detail(data) {
                // console.log(data)
                // this.loading = true;
                this.is_console = true
                this.innerip = data.bk_host_innerip
                this.$api.Search.search_base_info({host: data.bk_host_id}).then(res => {
                    if (res.result) {
                        this.host_info_data = res.data
                    } else {
                        this.$message.error(res.message)
                    }
                    // this.loading = false
                })
            },
            filterNode(value, data) {
                if (!value) return true
                return data.label.indexOf(value) !== -1
            },
            sizeChange(size) {
                // this.page.pageSize = val
                //this.initDate()
                this.page_size = size
                this.query_detail(this.query_data)
            },
            currentChange(page) {
                this.page = page.pageNum
                this.query_detail(this.query_data)
            },
        },
        mounted() {
            this.search_bussiness()
            // this.search_host_info()
        },
        watch: {
            filterText(val) {
                this.$refs.tree.filter(val);
            }
        },
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

        /deep/ .ivu-select-dropdown {
            height: 70%;
            max-height: 1000px;
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
                    text-align: left;
                    color: #ffffff;
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
