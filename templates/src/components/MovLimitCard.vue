<template>  
  <div class="home-card" v-show="contentshow">
    <el-row style="margin: 15px 0 0 0">
        <span class="home-card-type">{{ type_id_names[movtype] }}</span>
        <router-link :to="'/movtype/'+ movtype" class="home-card-type" style="text-decoration: none; color:black;">
          &nbsp; Больше...
        </router-link>
    </el-row>
    
    <!-- <el-divider style="margin: 0;"/> -->
    <el-row alignment="flex-start">
      <el-col 
        v-for="o in movieList[3]"
        :key="o.id"
        :xs="8" :sm="4" :md="4" 
        style="padding: 9px;">
        <router-link :to="'/movdetail/'+ o.id" style="text-decoration: none;" target="_blank">
        <el-card
        class="box-card" 
        @click="selectMovie"
        shadow="hover"
        :body-style="{ padding: '8px 5px' }">
        <div class="card-div">
          <img :src="o.picture" class="card-image"/>
          <span class="card-remark">{{ o.name }}</span>
        </div>
      
        <div style="padding: 0px;">
          
          <span style="line-height: 26px; font-size: 15px; color:#777; display: flex; margin-top: 4px; text-overflow: ellipsis; overflow: hidden; width: 80%; white-space: nowrap;">
            <el-tooltip class="box-item" effect="dark" :content="o.name" placement="bottom-end" :show-after="1000">
            {{ o.remark }}
            </el-tooltip>
          </span>
          <!-- <div class="bottom">
            <p style="font-size:smaller; color:#777; margin: 4px 0">{{ o.vod_remarks }}</p>
          </div> -->
        </div>
      
      </el-card>
      </router-link>
      </el-col>
   </el-row>
  </div>
</template>

<script>
// 有限展示视频卡片列表
import apiGetMovList from '../apis/getMovInfo'
// import SakuraTypeButton from './SakuraTypeButton.vue'
import { useStore } from 'vuex'

export default {
    name: "MovLimitCard",
    props: {
        movtype: Number
    },
    components: {
    },

    setup() {
      const store = useStore()  // 该方法用于返回store 实例
      const type_id_names = {
        1: "Аниме",
        2: "Фильмы",
        3: "Сериалы",
        4: "Дорамы",
    }
      return {
            store,
            type_id_names
        }
    },

    data() {
      return {
        page: 1,
        contentshow: true,
        movieList: [
            ]
      }
    },

    methods: {
        selectMovie(h) {
            console.log(h)
        },

        getMovList() {
          const param =  { 
              page: this.page,
              movtype: this.movtype 
              }

          apiGetMovList(param).then(
            (res) => {
              if (res !== null) {
                  for (var i in res) {
                    this.movieList.push(res[i])
                 }
              } else {
                this.contentShow = false
              }
             }
          ).catch(
            () => {
                this.contentShow = false
            }
          )
      }
   },

   created() {
    this.getMovList()
   }

}
</script>


<style>
span.home-card-type {
    float: left;
    margin: 10px;
    font-size: 20px; 
    font-weight: bold;
    line-height: 20px;
}

.home-card-type {
    float: left;
    margin: 10px;
    line-height: 20px;
}

a.home-card-type:hover {
    color:rgb(36, 184, 242) !important;
}
</style>
