<template>
  <el-menu
    :default-active="activeIndex"
    background-color="white"
    text-color="black"
    active-text-color="#24b8f2"
    :router="true"
    class="el-menu-demo"
    mode="horizontal"
    :ellipsis="false"
    @select="handleSelect"
  >
    <el-menu-item index="/" style="font-size:larger; color:#409EFF; ">Wanimein</el-menu-item>
    <el-menu-item index="/movtype/1">Аниме</el-menu-item>
    <el-menu-item index="/movtype/2">Фильмы</el-menu-item>
    <el-menu-item index="/movtype/3">Сериалы</el-menu-item>
    <el-menu-item index="/movtype/4">Дорамы</el-menu-item>
    <!-- <el-menu-item index="/movtype/5">社区</el-menu-item> -->
    <div class="menu-input">
      <el-input
        v-model="input"
        placeholder="Поиск"
        style = "width: 80%; margin-left: 3%"
        @keyup.enter="searchChange"
        :suffix-icon="Search"
      />
    </div>
    <div class="user-info-container" style = "width: 60%; margin-left: 3%">
      <div class="flex-grow"></div> <!-- Расширяющийся элемент, чтобы выравнивать элементы по краям -->
      <div class="avatar-profile-container">
        <div class="avatar-container">
          <el-avatar v-if="isLogining"
            src="https://e7.pngegg.com/pngimages/120/500/png-clipart-european-rabbit-cuteness-icon-cartoon-rabbit-cartoon-character-animals.png"
          />
          <el-avatar v-else
            src="https://e7.pngegg.com/pngimages/575/117/png-clipart-rabbit-drawing-rabbit-white-face-thumbnail.png"
          />
        </div>
        <div class="username-container">
          <el-dropdown class="login-out" style="margin: 15px 11px" v-if="isLogining"  trigger="click">
            <span class="el-dropdown-link">
              {{ user.login }}
              <el-icon class="el-icon--right"><arrow-down /></el-icon>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item>
                  <router-link :to="'/personSapce/'+ user.id" style="text-decoration: none; color: #606266">Профиль</router-link>
                </el-dropdown-item>
                <el-dropdown-item @click="loginOut">
                  Выйти
                </el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>

          <el-button link type="primary" class="login" style="margin: 15px 11px; color: black" v-else @click="login">
            Войти
          </el-button>
        </div>
      </div>
    </div>
  </el-menu>
</template>

<script>
// 导航栏
import { ref } from 'vue'
import { Search } from '@element-plus/icons-vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import {localGet, localRemove} from '../utils'
import { getUserInfo } from '../apis/login'
import { ElMessage } from 'element-plus'


export default {
    name: "HeaderMenu",
    setup() {
        const store = useStore()
        const router = useRouter()
        // console.log(router.currentRoute.value)
        const activeIndex = ref('/')
        // console.log(activeIndex.value)
        // console.log(router.currentRoute.value)
        const input = ref('')
        const isLogining = ref(store.state.appStore.isLogining)

        const loginOut = function() {
          localRemove('tokenwanimein')
          window.location.reload()
        }

        const login = function() {
          router.push({ name: 'login' })
        }

        return {
            router,
            activeIndex,
            input,
            store,
            isLogining,
            loginOut,
            login,
            Search
            }
    },

    data() {
      return {
        user: {}
      }
    },

    methods: {
        handleSelect(key, keyPath)  {
            // console.log(key)
            this.activeIndex = key
            this.input = ''
          },

        // 输入框输入数据时 路由改变
        searchChange(value) {
          if(this.input) {
            this.activeIndex = '/'
            this.router.push({ name: 'search', query: { keyword: this.input }})
          }
        },

        getUserInfo() {
          if (this.isLogining) {
            var param = {
              token: localGet('tokenwanimein')
            }
            getUserInfo(param).then(
              (res) => {
                // console.log(res.data)
                if (res.results !== null) {
                  this.store.state.appStore.user = res.results[0]
                  this.user = this.store.state.appStore.user

                } else {
                ElMessage({
                message: 'Что-то пошло не так, попробуйте позднее',
                type: 'warning',
                })
            }
              }
            )
          }
        },

        ToUserCenter() {
          console.log("Перейти в поддержку")
          this.router.push({name: 'personSapce'})
        }

    },


    mounted() {
      this.router.isReady().then(
        () => {
          var currentPath = this.$route.fullPath
          if (currentPath.indexOf('search?keyword=') > -1) {
            this.input = this.$route.query.keyword ? this.$route.query.keyword : ''
          } else if (currentPath.indexOf('/movtype/') > -1) {
            this.activeIndex = currentPath
          }
        }
        ).catch(
          () => {
            this.input = ''
            this.activeIndex = '/'
          }
        )
    },

    created() {
      //Идея со стором не сработала, позже оптимизировать запрос путём кэширования
      if (Object.keys(this.store.state.appStore.user).length === 0){
        const token = localGet('tokenwanimein');
        if (token !== null){
          this.getUserInfo()
        }
      } else {
        this.user = this.store.state.appStore.user
      }
    },

    watch: {
      moniterLogining() {
        return this.store.state.appStore.isLogining
      }
    },

    computed: {
      moniterLogining() {
        this.isLogining = this.store.state.appStore.isLogining
      }
    }
}


</script>

<style>
.user-info-container {
  display: flex;
  align-items: center;
  flex-shrink: 0;
}

.flex-grow {
  flex-grow: 1;
}

.avatar-profile-container {
  display: flex;
  align-items: center;
}

.avatar-container {
  margin-right: 10px;
}

.flex-grow {
  flex-grow: 1;
}
.username-container {
  /* Дополнительные стили для имени пользователя могут быть добавлены здесь */
  flex-shrink: 0; /* Запрет уменьшения размера блока */
}
/* Отмена эффекта перехода */
.el-menu-item {
  border-bottom: 0 !important;
}

.el-menu-item.is-active {
  background-color: white !important;
  border-bottom: 0 !important;
}

.el-menu-item:focus {
  background-color: white !important;
}

.el-menu-item:hover {
  background-color: white !important;
  color: #24b8f2 !important;
}

/* .el-button.login:hover {
  color: #24b8f2
}

p.login-out:hover {
  color: #24b8f2
} */

.el-menu {
  border: none !important;
  height: 100%;
  position: relative;
}

.el-input {
  margin: 10px 0px;
}

div.menu-input {
  position: absolute;
  right: 10%;
  width: 25%;
}
</style>
