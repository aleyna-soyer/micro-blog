<template>
  <div>
    <h2>Yazarınızın Gönderileri</h2>
    <ul v-if="posts.length > 0">
      <li v-for="post in posts" :key="post._id">
        <h3>{{ post.title }}</h3>
        <p>{{ post.content }}</p>
        <p>ID: {{ post._id }}</p>
        <button @click="deletePost(post._id)">Delete</button>
      </li>
    </ul>
    <p v-else>Yayınlanmış gönderiniz yok.</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      posts: []
    }
  },
  created () {
    this.fetchPosts()
  },
  methods: {
    fetchPosts () {
      const jwtToken = localStorage.getItem('jwt')
      axios.get('http://localhost:5000/getpostbyauthor', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`,
          'Content-Type': 'application/json'
        }
      })
        .then(response => {
          this.posts = response.data.posts
        })
        .catch(error => {
          console.log(jwtToken)
          console.error('Error fetching posts:', error)
        })
    },
    deletePost (postId) {
      axios
        .delete('http://localhost:5000/deletepost', {
          data: { _id: postId },
          headers: {
            Authorization: `Bearer ${localStorage.getItem('jwt')}`,
            'Content-Type': 'application/json'
          }
        })
        .then((response) => {
          console.log(response.data)
          // If you want to update the list after deletion, you can call fetchPosts() again
          this.fetchPosts()
        })
        .catch((error) => {
          console.error('Error deleting post:', error)
        })
    }
  }
}

</script>
