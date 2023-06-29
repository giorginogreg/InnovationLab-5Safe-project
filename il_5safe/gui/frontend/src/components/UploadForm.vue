<template>
  <div>
      <v-row align="center" justify="center">
          <v-col cols="6" class="mr-6">
            <v-card
              title="Upload an image"
              subtitle="Select an image that you would like to predict pedestrians and bikers"
            >
                <v-card-text>
                 <v-file-input @change="uploadImage" :rules="rules" accept="image/*" label="Image input" prepend-icon="mdi-camera"></v-file-input>
                </v-card-text>
            </v-card>
          </v-col>
          <v-col class="d-flex flex-column ">
                <v-select
                hide-details
                class="py-2 "
                label="Select a model"
                v-model="selectedModel"
                :items="selectOptions"
              >
                  <template v-slot:item="{ item, props }">
                    <v-list-item v-bind="props" :disabled="item.raw.disabled" />
                  </template>
              </v-select>
            <v-btn class="d-flex" @click="predict" :disabled="selectedModel === ''">Predict</v-btn>
          </v-col>
      </v-row>
      <ResultView class="py-4" :result-url="urlImage"></ResultView>
  </div>
</template>

<script >
import ResultView from "@/components/ResultView.vue";
import eventBus from "@/plugins/eventBus";

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
        rules: [
        value => {
          return !value || !value.length || value[0].size < 5000000 || 'Image size should be less than 5 MB!'
        },
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
      eventBus.$emit("retrievingDataChanged", true);

      this.$http.post('/api/predict', formData, {
          headers: {
              'Access-Control-Allow-Origin': '*',
               'Content-Type': 'multipart/form-data'
          }
      })
        .then(response => {
          //console.log(response.data.result)
            this.urlImage = '/static/' + response.data.result + '?t=' + Date.now()
        })
        .catch(error => {
          console.error(error)
        }).finally(() => eventBus.$emit("retrievingDataChanged", false))
    }
  }
}
</script>
