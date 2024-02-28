<template>
  <div class="collect-card">
    <el-row style="margin: 15px 0 0 0">
      <span class="collect-card-type">Моя коллекция</span>
    </el-row>

    <el-row
      alignment="flex-start"
      v-infinite-scroll="loadMore"
      :infinite-scroll-disabled="disabled"
      infinite-scroll-distance="30"
      :infinite-scroll-immediate="true"
      class="mov-card-row"
      v-show="contenshow"
    >
      <el-col v-for="o in movieList" :key="o.id" :xs="8" :sm="4" :md="4" style="padding: 9px;">
        <router-link :to="'/movdetail/'+ o.id" style="text-decoration: none;" target="_blank">
          <div class="badge-wrapper">
            <el-badge :value="o.notifications" class="item">
              <el-card class="box-card" shadow="hover" :body-style="{ padding: '8px 5px' }">
                <div class="card-div">
                  <img :src="o.picture" class="card-image" />
                  <span class="card-remark">{{ o.remark }}</span>
                </div>
                <div style="padding: 0px;">
                  <span style="line-height: 26px; font-size: 15px; color:#777; display: flex; margin-top: 4px; text-overflow: ellipsis; overflow: hidden; width: 80%; white-space: nowrap;">
                    <el-tooltip class="box-item" effect="dark" :content="o.name" placement="bottom-end" :show-after="1000">
                      {{ o.name }}
                    </el-tooltip>
                  </span>
                </div>
              </el-card>
            </el-badge>
          </div>
        </router-link>
      </el-col>
    </el-row>

    <el-backtop :right="50" :bottom="80" />
    <p v-show="infiniteMsgShow" class="tips" style="font-size:smaller; color:#777;">Загрузка...</p>
    <p v-show="!infiniteMsgShow" class="tips" style="font-size:smaller; color:#777;">Это конец</p>
  </div>
</template>

<script>
import { ref } from 'vue';
import { showCollectVideo } from '../apis/videoCollection';
import { useStore } from 'vuex';
import {apiGetEpisodeUserView} from "../apis/getMovDetail";

export default {
  name: "CollectVideos",
  props: {
    user_id: String,
  },
  components: {},
  setup() {
    const store = useStore(); // 该方法用于返回store 实例
    return {
      store,
    };
  },
  data() {
    return {
      disabled: false,
      page: 1,
      contenshow: true,
      infiniteMsgShow: true,
      movieList: [],
    };
  },
      methods: {
        // 当属性滚动的时候  加载  滚动加载
        loadMore () {
          if (this.infiniteMsgShow === true) {
            setTimeout(
                () => {
                  this.page++ // 增加页数
                  this.getCollectMovList(this.disabled) // 请求数据
                }, 500)  // 间隔500毫秒后发送请求
          }
           },

        getCollectMovList(data) {
         if (data === false) {
           const param = {
             page: this.page,
             user: this.user_id,
             type: 'collection'
           }

           // console.log(param)
           showCollectVideo(param).then(
               (res) => {
                 // console.log(res)
                 if (res.results !== null) {
                   this.contentShow = true
                   this.infiniteMsgShow = true
                   for (var i in res.results) {
                     this.movieList.push(res.results[i])
                   }
                   if (res.next === null) {
                     this.disabled = true
                     this.contentShow = false
                     this.infiniteMsgShow = false
                   } else {
                     this.disabled = false
                     this.contentShow = true
                     this.infiniteMsgShow = true
                   }
                   this.disabled = false // 还有多余数据时 无限滚动打开
                 } else {
                   this.contentShow = false
                   this.infiniteMsgShow = false
                   this.disabled = true

                 }
               }
           ).catch(
               () => {
                 this.contentShow = false
                 this.infiniteMsgShow = false
                 this.disabled = true
               }
           )
         }
        },
        // getUserViews() {
        //   const param = {
        //     user: this.user_id
        //   }
        //   apiGetEpisodeUserView(param).then(
        //       (res) => {
        //
        //       }
        //   )
        // },
   },
  created() {
    this.getCollectMovList();
    // this.getUserViews();
  },
};
</script>

<style>
/* Добавленные стили для выравнивания уведомлений */
div.badge-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

span.collect-card-type {
  float: left;
  margin: 10px;
  font-size: 20px;
  font-weight: bold;
  line-height: 20px;
}
</style>
