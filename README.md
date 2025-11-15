# 🎬 Movie Catalog API (Django REST Framework)

<p align="center">
  <strong>Este é o motor de backend para o <a href="https://github.com/tenoriopedro/StreamlitApp" target="_blank">Flix App (Cliente Streamlit)</a>.</strong>
</p>

---

## 🚀 Visão Geral

Este projeto é uma API RESTful robusta, construída com **Django REST Framework (DRF)**, para gerir um catálogo de filmes. Ela fornece lógica de negócio, persistência de dados e autenticação segura para qualquer cliente frontend.

## 🏛️ Arquitetura (Cliente-Servidor)

Esta API foi desenhada como o "Servidor" (Backend) num ecossistema Cliente-Servidor.



* **Cliente (Frontend):** [Flix App (Streamlit)](https://github.com/tenoriopedro/StreamlitApp)
    * Consome esta API para todas as operações de dados.
    * [Ver a demo ao vivo do cliente](https://appapp-nn6fq8ue8qikftrqoi9kfm.streamlit.app/)

* **Servidor (Este Projeto):** `Movie Catalog API (DRF)`
    * Expõe endpoints RESTful.
    * Gere a autenticação e permissões via **JWT (SimpleJWT)**.
    * Valida dados e interage com a base de dados (PostgreSQL/SQLite).

---

### 🛠️ Funcionalidades Principais (Backend)

* **Autenticação Segura:** Endpoints de `Obter`, `Refresh` e `Verificar` Tokens **JWT** (via `djangorestframework-simplejwt`).
* **Controlo de Permissão:** Permissões personalizadas (`GlobalDefaultPermission`) ao nível do modelo que verificam `add`, `view`, `change`, `delete`.
* **Endpoints de Estatísticas:** Um endpoint dedicado (`/stats`) que calcula e retorna o total de filmes, críticas e a média de classificações.
* **Validação de Dados:** Regras de negócio aplicadas ao nível do *serializer* e do modelo (ex: `resume` ≤ 200 caracteres, `stars` entre 0-5).
* **Gestão de Atores (CSV):** Inclui um *comando de gestão* (management command) personalizado para importar atores em massa a partir de um ficheiro CSV.

---

### 💻 Stack Tecnológico

* **Framework:** Django
* **API:** Django REST Framework (DRF)
* **Autenticação:** djangorestframework-simplejwt (JWT)
* **Base de Dados:** PostgreSQL (Produção) / SQLite (Desenvolvimento)

---

### Endpoints Principais

<details>
  <summary>Clique para ver um resumo dos endpoints da API</summary>
  
  <ul>
    <li><code>/api/v1/token/</code> (Obter Token JWT)</li>
    <li><code>/api/v1/token/refresh/</code> (Refresh Token)</li>
    <li><code>/api/v1/movies/</code> (GET, POST)</li>
    <li><code>/api/v1/movies/&lt;id&gt;/</code> (GET, PUT, DELETE)</li>
    <li><code>/api/v1/genres/</code> (GET, POST)</li>
    <li><code>/api/v1/actors/</code> (GET, POST)</li>
    <li><code>/api/v1/reviews/</code> (GET, POST)</li>
    <li><code>/api/v1/stats/</code> (GET)</li>
  </ul>
</details>
