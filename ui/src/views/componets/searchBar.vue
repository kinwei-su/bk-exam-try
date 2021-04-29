<template>
    <div>
        <Form :model="form" :label-width="100" inline>
            <FormItem label="实例名称：">
                <Input v-model="form.instanceName"/>
            </FormItem>
            <FormItem label="业务：">
                <Select v-model="form.bizName">
                </Select>
            </FormItem>
            <FormItem label="IP：">
                <Input v-model="form.ipAddr" />
            </FormItem>
            <FormItem>
                <Button @click="searchInstance" type="primary">搜索</Button>
            </FormItem>
        </Form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            form: {
                instanceName: '',
                bizName: '',
                ipAddr: '',
            }
        }
    },
    methods: {
        searchInstance () {
        }
    }
}
</script>

<style>

</style>

