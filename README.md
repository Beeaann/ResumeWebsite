# Luke Slautterback - Resume Website

A modern, responsive Flask website showcasing Luke Slautterback's professional resume with an elegant design and interactive features.

## 🚀 Features

- **Modern Design**: Clean, professional layout with gradient backgrounds and smooth animations
- **Responsive**: Fully responsive design that works on all devices
- **Interactive Elements**: 
  - Smooth scrolling navigation
  - Animated timeline for experience
  - Interactive skill showcase
  - Contact form with validation
  - Mobile-friendly hamburger menu
- **Performance Optimized**: Fast loading with optimized assets
- **Accessibility**: Semantic HTML and keyboard navigation support

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with CSS Grid and Flexbox
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter)
- **Animations**: CSS animations and JavaScript interactions

## 📁 Project Structure

```
ResumeWebsite/
├── app.py                 # Main Flask application
├── Dockerfile            # Docker container configuration
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── Luke Slautterback Resume.pdf  # Resume PDF file
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── css/
    │   └── style.css     # Main stylesheet
    ├── js/
    │   └── script.js     # JavaScript functionality
    └── images/
        └── profile.jpg   # Profile image
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   # If using git
   git clone <repository-url>
   cd ResumeWebsite
   
   # Or simply navigate to the project directory
   cd ResumeWebsite
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000` to view the website.

## 🎨 Customization

### Updating Resume Content

1. **Personal Information**: Edit the HTML template in `templates/index.html`
   - Update name, title, and contact information
   - Modify the hero section description
   - Update about section content

2. **Experience Section**: 
   - Add or modify timeline items in the experience section
   - Update job titles, companies, dates, and descriptions

3. **Skills Section**:
   - Modify skill categories and items
   - Add or remove technologies
   - Update icons (using Font Awesome classes)

4. **Contact Information**:
   - Update email, LinkedIn, and GitHub links
   - Modify contact form if needed

### Styling Customization

1. **Colors**: Edit CSS custom properties in `static/css/style.css`
   ```css
   :root {
       --primary-color: #6366f1;    /* Main brand color */
       --secondary-color: #f59e0b;  /* Accent color */
       --accent-color: #10b981;     /* Success/highlight color */
   }
   ```

2. **Fonts**: Change the Google Fonts import in `templates/index.html`
   ```html
   <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
   ```

3. **Layout**: Modify grid layouts and spacing in the CSS file

### Adding Your Photo

1. Add your photo to `static/images/` directory
2. Update the profile image section in `templates/index.html`:
   ```html
   <div class="profile-image">
       <img src="{{ url_for('static', filename='images/your-photo.jpg') }}" alt="Your Name">
   </div>
   ```

## 🌐 Deployment

### Local Development
The application runs on `http://localhost:5000` by default.

### Production Deployment (Docker)

This project is containerized and deployed using Docker.

#### Docker Deployment
1. **Build the image**: `docker build -t luke-resume-website .`
2. **Run the container**: `docker run -d -p 8080:5000 --name luke-resume-website luke-resume-website`
3. **Access the website**: `http://localhost:8080`

#### Live Website
- **URL**: `https://lukeslautterback.com`
- **Hosted on**: Synology NAS with Cloudflare SSL
- **Container**: Running on port 8080

## 📱 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🎯 Features Breakdown

### Navigation
- Fixed navigation bar with smooth scrolling
- Mobile-responsive hamburger menu
- Active section highlighting

### Hero Section
- Gradient background with animated elements
- Typing animation for name
- Call-to-action buttons
- Profile card with floating animation

### About Section
- Statistics counter animation
- Responsive grid layout
- Hover effects on stat cards

### Experience Timeline
- Vertical timeline with alternating layout
- Smooth scroll animations
- Interactive hover effects

### Skills Showcase
- Categorized skill display
- Icon integration with Font Awesome
- Hover animations and color transitions

### Contact Form
- Form validation
- Success/error notifications
- Responsive design

## 🔧 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Change port in app.py
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```

2. **CSS/JS not loading**
   - Check file paths in templates
   - Ensure static files are in correct directories
   - Clear browser cache

3. **PDF not downloading**
   - Verify PDF file exists in root directory
   - Check file permissions

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to fork this project and customize it for your own use. If you make improvements, consider submitting a pull request!

## 📞 Support

For questions or support, please contact:
- Email: lukeslautterback@gmail.com
- LinkedIn: [Luke Slautterback](http://www.linkedin.com/in/luke-slautterback-713728233)
- GitHub: [Beeaann](http://www.github.com/Beeaann)

---

**Made with ❤️ by Luke Slautterback**
