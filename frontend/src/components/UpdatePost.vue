<template>
  <div>
    <h2>Post Update</h2>
    <form @submit.prevent="updatePost">
      <label for="postId">Post ID:</label>
      <input v-model="postId" id="postId" type="text" required />

      <label for="title">Title:</label>
      <input v-model="title" id="title" type="text" required />

      <label for="content">Content:</label>
      <textarea v-model="content" id="content" required></textarea>

      <button type="submit">Update Post</button>
    </form>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      postId: '',
      title: '',
      content: ''
    }
  },
  methods: {
    updatePost () {
      axios.post('http://localhost:5000/updatepost', {
        _id: this.postId,
        title: this.title,
        content: this.content
      },
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`,
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          console.log(response.data.message)
          this.$router.push('/')
        })
        .catch((error) => {
          console.error('Error updating post:', error)
        })
    }
  }
}
</script>
