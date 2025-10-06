<template>
  <ul class="space-y-2">
    <li v-for="post in posts" :key="post">
      <button 
        @click="$emit('select', post)" 
        class="text-blue-600 hover:underline"
      >
        {{ post }}
      </button>
    </li>
  </ul>
</template>

<script>
export default {
  props: ['posts']
}
</script>
