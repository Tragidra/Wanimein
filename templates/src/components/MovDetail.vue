<template>
    <div class="vod-detail" style="margin: 20px 0; width: 90%; overflow: hidden;">
        <el-row class="vod-detail">
            <el-col :xs="24" :sm="6" class="vod-detail">
                <div class="vod-detail">
                    <img :src="movie_detail.picture" alt=""/>
                </div>

            <div class="statistic-card">
                <el-statistic :value="movie_detail.views">
                  <template #title>
                    <div style="display: inline-flex; align-items: center">
                      <h2 style="display: inline-flex; align-items: center"> Количество просмотров</h2>
                      <el-tooltip style="display: inline-flex; align-items: center"
                        effect="dark"
                        content="Количество человек, посмотревших это произведение на нашей платформе"
                      >
                        <el-icon style="margin-left: 4px" :size="12">
                          <Warning />
                        </el-icon>
                      </el-tooltip>
                    </div>
                  </template>
                </el-statistic >
                <div class="statistic-footer">
                  <div class="footer-item">
                    <span>За сегодня </span>
                    <span class="green">
                      {{ movie_detail.change_views }}%
                      <el-icon>
                        <CaretTop />
                      </el-icon>
                    </span>
                  </div>
                </div>
            </div>
            <div class="rating-container">
              <div class="rating-group">
                <h4 >Рейтинг пользователей</h4>
                <el-rate
                  v-model="movie_detail.user_rating"
                  size="large"
                  :icons="icons"
                  :void-icon="Film"
                  @change="setUserScore"
                  :colors="['#93c4ff', '#ea5959', '#ffd93c']"
                  show-score
                  text-color="#ff9900"
                  score-template="{value}"
                />
              </div>
              <div class="rating-group">
                <h4>Умный рейтинг системы</h4>
                <el-rate
                  v-model="movie_detail.system_rating"
                  size="large"
                  :void-icon="Plus"
                  :colors="['#ffb13c']"
                  show-score
                  text-color="#ffb13c"
                  score-template="{value}"
                  disabled
                />
              </div>
            </div>
            </el-col>
            <el-col  :sm="18" style="padding: 0 10px">
                <el-row style="margin: 0 0 15px 0">
                    <p style="margin: 0; font-size: 18px;">{{ movie_detail.name }}</p>
                </el-row>

                <el-row v-if="movie_detail.vod_sub">
                    <span class="des-name">
                        Другое название:&nbsp; &nbsp;
                        <p class="des-content">{{ movie_detail.other_name }}</p>
                    </span>
                    
                </el-row>

                <el-row>
                    <span class="des-name">Страна:&nbsp;&nbsp;</span>
                    <p class="des-content"> {{ movie_detail.country }}</p>
                </el-row>

                <el-row>
                    <span class="des-name">
                        Язык:&nbsp;&nbsp;
                        <p class="des-content"> {{ movie_detail.language }}</p>
                    </span>
                    
                </el-row>

                <el-row>
                    <span class="des-name">
                        Жанр:&nbsp;&nbsp;
                        <p v-for="mog in movie_genres" class="des-content">{{ mog.genre_name + ' ' }}</p>
                    </span>
                    
                </el-row>

                <el-row>
                    <span class="des-name">
                        Выпущено:&nbsp;&nbsp;
                        <p class="des-content"> {{ movie_detail.year }}</p>
                    </span>
                    
                </el-row>

                <el-row>
                    <span class="des-name">
                        Эпизоды:&nbsp; &nbsp;
                        <p class="des-content">{{ movie_detail.current_episodes + ' / ' + movie_detail.all_episodes }}</p>
                    </span>
                    
                </el-row>

                <el-row>
                    <span class="des-name">
                        Режиссёр:&nbsp;&nbsp;
                        <p class="des-content"> {{ movie_detail.director }}</p>
                    </span>
                    
                </el-row>

                <el-row>
                    <span class="des-name">
                        Последняя серия вышла:&nbsp;&nbsp;
                        <p class="des-content"> {{ movie_detail.last_episode }}</p>
                    </span>
                    
                </el-row>

                <el-row>
                    <span class="des-name">
                        В коллекции:&nbsp;&nbsp;
                        <p class="des-content"> 
                            <el-icon :size="26" style="vertical-align: middle;" v-if="!isCollect" color="#999" @click="addCollect"><StarFilled /></el-icon>
                            <el-icon :size="26" style="vertical-align: middle" v-else color="yellow" @click="removeCollect"><StarFilled /></el-icon>  
                        </p>
                    </span>
                    
                </el-row>

                <el-row>
                    <span class="des-name">
                        Главные персонажи:&nbsp;&nbsp;
                        <p v-for="mog in movie_actors" class="des-content">{{ mog.actor_name + ' ' }}</p>
                    </span>
                    
                </el-row>

                <el-row class="detail3">
                    <span class="des-name">
                        Подробнее:&nbsp;&nbsp;
                        <p class="des-content" style="font-size:15px" v-if="checkHtml(movie_detail.synopsis)" v-html="movie_detail.synopsis"/>
                        <p class="des-content" style="font-size:15px" v-else>{{ movie_detail.synopsis }}</p>
                    </span>  
                    
                </el-row>

            </el-col>  
        </el-row>

        <el-row class="vod-play-url">
            <el-col class="vod-play-url"
                v-for="v, k in movie_detail.episodes"
                :key="k"
                :href="v"
                :xs="8" :sm="3"
                style="margin: 5px 0;"
                >
                <el-button 
                class="vod-play-url" 
                style="float: left;" 
                @click="videoPlay(v)"
                :class="[{active: activeName == v}]"
                :href="v">{{ v.name }}
                </el-button>
            </el-col>
        </el-row>
        
        <el-row class="video-play" v-if="video_play" style="margin: 40px  0">
            <myVideoPlay :src="video_play_url"/>
        </el-row>
    </div>
</template>

<script>
// 视频详情
import apiGetMovDetail, {apiGetMovActors, apiGetMovGenres, apiGetUserRating} from '../apis/getMovDetail'
import myVideoPlay from './VideoPlay.vue'
import { ElMessage } from 'element-plus'
import { Film, Plus } from '@element-plus/icons-vue'
import {mapGetters, useStore} from 'vuex'
import { isCollectVideo, addCollectVideo, removeCollectVideo } from '../apis/videoCollection'
import {ref} from "vue";

export default {
  name: 'MovDetail',

  setup() {
    const store = useStore()
    return {
        store,
    }
  },

  components: {
    myVideoPlay
  },

  props: {
        vod_id: String
    },
  data() {
    return {
        icons: [Film, Film, Film],
        icons2: [Plus],
        movie_detail: {},
        movie_genres: {},
        movie_actors: {},
        video_play: false,
        video_play_url: '',
        activeName: '',
        isCollect: 0,
    }
  },

  methods: {
    getMovDetail() {
        var param = {
            vod_id: this.vod_id
        }
        apiGetMovDetail(param).then(
            (res) => {
              this.movie_detail = res.results[0]
              apiGetMovGenres(param).then(
                  (res) => {
                    this.movie_genres = res.results
                  }
              );
              apiGetMovActors(param).then(
                  (res) => {
                    this.movie_actors = res.results
                  }
              )
            }
        )
    },

    addCollect() {
        console.log("add collect")
        if (this.store.state.appStore.isLogining) {
          const data = {
            movie_details: this.vod_id,
            user: this.store.state.appStore.user.id
          };
          addCollectVideo(data).then(
                (res) => {
                    if (res.results !== null) {
                        this.isCollect = 1
                    } else {
                        ElMessage({
                                message: 'Что-то пошло не так, попробуйте позже',
                                type: 'warning',
                            })
                    }
                }
            )
        } else {
            ElMessage({
                        message: 'Пожалуйста, авторизуйтесь',
                        type: 'warning',
                            })
        }
    },

    removeCollect() {
        console.log("remove collect")
        if (this.store.state.appStore.isLogining) {
            var data = {
                movie_details: this.vod_id,
                user: this.store.state.appStore.user.id
            }
            removeCollectVideo(data).then(
                (res) => {
                    if (res.results !== null) {
                        this.isCollect = 0
                    } else {
                        ElMessage({
                                message: 'Что-то пошло не так, пожалуйста, попробуйте позже',
                                type: 'warning',
                            })
                    }
                }
            )
        } else {
            ElMessage({
                        message: 'Пожалуйста, авторизуйтесь',
                        type: 'warning',
                            })
        }
    },

    showIsCollect() {
        if (this.store.state.appStore.isLogining) {
            var params = {
                movie_details: this.vod_id,
                user: this.store.state.appStore.user.id
            }
            if(params.user !== undefined) {
              isCollectVideo(params).then(
                  (res) => {
                    if (res.results !== null) {
                      this.isCollect = 1
                    } else {

                    }
                  }
              )
            }
        }
    },

    videoPlay(v) {
        var play_url = v.url
        console.log(v)
        console.log('Вот что просили')
        if (play_url) {
            this.video_play = true
            this.video_play_url = play_url
            this.activeName = play_url
        } else {
            ElMessage({
                message: 'Не удалось загрузить видео',
                type: 'warning',
                })
        }
        
    },

    checkHtml(s) {
        if (typeof(s) == 'string') {
            if (s.indexOf('<p>')>-1) {
                return true
            } else if (s.indexOf('<span>')>-1) {
                return true
            } else {
                return false
            }
        } else {
            return false
        }
    },

    setUserScore(value) {
      const param = {
        user: this.store.state.appStore.user.id,
        movie_details: this.movie_detail.id,
        movie_info: this.movie_detail.id,
        score: value,
      };
      apiGetUserRating(param).then(
                  (res) => {
                    this.rating_value = value;
                    ElMessage({
                    message: 'Благодарим за оценку!',
                    type: 'success',
                    })
                  })
    }
  },

  watch: {
    moniterUser() {
        return this.store.state.appStore.user.id
    }
  },

    //На случай если пользователь поменяется на странице
  computed: {
      Film() {
        return Film
      },
      Plus() {
        return Plus
      },
      moniterUser() {
        this.showIsCollect()
      },
  },


  created() {
    this.getMovDetail();

  },

  mounted() {
    this.showIsCollect();
  }

}

</script>

<style>

div.vod-detail .el-row {
    margin: 0 0 10px;
}

span.des-name {
    line-height: 20px;
    margin: 0;
    color: #999;
    font-weight: 400;
    display: inline;
    text-align: left;
}

p.des-content {
    margin: 0;
    line-height: 20px;
    text-align: left;
    display: inline;
    color:black;
}


.el-col.vod-detail div.vod-detail {
    position: relative;
    width: 100%;
    height: 0;
    overflow: hidden;
    padding-bottom: 130%;
}

.el-col.vod-detail div img {
    width: 95%;
    height: auto;
    display: block;
    margin: 0 auto;
    /* aspect-ratio: 70/89;  */
    object-fit: cover;
}

.el-button.vod-play-url.active {
  background-color: rgb(36, 184, 242);
  color: white;
  border-radius: 4px;
}
/* p {
    margin: 0;
    padding: 0;
} */

.rating-container {
    display: flex;
    flex-direction: column;
}

.rating-group {
    margin-bottom: 1px; /* Или любое другое значение, чтобы установить расстояние между группами */
}
</style>