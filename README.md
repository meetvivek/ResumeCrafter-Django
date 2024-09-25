# ResumeCrafter

## Overview

**ResumeCrafter** is a Django-based web application that allows users to create, download, and manage resumes dynamically. Users can log in, fill out a custom form to generate their resume, and download it as a PDF. Each user can create multiple resumes with dynamic sections for projects and work experiences.

The project is live at: [https://resumecrafter.up.railway.app/](https://resumecrafter.up.railway.app/)

## Features

- **User Authentication**: Custom login and registration forms, extending Django's `UserCreationForm`.
- **Dynamic Resume Form**: Users can add multiple projects and work experiences, with options to dynamically add more sections as needed.
- **Resume Management**: Users can view their created resumes, download them as PDFs, or delete them after confirmation.
- **PDF Generation**: Resumes are generated as PDFs using `pdfkit` and `wkhtmltopdf`, based on a dynamically rendered HTML template.
- **Multiple Resume Support**: Each user can create and manage multiple resumes.
- **Deployment**: The project is containerized with Docker and deployed on Railway.
- **Future Updates**: Multiple resume templates will be available in the future for added customization.
- **Responsive Design**: The project is fully responsive, ensuring optimal viewing across all screen sizes, and designed with a great user experience in mind.

## Unique Resume Template

The resume template provided in this project is **industry-preferred** and **ideal for college students**. It has been designed to offer a clean, professional layout, tested to handle various conditions such as missing project links or other optional fields. This template is rarely found on common resume platforms, making it highly valuable for users looking to stand out.

While the template is not shared in the GitHub repository, it has been crafted with meticulous attention to detail and will be expanded with more template options in future updates.

## Technologies Used

- **Backend**: Django 5.x
- **Frontend**: HTML5, CSS3, Bootstrap, JavaScript
- **Database**: Default Django SQLite
- **PDF Generation**: `pdfkit`, `wkhtmltopdf`
- **Containerization**: Docker
- **Deployment**: Railway

## LinkedIn Post & Project Video

I will be sharing a detailed post on LinkedIn about this project along with a video explaining its features and implementation. Stay tuned!

**LinkedIn Post**: [Link to LinkedIn Post](#) (Link to be updated soon)


## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

- Python 3.8+
- Django 5.x
- `pdfkit` and `wkhtmltopdf`

### Clone the repository:
```bash
git clone https://github.com/meetvivek/ResumeCrafter-Django.git
cd ResumeCrafter-Django
```

### Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
### Install the required packages:
```bash
pip install -r requirements.txt
```

### Apply migrations:
```bash
python manage.py migrate
```

### Create a superuser to access the Django admin panel (optional):
```bash
python manage.py createsuperuser
```

### Run the development server:
```bash
python manage.py runserver
```

## Docker Setup
While this repository does not include the Docker configuration, the project has been deployed using Docker on Railway for handling pdfkit and wkhtmltopdf dependencies. The code here is meant for easy setup on local systems.

If you wish to containerize the project yourself, you can create a Dockerfile and follow the standard Docker practices for Django projects.

## Customization

You can customize the appearance of the forms and resume templates by editing the HTML/CSS files located in the templates/ and static/ directories.

## Contributing
Contributions are welcome! Please feel free to submit a pull request.
