<template>
  <div class="min-h-screen flex flex-col">
    <!-- HEADER -->
    <header class="bg-blue-600 text-white p-4 flex justify-between items-center">
      <h1 class="text-xl font-bold">My Blog</h1>
      <nav class="space-x-4">
        <RouterLink to="/home" class="hover:underline">Home</RouterLink>
        <RouterLink to="/writeup" class="hover:underline">Write Up</RouterLink>
      </nav>
    </header>

    <!-- CONTENT -->
    <main class="flex-1">
      <RouterView />
    </main>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>
