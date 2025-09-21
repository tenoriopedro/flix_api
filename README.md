# 🎬 Movie Catalog API

A Django REST Framework project that provides a structured API for managing movies, genres, actors, and reviews.  
It includes **JWT-based authentication**, **model-level permission control**, and **data validation rules**.  

---

## 🚀 Features

- **Movies**
  - CRUD operations with validation (`resume` ≤ 200 chars, release date ≥ 1900).  
  - Links to genres and actors.  
  - Returns average review rating per movie.  
  - Statistics endpoint with total movies, reviews, and average stars.  

- **Genres**
  - Simple management of movie genres.  

- **Actors**
  - CRUD operations with nationality and birthday fields.  
  - Import actors via CSV with a custom management command.  

- **Reviews**
  - CRUD operations with validation (stars between 0–5).  
  - Linked to movies, contributes to rating calculation.  

- **Authentication**
  - JWT authentication using [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/).  
  - Endpoints for token obtain, refresh, and verify.  

- **Permissions**
  - Custom `GlobalDefaultPermission` enforces model-based permissions (`add`, `view`, `change`, `delete`).  

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework  
- **Auth**: djangorestframework-simplejwt (JWT tokens)  
- **Database**: SQLite (default, can be swapped for PostgreSQL/MySQL) 