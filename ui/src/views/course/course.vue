<template>
    <div id="course">
        <div></div>
        <div></div>
        <div></div>
        <div></div>
    </div>
</template>

<script>
    export default {
        name: 'course',
        props: {},
        data() {
            return {
                name: '',
                dataList: []
            }
        },
        computed: {
            nameFilter() {
                return this.dataList.filter(item => {
                    return item.name === 'name'
                })
            }
        },
        watch: {
            'name'() {
                console.log(this.name)
            }
        },
        created() {
            // this.myFunc()
        },
        mounted() {
            // this.myFunc()
        },
        methods: {
            myFunc() {
                const param = {}
                this.$api.Server.testPost(param).then(res => {
                    console.log(res);
                })
                this.$showLoading()
                this.name = this.nameFilter()
                console.log(this.name)
            }
        }
    }
</script>

<style scoped lang="scss">
    #course {
        color: $base-color;
    }
</style>
