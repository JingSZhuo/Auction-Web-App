<template>
    <div>
        <ul>
            <li v-for="item in items" :key="item.id">
            {{item.id}}<br/>
                {{item.itemTitle}}
            </li>
        </ul>
    </div>
</template>

<script lang="ts">
    export default{
    data() {
        return {
            items: []
        };
    },
    methods: {
        async fetchItems() {
            let response = await fetch("http://localhost:8000/api/AddItems/");
            let data = await response.json();
            this.items = data;
        }
    },
    mounted(){
      this.fetchItems()
    }
}
</script>