<template>
    <div id="vm">
        <div class="search-top">
            <div class="search-input">
                <Input @on-search="SearchUser" v-model="SearchData" placeholder="输入用户名、所属网络、身份搜索" search>
                </Input>
            </div>
            <div class="search-button">
                <Button style="float:right" @click="exportData" type="primary">导出</Button>
            </div>
        </div>
        <div class="search-content">
            <CwTable :columns="pro_table_titles" :cwheight="0"
                     :data="tableList" ref="cwTable"></CwTable>
        </div>
    </div>
</template>

<script>
    import CwTable from '@/components/table/cw-table'

    export default {
        name: 'instancePage',
        components: {
            CwTable,
        },
        data() {
            return {
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
                title: '开机',
                SearchData: '',
                timer: '',
            }
        },
        watch: {},
        mounted() {
            let _this = this
            this.InitDataTime(_this)
        },
        destroyed() {
            clearTimeout(this.timer)
        },
        computed: {},
        methods: {
            //时间加载
            InitDataTime(_this) {
                _this.timer = setInterval(function () {
                }, 10000)
            },
            //修改
            update(index, row) {
                let content = '是否修改用户：' + row.userName
                this.$CWConfirm({
                    type: 'edit',
                    title: '修改',
                    content: content,
                    okText: '确定',
                    cancelText: '取消',
                }).then(() => {
                })
            },
            //删除
            delete(index, row) {
                let content = '是否删除用户：' + row.userName
                this.$CWConfirm({
                    type: 'del',
                    title: '关机',
                    content: content,
                    okText: '删除',
                    cancelText: '取消',
                }).then(() => {
                })
            },
            //搜索
            SearchUser() {
            },
            //导出
            exportData() {
            },
        }
    }
</script>

<style scoped lang="scss">
    #vm {
        .search-top {
            width: 100%;
            padding: 12px 16px;
            height: 56px;
            background-color: #fff;

            .search-input {
                width: 20%;
                float: left;
            }

            .search-button {
                float: right;
                width: 20%;
            }
        }

        .search-content {
            width: 100%;
            background-color: #fff;
            height: calc(100% - 58px);
        }
    }
</style>
<style scoped>
    /deep/ div::-webkit-scrollbar {
        width: 4px!important;
        color: #C5CACF!important;
        /**/
    }
</style>
