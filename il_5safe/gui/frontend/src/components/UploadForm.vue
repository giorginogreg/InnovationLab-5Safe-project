<template>
  <div>
    <h2>Upload an image</h2>
    <input type="file" @change="uploadImage">
    <button @click="predict">Predict</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedImage: null
    }
  },
  methods: {
    uploadImage(event) {
      this.selectedImage = event.target.files[0]
    },
    predict() {
      let formData = new FormData()
      formData.append('image', this.selectedImage)

      this.$http.post('http://localhost:5000/api/predict', formData, {
          headers: {
              'Access-Control-Allow-Origin': '*',
          }
      })
        .then(response => {
          // Mostra il risultato
          console.log(response.data.result)
        })
        .catch(error => {
          console.error(error)
        })
    }
  }
}
</script>
