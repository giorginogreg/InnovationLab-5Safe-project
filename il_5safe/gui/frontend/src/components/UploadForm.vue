<template>
  <div>
      <v-select
        label="Select a model"
        v-model="selectedModel"
        :items="selectOptions"
      >
          <template v-slot:item="{ item, props }">
            <v-list-item v-bind="props" :disabled="item.raw.disabled" />
          </template>
      </v-select>
      <h2>Upload an image</h2>
    <input type="file" @change="uploadImage">
    <button @click="predict" :disabled="selectedModel === ''">Predict</button>
      <ResultView :result-url="urlImage"></ResultView>
  </div>
</template>

<script >
import ResultView from "@/components/ResultView.vue";

export default {
    components: {ResultView},
  data() {
    return {
      selectedImage: null,
      selectedModel: '',
      urlImage: '',
      selectOptions: [
        {'title':'YoloV5', 'value': 'yolov5', disabled: false},
        {'title':'FasterRCNN', 'value': 'fasterrcnn', disabled: true}
      ],
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
          console.log(response.data.result)
            this.urlImage = '/static/' + response.data.result + '?t=' + Date.now()
        })
        .catch(error => {
          console.error(error)
        })
    }
  }
}
</script>
