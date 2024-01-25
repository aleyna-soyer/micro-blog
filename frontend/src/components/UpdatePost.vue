<template>
  <div>
    <h2>Post Update</h2>
    <form @submit.prevent="updatePost(postId)">
      <div class="block">
      <label for="title">Title:</label>
      <input v-model="title" id="title" type="text" required />
      </div>
      <div class="block">
      <label for="content">Content:</label>
      <textarea v-model="content" id="content" required></textarea>
      </div>
      <button type="submit">Update Post</button>
    </form>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      postId: this.$route.params.id,
      title: '',
      content: ''
    }
  },
  mounted () {
    this.fetchPosts(this.postId)
  },
  methods: {
    updatePost (postId) {
      axios.post(`http://localhost:5000/updatepost/${postId}`, {
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
    },
    fetchPosts (postId) {
        console.log(postId)
        const jwtToken = localStorage.getItem('jwt')
        axios.get(`http://localhost:5000/getpost/${postId}`, {
          headers: {
            Authorization: `Bearer ${jwtToken}`,
            'Content-Type': 'application/json'
          }
        })
          .then(response => {
            console.log(response)
            this.title = response.data.post.title
            this.content = response.data.post.content
          })
          .catch(error => {
            console.log(jwtToken)
            console.error('Error fetching posts:', error)
          })
      },
  },
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