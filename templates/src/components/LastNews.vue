<template>
  <el-timeline>
    <el-timeline-item v-for="movie in movies" timestamp="Новый контент" type="primary" hollow placement="top">
      <el-card :style="{ 'background-image': `url('${movie.picture}')`, 'background-size': 'cover' }">
        <router-link :to="'/movdetail/'+ movie.id" v-if="movie.current_episodes !== 0 && movie.current_episodes !== 1" style="color: white; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);"> Обновление "{{movie.name}}"</router-link>
        <router-link :to="'/movdetail/'+ movie.id" v-else style="color: white; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);"> Новый релиз – "{{movie.name}}"</router-link>
        <h4 style="color: white; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);">Добавлена Серия {{movie.current_episodes}}</h4>
      </el-card>
    </el-timeline-item>
  </el-timeline>
</template>

<script>
import {useStore} from "vuex";

export default {
  name: "LastNews",
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
      news: [],
    }
  }
}

</script>

<style scoped>

</style>