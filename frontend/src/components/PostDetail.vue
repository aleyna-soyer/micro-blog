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
    <form @submit.prevent="addComment()">
      <label for="comment">Comment:</label>
        <textarea v-model="my_comment" id="comment" required></textarea>
        <button type="submit">Add Comment</button>
      </form>
</div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      post: {},
      id: this.$route.params.id,
      comment: [],
      my_comment: ''
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
    addComment () {
      axios.post(`http://localhost:5000/addcomment/${this.id}`,{
        text: this.my_comment,
      },
    {
      headers: {
            Authorization: `Bearer ${localStorage.getItem('jwt')}`,
            'Content-Type': 'application/json'
          }
    }
      )
      .then((response) => 
        this.$router.go()
      )
    },
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
