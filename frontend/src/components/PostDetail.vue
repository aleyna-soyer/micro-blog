<template>
  <div>
    <h2 class="post-title">{{ post.title }}</h2>
    <p class="post-detail"><span class="label">AUTHOR:</span> {{ post.author }}</p>
    <p class="post-detail"><span class="label"></span> {{ post.content }}</p>

    <button @click="votes('1')">Like({{ this.like }})</button>
    <button @click="votes('0')">Dislike({{ this.dislike }})</button>

    <div v-if="comment && comment.length > 0" v-for="c in comment" :key="c.id">
      <p class="comment"><span class="label">COMMENT:</span> {{ c.comment }}</p>
    </div>

    <p v-else class="no-comments">No comments</p>

    <form @submit.prevent="addComment()" class="labelc">
      <label for="comment"><span class="label">COMMENT:</span></label>
      <textarea v-model="my_comment" id="comment" required></textarea>
      <button type="submit">Add Comment</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      post: {},
      id: this.$route.params.id,
      comment: [],
      my_comment: '',
      like: '0',
      dislike: '0'
    }
  },
  created() {
    console.log(this.id)
    this.fetchPost(this.id)
    this.fetchVote()
  },
  mounted() {
    this.fetchComment(this.id)
  },
  methods: {
    fetchVote () {
      axios.get(`http://localhost:5000/getvote/${this.id}`)
      .then((response) => 
      {
        this.like = response.data.Like
        this.dislike = response.data.Dislike
        console.log(response.data)
      }
      )
    },
    votes(vote) {
      axios.post(`http://localhost:5000/addvote/${this.id}`, {
        vote:vote
      },
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('jwt')}`,
          'Content-Type': 'application/json'
        }
      }
      )
        .then((response) =>
          {
            
          }
        )
        .catch((error) => {
        console.error('Error vote:', error)
      })
    },
  addComment() {
    axios.post(`http://localhost:5000/addcomment/${this.id}`, {
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
  fetchComment(id) {
    axios.get(`http://localhost:5000/getcomment/${id}`)
      .then((response) => {
        this.comment = response.data.comments
      })
      .catch((error) => {
        console.error('Error fetching comments:', error)
      })
  },
  fetchPost(id) {
    axios.get(`http://localhost:5000/getpost/${id}`)
      .then((response) => {
        this.post = response.data.post
      })
      .catch((error) => {
        console.error('Error fetching post:', error)
      })
  },
}
}
</script>

<style scoped>

.labelc{
  margin-top: 1em;
}

div {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.post-title {
  color: #333;
  font-size: 24px;
  margin-bottom: 10px;
}

.post-detail,
.comment {
  white-space: pre-wrap;
  overflow-y: auto;
  overflow-x: hidden;
  max-height: 300px;
  margin-bottom: 20px;
}

.label {
  font-weight: bold;
  margin-right: 5px;
}

textarea {
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
  resize: vertical;
  margin-bottom: 10px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

.no-comments {
  margin-top: 10px;
}
</style>
