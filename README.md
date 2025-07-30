
# Django Movie App 🎬

This is a simple Django web application that displays a list of movies with their posters, titles, release years, and descriptions. It also allows viewing detailed information about each movie on a separate page.

## 📌 Project Structure

- movieGallery/ – Main Django project folder  
- movies/ – App that manages movie data and views  
- static/images/ – Contains all movie poster images (1080×1920px)  
- templates/movies/ – Contains HTML templates:  
  - home.html – Homepage  
  - movie_list.html – Displays all movies in a responsive card layout  
  - movie_details.html – Displays details for a selected movie  

## 💡 Features

- 📱 Mobile-friendly layout  
- 🎨 Elegant UI using custom CSS and Google Fonts (Poppins)  
- 🖼️ Poster images shown in full resolution (1080×1920px) without distortion  
- 🧾 Organized template structure using Django  
- 🔁 Fully responsive Flexbox-based layout  
- 🗂️ Separated static and template folders for modularity  

## ⚙️ How to Run Locally

Clone this repository:
```

git clone [https://github.com/SyedaJuveriya/django-movie-app.git](https://github.com/SyedaJuveriya/django-movie-app.git)
cd django-movie-app

```

(Optional) Create and activate a virtual environment:
```

python -m venv venv
venv\Scripts\activate

```

Install the required packages:
```

pip install -r requirements.txt

```

Run the development server:
```

python manage.py runserver

```

Now open your browser and go to:
```

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

```
```






