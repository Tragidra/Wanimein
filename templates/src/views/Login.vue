<template>
  <div class="login-body">
    <div class="login-container">
      <div class="head">
        <div class="name">
          <div class="title">Animein</div>
          <div class="tips">Все онгоинги в одном месте</div>
        </div>
      </div>
      <el-form label-position="top" :rules="rules" :model="ruleForm" ref="loginForm" class="login-form">
        <el-form-item label="Никнейм" prop="username">
          <el-input type="text" v-model.trim="ruleForm.username" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Пароль" prop="password">
          <el-input type="password" v-model.trim="ruleForm.password" autocomplete="off"></el-input>
        </el-form-item>

        <el-form-item v-if="haveAccount">
          <el-button type="primary" link style="margin-bottom:10px" @click="registerAccount">Ещё нет аккаунта?</el-button>
          <el-button style="width: 100%" type="primary" @click="submitForm">Войти</el-button>
          <el-checkbox v-model="checked" @change="!checked">Запомнить меня</el-checkbox>
        </el-form-item>

        <el-form-item v-else>
          <el-button style="width: 100%" type="primary" @click="submitRegisterForm">Регистрация</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
// 登录页
import { reactive, ref, toRefs } from 'vue'
import { useStore } from 'vuex'
import { localSet } from '../utils'
import login from '../apis/login'
import { register } from '../apis/login'
import { ElMessage } from 'element-plus'

export default {
  name: 'Login',
  setup() {
    const loginForm = ref(null)
    const haveAccount = ref(true)
    const store = useStore()
    const state = reactive({
      ruleForm: {
        username: '',
        password: ''
      },
      checked: true,
      rules: {
        username: [
          { required: 'true', message: 'Никнейм не может быть пустым', trigger: 'blur' }
        ],
        password: [
          { required: 'true', message: 'Пароль не может быть пустым', trigger: 'blur' }
        ]
      }
    })

    const submitForm = async () => {
        // 执行登录操作
      loginForm.value.validate((valid) => {
        if (valid) {
          login({
            login: state.ruleForm.username || '',
            password: state.ruleForm.password,
            ip: window.location.host,
          }).then(res => {
            if (res.results !== null) {
                localSet('token', res.data.token)
                window.location.href = '/'
            } else {
                ElMessage({
                message: res.data.message,
                type: 'warning',
                })
            }
          })
        } else {
          console.log('error login!!')
          return false;
        }
      })
    }

    const submitRegisterForm =  async () => {
        // 执行注册账户操作
      loginForm.value.validate((valid) => {
        if (valid) {
          register({
            name: state.ruleForm.username,
            password: state.ruleForm.password,
            ip:  window.location.host
          }).then(res => {
            if (res.results !== null) {
                ElMessage({
                message: 'Регистрация успешно завершена',
                type: 'success',
                })
                haveAccount.value = true
                // setTimeout(() => {
                //     haveAccount = true
                // }, 4000);
                
            } else {
                ElMessage({
                message: 'Что-то пошло не так, попробуйте снова',
                type: 'warning',
                })
            }
          })
        } else {
          console.log('error register!!')
          return false;
        }
      })
    }

    const resetForm = () => {
      loginForm.value.resetFields();
    }

    return {
      ...toRefs(state),
      haveAccount,
      loginForm,
      submitForm,
      submitRegisterForm,
      resetForm
    }
  },


  methods: {
    registerAccount() {
        this.haveAccount = false
    }
  }
}
</script>

<style scoped>
  .login-body {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    padding: 5px;
    background-color: #fff;
    /* background-image: linear-gradient(25deg, #077f7c, #3aa693, #5ecfaa, #7ffac2); */
  }
  .login-container {
    width: 420px;
    height: 500px;
    background-color: #fff;
    border-radius: 4px;
    box-shadow: 0px 21px 41px 0px rgba(0, 0, 0, 0.2);
  }
  .head {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 40px 0 20px 0;
  }
  .head img {
    width: 100px;
    height: 100px;
    margin-right: 20px;
  }
  .head .title {
    font-size: 28px;
    color: #409EFF;
    font-weight: bold;
  }
  .head .tips {
    font-size: 12px;
    color: #999;
  }
  .login-form {
    width: 70%;
    margin: 0 auto;
  }
</style>
<style>
  .el-form--label-top .el-form-item__label {
    padding: 0;
  }
  .login-form .el-form-item {
    margin-bottom: 12px;
  }
</style>