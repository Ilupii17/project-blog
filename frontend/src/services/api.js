const API_BASE_URL = 'http://localhost:5000';

export const api = {
  async getPosts() {
    try {
      console.log('Fetching from:', `${API_BASE_URL}/posts`); // tambah log ini
      const response = await fetch(`${API_BASE_URL}/posts`);
      if (!response.ok) throw new Error('Failed to fetch posts');
      const data = await response.json();
      console.log('Posts received:', data); // tambah log ini
      return data;
    } catch (error) {
      console.error('Error fetching posts:', error);
      return [];
    }
  },

  async getPost(name) {
    try {
      console.log('Fetching post:', `${API_BASE_URL}/posts/${name}`); // tambah log ini
      const response = await fetch(`${API_BASE_URL}/posts/${name}`);
      if (!response.ok) throw new Error('Post not found');
      return await response.json();
    } catch (error) {
      console.error('Error fetching post:', error);
      return null;
    }
  }
};