<template>
  <div>
      <Table border :columns="column" :data="data"></Table>
  </div>
</template>

<script>
export default {
    name: 'instanceTable',
    data() {
        return {
            column: [
                {
                    title: '实例名称',
                    key: 'name'
                },
                {
                    title: '主机',
                    key: 'host'
                },
                {
                    title: '端口',
                    key: 'address'
                },
                {
                    title: '业务',
                    key: 'biz'
                },
                {
                    title: '状态',
                    key: 'state'
                },
                {
                    title: '版本',
                    key: 'version'
                },
                {
                    title: '说明',
                    key: 'desc'
                },
                {
                    title: '操作',
                    key: 'operate'
                },
            ],
            data: [

            ]
            }
    }

}
</script>

<style>

</style>
