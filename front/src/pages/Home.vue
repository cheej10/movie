<template lang="pug">
.flex.q-gutter-md.justify-start
  div.cursor-pointer(v-for="(movie, index) in movies" :key="`movie${index}`" @click="this.$router.push(`/movie/${movie.id}`)")
    img(:src="movie.poster_img")
    p {{ movie.title }}
</template>

<script>
export default {
  data() {
    return {
      movies: [],
    };
  },
  methods: {
    async get_movies() {
      await fetch("http://localhost:8000/movies")
      .then((res) => res.json())
      .then(data => console.log(data))
    },
  },
  created() {
    this.get_movies();
  },
};
</script>

<style>
</style>