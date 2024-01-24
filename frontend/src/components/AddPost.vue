
<template>
<div>
  <div v-if="posts.length >= 0">
    <h2>Create a New Post</h2>
    <form @submit.prevent="createPost">
      <label for="title">Title:</label>
      <input v-model="post.title" type="text" required>

      <label for="content">Content:</label>
      <textarea v-model="post.content" required></textarea>

      <button type="submit">Create Post</button>
    </form>
  </div>
  <p v-else>You are not logged in.</p>
</div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      posts: [],
      post: {
        title: '',
        content: '',
        author: '',
        date: ''
      }
    }
  },
  methods: {
    createPost () {
      const jwtToken = localStorage.getItem('jwt')
      axios.post('http://localhost:5000/addpost', this.post, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`,
          'Content-Type': 'application/json'
        }
      })
        .then(response => {
          console.log(response.data.message)
          this.$router.push('/')
        })
        .catch(error => {
          console.log(jwtToken)
          console.error('Error creating post:', error.response.data)
          // Handle error, show a message, or redirect
          this.error = error.response.data.message // Example of showing an error message
        })
    }
  }
}
</script>
