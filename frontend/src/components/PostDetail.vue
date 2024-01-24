<template>
  <div>
    <h2>{{ post.title }}</h2>
    <p>Author: {{ post.author }}</p>
    <p>Date: {{ post.date }}</p>
    <p>Entry: {{ post.content }}</p>
     <div v-if="comment && comment.length > 0" v-for="c in comment" :key="c.id">
      <p>Comment: {{ c.comment }}</p>
    </div>
    <p v-else>No comments</p>
</div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      post: {},
      id: this.$route.params.id,
      comment: []
    }
  },
  created () {
    console.log(this.id)
    this.fetchPost(this.id)
  },
  mounted () {
    this.fetchComment(this.id)
  },
  methods: {
    fetchComment (id) {
      axios.get(`http://localhost:5000/getcomment/${id}`)
        .then((response) => {
          this.comment = response.data.comments
          console.log(response.data)
        })
        .catch((error) => {
          console.error('Error fetching comments:', error)
        })
    },
    fetchPost (id) {
      axios.get(`http://localhost:5000/getpost/${id}`)
        .then((response) => {
          this.post = response.data.post
          console.log(this.$route.params.id)
        })
        .catch((error) => {
          console.error('Error fetching post:', error)
        })
    }
  }
}
</script>
