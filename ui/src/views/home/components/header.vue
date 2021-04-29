<template>
    <Menu @on-select=changeMenu mode="horizontal" :theme="theme" active-name="1">
        <MenuItem name="1">
            实例列表
        </MenuItem>
        <MenuItem name="2">
            实例状态
        </MenuItem>
    </Menu>
</template>
<script>
    export default {
        name: 'Header',
        data () {
            return {
                theme: 'dark'
            }
        },
        methods: {
            changeMenu (menuIndex) {
                console.log(menuIndex);
                switch (menuIndex) {
                    case '1':
                        this.$router.push('/')
                        break;
                    case '2':
                        this.$router.push('/instanceView')
                        break;
                    default:
                        break;
                }
            }
        }
    }
</script>
