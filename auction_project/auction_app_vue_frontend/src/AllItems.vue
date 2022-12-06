<template>
    <div>
        <table>
            <tr v-for="(item, item_id) in (items['items' as unknown as number])" :key="item_id">
                <th>{{item.id}}</th>
                <th>{{item.item_title}}</th>
                <th>{{item.item_description}}</th>
                <th>{{item.item_sprice}}</th>
                <th>{{item.item_picture}}</th>
                <th>{{item.item_auctionfinish}}</th>
            </tr>
        </table>
    </div>
</template>

<script lang="ts">
    export default{
    data() {
        return {
            items: [] as any[]
        };
    },
    methods: {
        async fetchItems() {
            let response = await fetch("http://localhost:8000/api/addItems/");
            let data = await response.json();
            this.items = data;
        }
    },
    mounted(){
      this.fetchItems()
    }
}
</script>