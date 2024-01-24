<template>
  <div>
    <h2>My Posts</h2>
    <button @click="addPost()" class="add">Add Post</button>
    <ul v-if="posts.length > 0">
      <li v-for="post in posts" :key="post.id">
        <h3>{{ post.title }}</h3>
        <p>{{ post.content }}</p>
        <p>ID: {{ post.id }}</p>
        <button @click="deletePost(post.id)">Delete</button>
        <router-link :to="`/UpdatePost/${post.id}`" >
          <button>Update</button>
        </router-link>
      </li>
    </ul>
    <p v-else> Any post </p>
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
    const jwtToken = localStorage.getItem('jwt')
    if (!jwtToken){
      this.$router.push('/login')
    }
    else {
      this.fetchPosts()
    }
  },
  methods: {
    addPost () {
      this.$router.push({ name: 'AddPost' })
    },
    fetchPosts () {
      const jwtToken = localStorage.getItem('jwt')
      axios.get('http://localhost:5000/getpostbyauthor', {
        headers: {
          Authorization: `Bearer ${jwtToken}`,
          'Content-Type': 'application/json'
        }
      })
        .then(response => {
          this.posts = response.data.posts
          console.log(response)
        })
        .catch(error => {
          console.log(jwtToken)
          console.error('Error fetching posts:', error)
        })
    },
    deletePost (postId) {
      axios.delete(`http://localhost:5000/deletepost/${postId}`, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`,
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          console.log(response.data)
          this.fetchPosts()
        })
        .catch((error) => {
          console.error('Error deleting post:', error)
        })
    },
    updatePost (postId) {
      this.$router.push({ name: 'UpdatePost', params: postId})
    }
  }
}

</script>

<style scoped>

.add{
  background-color: #D2691E;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  font-size: 14px;
  width: 5%;
  display: block;
  box-sizing: border-box;
  margin: 0 auto;
}

body {
  background-color: #f5f5f5;
}

ul {
  max-width: 600px;
  margin: 0 auto;
}

</style>