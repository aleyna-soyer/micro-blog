
<template>
<div>
  <div>
    <h2>Create a New Post</h2>
    <form @submit.prevent="createPost">
      <div class="block">
      <label for="title">Title:</label>
      <input v-model="post.title" type="text" required>
      </div>
      <div class="block">
      <label for="content">Content:</label>
      <textarea v-model="post.content" required></textarea>
      </div>
      <button type="submit">Create Post</button>
    </form>
  </div>
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
  created () {
    const jwtToken = localStorage.getItem('jwt')
    if (!jwtToken){
      this.$router.push('/login')
    }
  },
  methods: {
    createPost () {
      const jwtToken = localStorage.getItem('jwt')
      console.log(jwtToken)
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

<style scoped>
textarea{
  height: 20em;
  width: 40em;
}
.block{

display: block;
margin: 1em;

}
</style>
