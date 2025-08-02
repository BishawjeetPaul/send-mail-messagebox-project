# send-mail-messagebox-project
📧 Django Email Sender App with Login A simple yet powerful web-based email sending application built using Django, with user authentication (login/logout) and a sleek frontend powered by jQuery, HTML, CSS, and JavaScript. It allows users to send emails via a web form using Django's email backend.

🚀 Features
    🔐 User Authentication
        Register, Login, Logout functionality
        Password hashing and session management

    📬 Send Email Form
        Send email with subject, message, and recipient
        Uses Django's send_mail() for backend handling
        jQuery validation before form submission
        Success and error feedback messages
        
    🌐 Frontend  
        Clean and responsive UI using HTML, CSS, and Bootstrap
        JavaScript & jQuery for dynamic form behavior

    💾 Database
        SQLite used for user and session storage (default Django setup)
        

   🛠️ Tech Stack

        Layer	                     Technology

        Backend	                     Django (Python)
        Frontend	                 HTML, CSS, JavaScript, jQuery
        Auth System	                 Django’s built-in auth views
        Email Backend	             Django SMTP Email Backend
        Database	                 SQLite
        
        
📂 Project Structure

      email_project/
      ├── email_app/
      │   ├── templates/
      │   │   ├── login.html
      │   │   ├── register.html
      │   │   ├── send_email.html
      │   │   └── base.html
      │   ├── static/
      │   │   └── js/
      │   │       └── form.js
      │   ├── views.py
      │   ├── urls.py
      ├── email_project/
      │   └── settings.py
      ├── db.sqlite3
      ├── manage.py
      └── requirements.txt
    
🧪 Live Features
  ✅ Login-protected email form
  ✅ Client-side and server-side validations
  ✅ Feedback alerts after sending
  ✅ Clean logout that destroys session
  

🔧 Setup Instructions
  ✅ Prerequisites
      Python 3.x
      pip

📦 Installation
    # Clone the repo
    git clone https://github.com/yourusername/django-email-login-app.git
    cd django-email-login-app
    
    # Create a virtual environment
    
    # Install required packages
    pip install -r requirements.txt
    
    # Apply migrations
    python manage.py migrate
    
    # Create superuser (optional)
    python manage.py createsuperuser
    
    # Start development server
    python manage.py runserver
    
    

        
