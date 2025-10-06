<template>
  <div 
    class="bg-slate-800 rounded-lg shadow-lg p-6 cursor-pointer transform transition-all duration-300 hover:shadow-2xl hover:scale-105 hover:-translate-y-1"
    @click="$emit('click')"
  >
    <h3 class="text-xl font-semibold text-white mb-2">
      {{ post.title || formatTitle(post.filename) }}
    </h3>
    <p class="text-gray-400 text-sm mb-3">
      {{ post.description || 'No description available' }}
    </p>
    <div class="flex items-center justify-between text-xs text-gray-500">
      <span>{{ post.date || formatDate(post.filename) }}</span>
      <span class="text-blue-400">Read more →</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostCard',
  props: {
    post: {
      type: Object,
      required: true
    }
  },
  methods: {
    formatTitle(filename) {
      if (!filename) return 'Untitled';
      return filename.replace('.md', '').replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    },
    formatDate(filename) {
      return new Date().toLocaleDateString('en-US', { 
        year: 'numeric', 
        month: 'short', 
        day: 'numeric' 
      });
    }
  }
};
</script>