<template>
  <div>
    <h2>Result</h2>
    <img :src="resultUrl" alt="Result">
  </div>
</template>

<script>
export default {
  props: {
    resultUrl: {
      type: String,
      required: true
    }
  }
}
</script>
