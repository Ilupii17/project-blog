<template>
  <div class="min-h-screen bg-slate-700 py-12">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Back Button -->
      <button 
        @click="$router.go(-1)"
        class="mb-6 text-gray-300 hover:text-white flex items-center space-x-2 transition-colors"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
        </svg>
        <span>Back</span>
      </button>

      <!-- Loading State -->
      <div v-if="loading" class="text-center text-gray-300">
        <p>Loading post...</p>
      </div>

      <!-- Post Content -->
      <article v-else-if="post" class="bg-slate-800 rounded-lg shadow-lg p-8">
        <h1 class="text-4xl font-bold text-white mb-6">{{ formatTitle(post.title) }}</h1>
        <div class="markdown-content" v-html="post.content"></div>
      </article>

      <!-- Error State -->
      <div v-else class="text-center text-red-400">
        <p>Post not found</p>
      </div>
    </div>
  </div>
</template>

<script>
import { api } from '../services/api';

export default {
  name: 'PostDetail',
  data() {
    return {
      post: null,
      loading: true
    };
  },
  async mounted() {
    await this.loadPost();
  },
  methods: {
    async loadPost() {
      this.loading = true;
      const postName = this.$route.params.name;
      this.post = await api.getPost(postName);
      this.loading = false;
    },
    formatTitle(filename) {
      return filename.replace('.md', '').replace(/-/g, ' ');
    }
  },
  watch: {
    '$route.params.name': 'loadPost'
  }
};
</script>