<template>
  <div>
    <h2>Home Page</h2>
    <button @click="logout">Logout</button>
    <ul>
      <li v-for="post in posts" :key="post._id">
        <router-link :to="{ name: 'PostDetail', params: { id: post._id }}">
          {{ post.title }}
        </router-link>
      </li>
    </ul>
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
    logout () {
      const jwtToken = localStorage.getItem('jwt')
      axios.delete('http://localhost:5000/logout', {
        headers: {
          Authorization: `Bearer ${jwtToken}`,
          'Content-Type': 'application/json'
        }
      })
        .then(response => {
          console.log('Current Token:', jwtToken)
          localStorage.removeItem('jwt')
          this.$router.push({name: 'Login'})
        })
        .catch(error => {
          console.error('Error logout:', error)
        })
      console.log('Current Token:', jwtToken)
    },
    fetchPosts () {
      axios.get('http://localhost:5000/getposts')
        .then(response => {
          this.posts = response.data.posts
        })
        .catch(error => {
          console.error('Error fetching posts:', error)
        })
    }
  }
}
</script>

<style>
/* Genel stiller */
body {
  font-family: sans-serif;
  margin: 0;
  padding: 20px;
}

h2 {
  margin-bottom: 15px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}

a {
  text-decoration: none;
  color: #333;
}

/* Router-link stilleri */
.router-link-active {
  font-weight: bold;
}
</style>
