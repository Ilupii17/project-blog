<template>
  <nav class="bg-slate-800 shadow-lg">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <div class="flex-shrink-0">
          <router-link to="/" class="text-3xl font-bold text-white hover:text-gray-200 transition-colors">
            llupii
          </router-link>
        </div>
        
        <!-- Desktop Menu -->
        <div class="hidden md:flex space-x-8">
          <router-link 
            v-for="item in navItems" 
            :key="item.name"
            :to="item.path" 
            class="text-gray-300 hover:text-white transition-colors duration-200 text-lg font-medium"
            active-class="text-white border-b-2 border-white"
          >
            {{ item.name }}
          </router-link>
        </div>
        
        <!-- Mobile Menu Button -->
        <button 
          @click="toggleMenu"
          class="md:hidden text-gray-300 hover:text-white focus:outline-none"
        >
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path 
              v-if="!isMenuOpen"
              stroke-linecap="round" 
              stroke-linejoin="round" 
              stroke-width="2" 
              d="M4 6h16M4 12h16M4 18h16" 
            />
            <path 
              v-else
              stroke-linecap="round" 
              stroke-linejoin="round" 
              stroke-width="2" 
              d="M6 18L18 6M6 6l12 12" 
            />
          </svg>
        </button>
      </div>
      
      <!-- Mobile Menu -->
      <div 
        v-if="isMenuOpen" 
        class="md:hidden pb-4 space-y-2"
      >
        <router-link 
          v-for="item in navItems" 
          :key="item.name"
          :to="item.path" 
          @click="closeMenu"
          class="block py-2 text-gray-300 hover:text-white transition-colors duration-200"
          active-class="text-white font-semibold"
        >
          {{ item.name }}
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      isMenuOpen: false,
      navItems: [
        { name: 'Home', path: '/' },
        { name: 'WriteUp', path: '/writeup' },
        { name: 'Project', path: '/project' }
      ]
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
    closeMenu() {
      this.isMenuOpen = false;
    }
  }
};
</script>