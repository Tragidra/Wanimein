<template>
  <el-carousel :interval="4000" type="card" height="200px">
    <el-carousel-item v-for="movie in movies" :key="movie.id">
      <el-card class="hot-card" :style="{ 'background-image': `url('${movie.picture}')`, 'background-size': 'cover' }">
        <div>
          <h4 class="movie-name">{{movie.name}}...</h4>
        </div>
        <div>
          <h5 class="movie-synopsis">{{movie.shortsynopsis}}...</h5>
        </div>
        <div class="flex gap-2 mt-4">
          <el-tag v-for="tag in movie.tags"
            :type="colors[movie.id]"
            effect="plain"
            round
          >
            {{tag.tags_name}}
          </el-tag>
        </div>
      </el-card>
    </el-carousel-item>
  </el-carousel>
</template>

<script>
import {useStore} from "vuex";

export default {
  name: "HotVideos",
  props: {
    movies: null
  },
  components: {},

  setup() {
    const store = useStore()
    return {
      store,
    }
  },

  data() {
    return {
      hots: [],
      colors: ['primary', 'success', 'info', 'warning', 'danger']
    }
  },

  methods: {
  },

  created() {

  }
}
</script>

<style scoped>
  .movie-name {
    color: white;
    font-weight: bold;
    /* Дополнительные стили по вашему выбору */
  }

  .movie-synopsis {
    color: white;
    font-weight: bold;
    /* Дополнительные стили по вашему выбору */
  }
</style>