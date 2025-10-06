<template>
  <div class="min-h-screen bg-slate-700">
    <!-- Hero Section -->
    <section class="bg-gradient-to-b from-slate-800 to-slate-700 py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <p class="text-gray-300 text-xl mb-4">Random post about CyberSecurity</p>
          <div class="max-w-3xl mx-auto">
            <p class="text-gray-200 text-lg leading-relaxed">
              Hi! I'm Ilupii. This is my blog where post stuff I want to write about (mostly cybersecurity).
              I'm a CTF player that currently plays with LastSeenIn2026, and my main category is pwn.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Posts Section -->
    <section class="py-12">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-white mb-8">Latest Posts</h2>
        
        <!-- Loading State -->
        <div v-if="loading" class="text-center text-gray-300">
          <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-white"></div>
          <p class="mt-4">Loading posts...</p>
        </div>

        <!-- Posts Grid -->
        <div v-else-if="posts.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <PostCard 
            v-for="post in posts" 
            :key="post.filename"
            :post="post"
            @click="viewPost(post.filename)"
          />
        </div>

        <!-- Empty State -->
        <div v-else class="text-center text-gray-300 py-12">
          <p>No posts available yet.</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { api } from '../services/api';
import PostCard from '../components/PostCard.vue';

export default {
  name: 'Home',
  components: {
    PostCard
  },
  data() {
    return {
      posts: [],
      loading: true
    };
  },
  async mounted() {
    await this.loadPosts();
  },
  methods: {
    async loadPosts() {
      this.loading = true;
      try {
        const data = await api.getPosts();
        
        // Handle both array of strings and array of objects
        this.posts = data.map(item => {
          if (typeof item === 'string') {
            return {
              filename: item,
              title: null,
              description: null,
              date: null
            };
          }
          return item;
        });
      } catch (error) {
        console.error('Error loading posts:', error);
        this.posts = [];
      } finally {
        this.loading = false;
      }
    },
    viewPost(filename) {
      if (filename) {
        this.$router.push(`/post/${filename}`);
      }
    }
  }
};
</script>