<template>
  <div>
    <h2 class="py-4">Result</h2>
      <v-img :lazy-src="lazy_src" :src="resultUrl" alt="Result">
          <template v-slot:placeholder>
      <div class="d-flex align-center justify-center fill-height">

      </div>
    </template>
      </v-img>
  </div>
</template>

<script>
export default {
    data() {
        return {
          "lazy_src": require("@/assets/default.png")
        }
    },
  props: {

    resultUrl: {
      type: String,
      required: true,
    }
  }
}
</script>
<style scoped>
.v-responsive__sizer {
    padding: 0 !important;
}
</style>
