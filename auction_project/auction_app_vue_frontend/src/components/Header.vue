<template>
    <div class="text-center my-3">
      <h4>Ebay</h4>
      <div class="d-flex justify-content-center">
        <HeaderLink to="/" exact>Home</HeaderLink>
        <HeaderLink to="../AllList">List</HeaderLink>
        <!-- <HeaderLink to=""></HeaderLink> -->
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue'
  import HeaderLink from './HeaderLink.vue'
  export default defineComponent({
    components: { HeaderLink }
  })
  </script>