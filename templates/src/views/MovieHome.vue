<template>
  <div>
    <div class="main-container">
      <div class="main-content">
        <HotVideos :movies="hots"/>
        <MovLimitCardVue :movtype="1"/>
        <MovLimitCardVue :movtype="2"/>
        <MovLimitCardVue :movtype="3"/>
        <MovLimitCardVue :movtype="4"/>
      </div>
      <div class="side-container">
        <LastNews :movies="news"/>
      </div>
    </div>
    <el-backtop :right="50" :bottom="80" />
  </div>
</template>

<script>
// 首页
import MovLimitCardVue from '../components/MovLimitCard.vue'
import LastNews from "../components/LastNews.vue";
import HotVideos from "../components/HotVideos.vue";
import {computed} from "vue";
import apiGetMovDetail, {apiGetMovTags} from "../apis/getMovDetail";
import {ElMessage} from "element-plus";

export default {
  name: 'MovieHome',
  components: {
    HotVideos,
    LastNews,
    MovLimitCardVue,
  },

  data() {
    return {
      news: {},
      hots: {},
      tags: {},
      maxCharacters: 100,
    }
  },

  methods: {

    getUpdates(){
      const params = {
        type: 'news'
      };
      apiGetMovDetail(params).then(
          (res) => {
            this.news = res.results
          }
      )
    },
    getHots(){
      const params = {
        type: 'hot'
      };
      apiGetMovDetail(params).then(
          (res) => {
            this.hots = res.results
            for (const e of this.hots) {
              e.shortsynopsis = e.synopsis.length > this.maxCharacters
        ? e.synopsis.substring(0, this.maxCharacters)
        : e.synopsis;
            }
            var queryString = "ids=" + this.hots.map(obj => obj.id).join(",");
            console.log(queryString)
            const param = {
              ids: queryString
            };
            apiGetMovTags(param).then(
                (res) => {
                  for (let i = 0; i < this.hots.length; i++) {
                    this.hots[i].tags =  res.filter(item => item.movie_details === this.hots[i].id)
                  }
                }
            )
          }
      )
    },
  },

  created() {
    this.getUpdates();
    this.getHots();
  }
}
</script>

<style>
.main-container {
  display: flex;
}

.main-content {
  flex: 1;
}

.side-container {
  width: 300px; /* Укажите нужную ширину контейнера */
  padding: 20px;
  box-sizing: border-box;
  /* Добавьте другие стили, если необходимо */
}
</style>