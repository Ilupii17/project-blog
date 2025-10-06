<template>
  <article v-if="post.content" v-html="post.content" class="prose max-w-none"></article>
</template>

<script>
export default {
  props: ['post']
}
</script>
