<template>
  <v-container>
      <FullScreenLoading></FullScreenLoading>
      <v-row class="align-center py-6">
        <v-img :height="100" :src="iot"></v-img>
        <h1 class="text-center pa-4"> 5 Safe - Prediction PoC</h1>
        <v-img :height="100" :src="hochschule"></v-img>
      </v-row>
    <router-view/>
  </v-container>
</template>

<script>
import FullScreenLoading from "@/components/FullScreenLoading.vue";

export default {
  name: 'App',
    components: {FullScreenLoading},
    data() {
      return {
          iot: require("@/assets/iot_lab.png"),
          hochschule: require("@/assets/logo.png")
      }
    }
}
</script>
