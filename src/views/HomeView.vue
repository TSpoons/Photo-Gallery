<template>
  <div class="home row justify-content-center flex-grow-1">
    <div class="col-sm-4" v-for="(photo, index) in photos" :key="index">
      <img :src="photo">
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
        photos: [],
    }
  },  
  methods: {
    getPhotos() {
      const path = 'http://localhost:5000/photos';
      axios.get(path, {responseType: "json"})
        .then((res) => {
          res.data.forEach((photo) => {
            this.photos.push(photo.src);
          });
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getPhotos();
  }
}
</script>

<style>
.home {
  background-color: var(--secondary);
}

img {
    width: 80%;
    height: 80%;
    object-fit: scale-down;
 }
</style>
