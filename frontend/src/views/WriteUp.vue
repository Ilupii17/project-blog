<template>
  <section class="prose max-w-none p-6">
    <h2>Write Up</h2>
    <ul>
      <li v-for="post in posts" :key="post">
        <a href="#" @click.prevent="loadPost(post)" class="text-blue-600 hover:underline">
          {{ post }}
        </a>
      </li>
    </ul>

    <!-- Konten post ditampilkan di bawah -->
    <article v-if="currentPost.content" v-html="currentPost.content" class="mt-6"></article>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const posts = ref([])
const currentPost = ref({})

onMounted(async () => {
  try {
    const res = await axios.get("http://127.0.0.1:5000/posts")
    posts.value = res.data
  } catch (err) {
    console.error("Gagal load daftar post:", err)
  }
})

async function loadPost(name) {
  try {
    const res = await axios.get(`http://127.0.0.1:5000/posts/${name}`)
    currentPost.value = res.data
  } catch (err) {
    console.error("Gagal load post:", err)
  }
}
</script>
