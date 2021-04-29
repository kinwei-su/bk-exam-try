<template>
    <div>
        <search-bar/>
        <instance-table/>
    </div>
</template>

<script>
import InstanceTable from '../componets/instanceTable'
import SearchBar from '../componets/searchBar.vue'
export default {
    name: 'instanceView',
    components: {
        SearchBar,
        InstanceTable,
    }
}
</script>

<style>

</style>
