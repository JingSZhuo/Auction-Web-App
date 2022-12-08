<template>
    <h1> Hello i hope this works</h1>



</template>


<script lang="ts">
import { useRoute, useRouter } from 'vue-router';
import { computed, ComputedRef, defineComponent } from 'vue';
import Header from '../components/Header.vue'

export default defineComponent({
    components: {Header},
    setup(){
        const router = useRoute()
        const itemId = computed(() => router.params.id) as ComputedRef<string>
            return {itemId}
    }
})
</script>