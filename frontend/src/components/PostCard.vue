<template>
  <div class="bg-slate-800 rounded-lg shadow-lg p-6 hover:shadow-xl transition-shadow duration-300 cursor-pointer"
       @click="$emit('click')">
    <h3 class="text-xl font-semibold text-white mb-2">{{ title }}</h3>
    <p class="text-gray-400 text-sm">{{ formatDate(title) }}</p>
  </div>
</template>

<script>
export default {
  name: 'PostCard',
  props: {
    title: {
      type: String,
      required: true
    }
  },
  methods: {
    formatDate(filename) {
      // Remove .md extension
      const name = filename.replace('.md', '');
      // Format untuk display
      return name.replace(/-/g, ' ');
    }
  }
};
</script>