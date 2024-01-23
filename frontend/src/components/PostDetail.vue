<template>
  <div>
    <h2>{{ post.title }}</h2>
    <p>Author: {{ post.author }}</p>
    <p>Date: {{ post.date }}</p>
    <p>{{ post.content }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      post: null
    }
  },
  created () {
    this.fetchPostDetails()
  },
  methods: {
    fetchPostDetails () {
      axios.get(`http://localhost:5000/getpostbyauthor`)
        .then((response) => {
          this.post = response.data
        })
        .catch((error) => {
          console.error('Error fetching post details:', error)
        })
    }
  }
}
</script>
