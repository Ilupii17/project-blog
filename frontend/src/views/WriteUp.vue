<template>
  <div class="min-h-screen bg-slate-700 py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-4xl font-bold text-white mb-8">WriteUps</h1>
      
      <!-- Loading State -->
      <div v-if="loading" class="text-center text-gray-300">
        <p>Loading writeups...</p>
      </div>

      <!-- WriteUps Grid -->
      <div v-else-if="writeups.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <PostCard 
          v-for="writeup in writeups" 
          :key="writeup"
          :title="writeup"
          @click="viewPost(writeup)"
        />
      </div>

      <!-- Empty State -->
      <div v-else class="text-center text-gray-300">
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
      const allPosts = await api.getPosts();
      
      // HAPUS FILTER - tampilkan semua posts
      this.writeups = allPosts;
      
      // Atau kalau mau tetap filter, uncomment baris ini:
      // this.writeups = allPosts.filter(post => 
      //   post.toLowerCase().includes('writeup') || 
      //   post.toLowerCase().includes('ctf')
      // );
      
      this.loading = false;
    },
    viewPost(postName) {
      this.$router.push(`/post/${postName}`);
    }
  }
};
</script>