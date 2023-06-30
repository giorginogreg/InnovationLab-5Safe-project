<template>
<v-dialog
    v-model="retrievingData"
    content-class="custom_dialog"
    persistent="true"
  >
    <div class="text-center">
      <v-progress-circular
        indeterminate
        color="white"
      />
    </div>
  </v-dialog>
</template>

<script>
import eventBus from "@/plugins/eventBus";

export default {
  name: 'FullScreenLoading',
  data() {
    return {
        retrievingData: false,
    };
  },
  mounted() {
     eventBus.$on('retrievingDataChanged', status => {
        this.retrievingData = status
      });
  }
};
</script>

<style scoped>

.custom_dialog {
  box-shadow: unset !important;
  overflow: unset !important;
}

</style>
