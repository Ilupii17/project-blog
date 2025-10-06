# 🔐 Ilupii Blog - Cybersecurity Blog Platform

A modern, minimal, and elegant blog platform built with **Vue.js** and **Flask** for sharing cybersecurity content, CTF writeups, and projects.

## ✨ Features

- 🎨 **Modern UI** - Clean and responsive design with dark theme
- 📝 **Markdown Support** - Write posts in Markdown with syntax highlighting
- 🚀 **Fast & Lightweight** - Built with Vue.js 3 Composition API
- 🔍 **Smart Filtering** - Automatic categorization for WriteUps and Projects
- 📱 **Fully Responsive** - Mobile-first design approach
- 🎯 **SEO Friendly** - Optimized routing and meta tags
- ⚡ **Hot Reload** - Fast development experience

## 🛠️ Tech Stack

### Frontend
- **Vue.js 3** - Progressive JavaScript framework
- **Vue Router** - Official routing library
- **Tailwind CSS** - Utility-first CSS framework
- **Vite** - Next generation frontend tooling
- **Montserrat Font** - Modern typography

### Backend
- **Flask** - Lightweight Python web framework
- **Flask-CORS** - Cross-Origin Resource Sharing
- **Python Markdown** - Markdown to HTML conversion
- **Pygments** - Syntax highlighting for code blocks

## 📁 Project Structure

```
ilupii-blog/
├── frontend/                # Vue.js frontend
│   ├── src/
│   │   ├── assets/
│   │   │   └── main.css    # Tailwind + custom styles
│   │   ├── components/
│   │   │   ├── Header.vue  # Navigation bar
│   │   │   └── PostCard.vue # Post preview card
│   │   ├── services/
│   │   │   └── api.js      # API service layer
│   │   ├── views/
│   │   │   ├── Home.vue    # Homepage
│   │   │   ├── WriteUp.vue # WriteUps listing
│   │   │   ├── Project.vue # Projects page
│   │   │   └── PostDetail.vue # Single post view
│   │   ├── router/
│   │   │   └── index.js    # Route configuration
│   │   ├── App.vue         # Root component
│   │   └── main.js         # Entry point
│   ├── tailwind.config.js  # Tailwind configuration
│   └── package.json
│
└── backend/                 # Flask backend
    ├── posts/              # Markdown posts directory
    │   ├── hello.md
    │   └── ctf-writeup.md
    ├── app.py              # Flask application
    └── requirements.txt    # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **npm** or **yarn**

### Installation

#### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ilupii-blog.git
cd ilupii-blog
```

#### 2. Setup Backend

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install flask flask-cors markdown

# Run Flask server
python app.py
```

Backend will run on `http://localhost:5000`

#### 3. Setup Frontend

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend will run on `http://localhost:5173`

## 📝 Writing Posts

### Create a new post

1. Create a new `.md` file in `backend/posts/` directory
2. Write your content in Markdown format

**Example: `my-first-writeup.md`**

```markdown
# My First CTF WriteUp

## Challenge Description
This is a web exploitation challenge...

## Solution
First, I analyzed the source code...

```python
import requests

url = "https://example.com"
response = requests.get(url)
print(response.text)
```

## Flag
`flag{example_flag_here}`
```

3. The post will automatically appear on your blog!

### Naming Conventions

- **WriteUps**: Include `writeup` or `ctf` in filename
  - `picoctf-2024-writeup.md`
  - `htb-ctf-web-challenge.md`
  
- **General Posts**: Any other markdown file
  - `introduction-to-pwn.md`
  - `binary-exploitation-basics.md`

## 🎨 Customization

### Change Theme Colors

Edit `frontend/src/assets/main.css`:

```css
/* Change primary colors */
.bg-slate-800 { background-color: #your-color; }
.text-white { color: #your-color; }
```

### Modify Navigation

Edit `frontend/src/components/Header.vue`:

```javascript
navItems: [
  { name: 'Home', path: '/' },
  { name: 'WriteUp', path: '/writeup' },
  { name: 'Project', path: '/project' },
  { name: 'About', path: '/about' }, // Add new item
]
```

### Change Font

Edit `frontend/src/assets/main.css`:

```css
@import url('https://fonts.googleapis.com/css2?family=YourFont:wght@300;400;500;600;700&display=swap');

body {
  font-family: 'YourFont', sans-serif;
}
```

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/posts` | Get all posts list |
| GET | `/posts/<name>` | Get specific post content |

### Response Format

**GET `/posts`**
```json
[
  "hello.md",
  "ctf-writeup-2024.md",
  "pwn-tutorial.md"
]
```

**GET `/posts/hello.md`**
```json
{
  "title": "hello.md",
  "content": "<h1>Hello World</h1><p>This is rendered HTML...</p>"
}
```

## 📦 Build for Production

### Frontend

```bash
cd frontend
npm run build
```

Build files will be in `frontend/dist/`

### Backend

For production deployment, use a WSGI server like **Gunicorn**:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🚢 Deployment

### Option 1: Vercel (Frontend) + PythonAnywhere (Backend)

1. Deploy frontend to Vercel
2. Deploy backend to PythonAnywhere
3. Update API base URL in `frontend/src/services/api.js`

### Option 2: Docker

Create `docker-compose.yml`:

```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
  
  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend
```

Run: `docker-compose up`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Ilupii**

## 🙏 Acknowledgments

- Vue.js team for the amazing framework
- Flask team for the lightweight backend
- Tailwind CSS for the utility-first approach
- The cybersecurity community for inspiration

## 📧 Contact

Have questions? Feel free to reach out!

- Create an issue on GitHub
- Email: your.email@example.com

---

<p align="center">Made with ❤️ by Ilupii</p>
<p align="center">Happy Hacking! 🔐</p>

buat
