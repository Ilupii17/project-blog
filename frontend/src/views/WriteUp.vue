<template>
  <div class="min-h-screen bg-slate-700 py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-4xl font-bold text-white mb-8">WriteUps</h1>
      
      <!-- Loading State -->
      <div v-if="loading" class="text-center text-gray-300">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-white"></div>
        <p class="mt-4">Loading writeups...</p>
      </div>

      <!-- WriteUps Grid -->
      <div v-else-if="writeups.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <PostCard 
          v-for="writeup in writeups" 
          :key="writeup.filename"
          :post="writeup"
          @click="viewPost(writeup.filename)"
        />
      </div>

      <!-- Empty State -->
      <div v-else class="text-center text-gray-300 py-12">
        <svg class="w-24 h-24 mx-auto mb-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
        </svg>
        <p>No writeups available yet.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { api } from '../services/api';
import PostCard from '../components/PostCard.vue';

export default {
  name: 'WriteUp',
  components: {
    PostCard
  },
  data() {
    return {
      writeups: [],
      loading: true
    };
  },
  async mounted() {
    await this.loadWriteups();
  },
  methods: {
    async loadWriteups() {
      this.loading = true;
      const filenames = await api.getPosts();
      
      // Transform to post objects
      const allPosts = filenames.map(item => {
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
      
      // Show all posts or filter for writeups
      this.writeups = allPosts;
      
      // Uncomment to filter only writeups:
      // this.writeups = allPosts.filter(post => 
      //   post.filename.toLowerCase().includes('writeup') || 
      //   post.filename.toLowerCase().includes('ctf')
      // );
      
      this.loading = false;
    },
    viewPost(filename) {
      this.$router.push(`/post/${filename}`);
    }
  }
};
</script>