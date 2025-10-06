<template>
  <div>
    <h1>Daftar Post</h1>
    <ul>
      <li v-for="post in posts" :key="post">
        <a href="#" @click.prevent="loadPost(post)">{{ post }}</a>
      </li>
    </ul>

    <hr />

    <!-- Render konten HTML -->
    <div v-if="currentPost.content" v-html="currentPost.content"></div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data() {
    return {
      posts: [],
      currentPost: {}
    }
  },
  async mounted() {
    try {
      const res = await axios.get("http://127.0.0.1:5000/posts")
      this.posts = res.data
      if (this.posts.length > 0) {
        this.loadPost(this.posts[0]) // otomatis load post pertama
      }
    } catch (err) {
      console.error("Gagal fetch daftar post:", err)
    }
  },
  methods: {
    async loadPost(name) {
      try {
        const res = await axios.get(`http://127.0.0.1:5000/posts/${name}`)
        this.currentPost = res.data
      } catch (err) {
        console.error("Gagal fetch post:", err)
      }
    }
  }
}
</script>
