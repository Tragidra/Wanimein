<template>
    <el-row>
        <el-form size="large"
                id="comment-form"
                 :model="commentForm" 
                 class="demo-form-inline"
                 label-position="top"
                 style="width: 100%;"
                 label-width="100px">
            <el-form-item label="Комментарии">
                <el-input v-model="commentForm.body" placeholder="Пожалуйста, напишие комментарий" type="textarea" :rows="4"/>
            </el-form-item>
            <el-form-item style="float:left;">
                <el-button type="primary" @click="publishComment">Сохранить</el-button>
            </el-form-item>
        </el-form>
    </el-row>

    <div v-for="(comment, i) in comments" :key="i" class="comment">
        <el-divider />
        <el-row class="comment-username" :id="comment.id">
          <el-avatar v-if="this.store.state.appStore.isLogining"
            src="https://e7.pngegg.com/pngimages/120/500/png-clipart-european-rabbit-cuteness-icon-cartoon-rabbit-cartoon-character-animals.png"
          />
          <el-avatar v-else
            src="https://e7.pngegg.com/pngimages/575/117/png-clipart-rabbit-drawing-rabbit-white-face-thumbnail.png"
          />
            {{ comment.author_name }} &nbsp;&nbsp; {{comment.createdAt }}
            <el-button link style="position:absolute; right: 10%" @click="showReplyForm">Ответить</el-button>
        </el-row>
        <!-- 评论内容 -->
        <el-row class="comment-p" style="padding: 10px" >
            {{ comment.text }}
        </el-row>
        <!-- 回复框 -->
        <el-row class="comment-reply-form" style="display: none" :id="'reply-' + comment.id">
            <el-form  :model="replyComment" size="small" style="width: 100%;">
                <el-form-item label="">
                    <el-input v-model="replyComment.body" placeholder="Ответ:" type="textarea" :rows="3" />
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="replyCommentPost">Ответить</el-button>
                </el-form-item>
            </el-form>
        </el-row>
        <!-- 此评论的回复 -->
        <div v-for="(reply, j) in comment.reply_list" :key="j" class="comment-replay">
            <el-row class="comment-username" :id="reply.id">
                {{ reply.user_name }} &nbsp;ответил&nbsp; {{reply.reply_user_name }} &nbsp;&nbsp; {{ reply.time }}
                <el-button link style="position:absolute; right: 10%" @click="showReplyForm">Ответить</el-button>
            </el-row>
            <el-row class="comment-p" style="padding: 10px" >{{ reply.body }}</el-row>
            <el-row class="comment-reply-form" style="display: none" :id="'reply-' + reply.id">
                <el-form  :model="replyComment" size="small" style="width: 100%;">
                    <el-form-item label="">
                      <el-input v-model="replyComment.body" placeholder="Ответ:" type="textarea" :rows="3" />
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="replyCommentPost">Ответить</el-button>
                    </el-form-item>
                </el-form>
            </el-row>
        </div>
    </div>
    
</template>

<script>
import { reactive } from 'vue'
import { useStore } from 'vuex'
import { ElMessage } from 'element-plus'
import { postComments, showComments, replyComment } from '../apis/comments'

export default {
    // 评论组件
    name: 'Comment',
    setup() {
        const store = useStore()
        
        const commentForm = reactive({
                body: '',
                user: '',
            })

        const replyComment = reactive({
                body: '',
                user: ''
            })

        return {
            store,
            commentForm,
            replyComment
        }
    },

    props: {
        vod_id: String
    },

    data() {
        return {
            comments:  [],
        }
    },

    methods: {
        publishComment() {
            if (this.store.state.appStore.isLogining) {
                this.commentForm.user_id = this.store.state.appStore.user.id;
                var params = {
                movie_details: this.vod_id,
                author: this.commentForm.user_id,
                text: this.commentForm.body,
                respondent: null
                };
                postComments(params).then(
                    res => {
                        if (res.results !== null) {
                            this.showVodComment()
                            this.commentForm.body = ''
                        } else {ElMessage({
                                    message: 'Что-то пошло не так, попробуйте ещё раз позднее',
                                    type: 'warning',
                                    })}
                                }
                            )
            } else {
                ElMessage({
                message: "Пожалуйста, войдите в свой аккаунт",
                type: 'warning',
                })
            }
        },

        showVodComment() {
            var params = {
              movie_details: this.vod_id
            };
            showComments(params).then(
                res => {
                    if (res.results !== null) {
                        this.comments = res.results
                    } else {
                        ElMessage({
                                    message: 'Что-то пошло не так, комментарии не смогли прогрузиться',
                                    type: 'warning',
                                    })}
                                }
                            )
                },

        showReplyForm(e) {
            this.replyComment.body = ''
            var forms = document.getElementsByClassName("comment-reply-form")
            for (var i in forms) {
                if (typeof(forms[i])=="object" && forms[i].style.display == "block") {
                    forms[i].style.display = "none"
                }
            }
            var comment_id = 'reply-' + e.currentTarget.parentElement.id
            document.getElementById(comment_id).style.display = "block"
        },

        replyCommentPost(e) {
            
            if (this.store.state.appStore.isLogining) {
                // loginStatusToReplyToComments
                var comment_id = e.currentTarget.parentElement.parentElement.parentElement.parentElement.id.split('-')[1];
                this.replyComment.user_id = this.store.state.appStore.user.id;
                var params = {
                  respondent: comment_id,
                  author: this.replyComment.user_id,
                  text: this.replyComment.body,
                  movie_details: this.vod_id
                };
                replyComment(params).then(
                    res => {
                        if (res.results !== null) {
                            this.replyComment.body = ''
                            this.showVodComment()
                        } else {ElMessage({
                                    message: 'Что-то пошло не так, комментарий не был отправлен',
                                    type: 'warning',
                                    })}
                                }
                            )
            } else {
                ElMessage({
                message: "Пожалуйста, войдите в свой аккаунт",
                type: 'warning',
                })
            }
        }
            
        },

    created() {
        this.showVodComment()
    }

   
}
</script>

<style>
#comment-form .el-form-item__label {
  font-size: 18px;
  font-weight: bold;
}


.el-row.comment-username {
    color: #777888;
}

div.comment-replay {
    padding-left: 3%;
}
</style>