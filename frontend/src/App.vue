<template>
  <div class="max-w-3xl mx-auto p-6">
    <h1 class="text-3xl font-bold mb-4">My Blog</h1>
    <PostList :posts="posts" @select="loadPost" />
    <hr class="my-6" />
    <PostContent :post="currentPost" />
  </div>
</template>

<script>
import axios from 'axios'
import PostList from './components/PostList.vue'
import PostContent from './components/PostContent.vue'

export default {
  components: { PostList, PostContent },
  data() {
    return { posts: [], currentPost: {} }
  },
  async mounted() {
    const res = await axios.get("http://127.0.0.1:5000/posts")
    this.posts = res.data
    if (this.posts.length > 0) this.loadPost(this.posts[0])
  },
  methods: {
    async loadPost(name) {
      const res = await axios.get(`http://127.0.0.1:5000/posts/${name}`)
      this.currentPost = res.data
    }
  }
}
</script>
