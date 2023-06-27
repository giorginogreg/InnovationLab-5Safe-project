<template>
  <div>
    <h2>Upload an image</h2>
    <input type="file" @change="uploadImage">
    <button @click="predict">Predict</button>
      <ResultView :result-url="urlImage"></ResultView>
  </div>
</template>

<script>
import ResultView from "@/components/ResultView.vue";

export default {
    components: {ResultView},
  data() {
    return {
      selectedImage: null,
        urlImage: '',
    }
  },
  methods: {
    uploadImage(event) {
      this.selectedImage = event.target.files[0]
    },
    predict() {
      let formData = new FormData()
      formData.append('image', this.selectedImage)

      this.$http.post('/api/predict', formData, {
          headers: {
              'Access-Control-Allow-Origin': '*',
          }
      })
        .then(response => {
          // Mostra il risultato
          console.log(response.data.result)
            this.urlImage = '/static' + response.data.result + '?t=' + Date.now()
        })
        .catch(error => {
          console.error(error)
        })
    }
  }
}
</script>
