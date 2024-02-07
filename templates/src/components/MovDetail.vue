<template>
    <div class="vod-detail" style="margin: 20px 0; width: 90%; overflow: hidden;">
        <el-row class="vod-detail">
            <el-col :xs="24" :sm="6" class="vod-detail">
                <div class="vod-detail">
                    <img :src="movie_detail.picture" alt=""/>
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
                        <p class="des-content">{{ movie_detail.current_episodes + '/' + movie_detail.all_episodes }}</p>
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
                v-for="v, k in movie_detail.vod_play_url"
                :key="k"
                :href="v"
                :xs="8" :sm="3"
                style="margin: 5px 0;"
                >
                <el-button 
                class="vod-play-url" 
                style="float: left;" 
                @click="videoPlay" 
                :class="[{active: activeName == v}]"
                :href="v">{{ k }}
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
import apiGetMovDetail, {apiGetMovActors, apiGetMovGenres} from '../apis/getMovDetail'
import myVideoPlay from './VideoPlay.vue'
import { ElMessage } from 'element-plus'
import { ref } from 'vue'
import { useStore } from 'vuex'
import { isCollectVideo, addCollectVideo, removeCollectVideo } from '../apis/videoCollection'

export default {
  name: 'MovDetail',

  setup() {
    const store = useStore()
    return {
        store
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
        movie_detail: {},
        movie_genres: {},
        movie_actors: {},
        video_play: false,
        video_play_url: '',  // 此时正在播放的 视频url
        activeName: '',
        isCollect: 0  // 此视频是否被收藏
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
        // 将此视频添加收藏
        console.log("add collect")
        if (this.store.state.appStore.isLogining) {
            var params = {
                vod_id: this.vod_id,
                user_id: this.store.state.appStore.user.id
            }
            addCollectVideo(params).then(
                (res) => {
                    if (res.data.code == 200) {
                        this.isCollect = 1
                    } else {
                        ElMessage({
                                message: res.data.message,
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
            var params = {
                vod_id: this.vod_id,
                user_id: this.store.state.appStore.user.id
            }
            removeCollectVideo(params).then(
                (res) => {
                    if (res.data.code == 200) {
                        this.isCollect = 0
                    } else {
                        ElMessage({
                                message: res.data.message,
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
        // 显示此视频是否被收藏
        if (this.store.state.appStore.isLogining) {
            var params = {
                vod_id: this.vod_id,
                user_id: this.store.state.appStore.user.id
            }
            isCollectVideo(params).then(
                (res) => {
                    if (res.data.code == 200) {
                        this.isCollect = res.data.data
                        console.log(this.isCollect)
                    } else {
                        ElMessage({
                                message: res.data.message,
                                type: 'warning',
                            })
                    }
                }
            )
        }
    },

    videoPlay(v) {
        // 点击按钮时修改 视频播放的链接
        var play_url = v.currentTarget.attributes.href.value
        console.log(play_url)
        if (play_url) {
            this.video_play = true
            this.video_play_url = play_url
            this.activeName = play_url
        } else {
            ElMessage({
                message: '导入视频失败',
                type: 'warning',
                })
        }
        
    },

    checkHtml(s) {
        // 判断它是否是html
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
    }
  },

   watch: {
      // user出现变化后 请求数据 查看是视频是否被收藏
      moniterUser() {
        return this.store.state.appStore.user.id
      }
    },

    computed: {
      moniterUser() {
        this.showIsCollect()
      }
    },


  created() {
    this.getMovDetail()
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
</style>