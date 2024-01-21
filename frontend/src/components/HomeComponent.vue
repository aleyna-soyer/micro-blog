<template>
  <div class="center-content">
    <h2>Home Page</h2>
    <button @click="logout">
      <span>Logout</span>
    </button>
    <table>
    <thead>
      <tr>
        <th>POSTS</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="post in posts" :key="post._id">
        <td>
          <router-link :to="{ name: 'PostDetail', params: { id: post._id }}">
            {{ post.title }}
          </router-link>
        </td>
      </tr>
    </tbody>
</table>

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

<style scoped>

.center-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.home-page {
  font-family: 'Arial', sans-serif;
  margin: 20px;
}

h2 {
  margin-bottom: 15px;
}

button {
  padding: 8px 16px;
  background-color: #3498db;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  position: absolute;

      right: 10px;
      top: 10px;
}

ul.post-list {
  list-style: none;
  padding: 0;
}

li.post-item {
  margin-bottom: 10px;
}

router-link.post-link {
  text-decoration: none;
  color: #333;
  font-size: 16px;
  display: inline-block;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

router-link.post-link:hover {
  background-color: #f4f4f4;
}

/* Router-link stilleri */
.router-link-active {
  font-weight: bold;
}

  table {
    border-collapse: collapse;
    width: 50%;
    margin-bottom: 200px;
  }

  th, td {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
  }

  th {
    background-color: #f2f2f2;
  }
</style>
