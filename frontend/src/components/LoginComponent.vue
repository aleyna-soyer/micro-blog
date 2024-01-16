<template>
  <div>
    <form @submit.prevent="submitForm">
      <label for="username">Username:</label>
      <input type="text" v-model="username" id="username" name="username">

      <label for="password">Password:</label>
      <input type="password" v-model="password" id="password" name="password">

      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      username: '',
      password: '',
      jwt: ''
    }
  },
  methods: {
    submitForm () {
      axios.post('http://localhost:5000/login', {
        username: this.username,
        password: this.password
      })
        .then(response => {
          this.jwt = response.data.token
          localStorage.setItem('jwt', this.jwt)
          console.log(this.jwt)
          this.$router.push('/')
        })
        .catch(error => {
          console.error('Error:', error)
        })
    }
  }
}
</script>

<style scoped>
.login-form {
  max-width: 300px;
  margin: 0 auto;
  background-color: #f4f4f4;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
}

label {
  display: block;
  margin-bottom: 5px;
  font-size: 14px;
  color: #333;
}

input, button {
  width: 10%;
  padding: 8px;
  margin-bottom: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 3px;
  box-sizing: border-box;
}

button {
  background-color: #4caf50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  font-size: 14px;
  width: 10%;
  display: block;
  box-sizing: border-box;
  margin: 0 auto;
}

button:hover {
  background-color: #45a049;
}
</style>
