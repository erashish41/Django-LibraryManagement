# {% extends 'base.html' %}
# {% load crispy_forms_tags %}
# {% block title %}Book List{% endblock %}

# {% block content %}
# <div class="container py-4">
#     <div class="d-flex justify-content-between align-items-center mb-4">
#         <h2 class="text-primary">📚 Book List</h2>
#         <!-- Button trigger modal -->
#         <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#exampleModal">
#             ➕ Add New Book
#         </button>
#     </div>

#     <!-- Modal -->
#     <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
#         <div class="modal-dialog modal-lg">
#             <div class="modal-content shadow">
#                 <div class="modal-header bg-primary text-white">
#                     <h5 class="modal-title" id="exampleModalLabel">Add New Book</h5>
#                     <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
#                 </div>
#                 <div class="modal-body">
#                     <form method="post" action="">
#                         {% csrf_token %}
#                         {{ form|crispy }}
#                         <div class="d-flex justify-content-end mt-3 gap-2">
#                             <button type="submit" class="btn btn-primary">💾 Save</button>
#                             <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">❌ Cancel</button>
#                         </div>
#                     </form>
#                 </div>
#             </div>
#         </div>
#     </div>

#     <!-- Book Cards -->
#     <div class="row">
#         {% for book in books %}
#             <div class="col-md-4 col-lg-3 mb-4">
#                 <div class="card h-100 border-0 shadow-sm">
#                     <div class="card-body">
#                         <h5 class="card-title text-info fw-bold">{{ book.title }}</h5>
#                         <p class="mb-1"><strong>📘 Publisher:</strong> {{ book.publisher.name }}</p>
#                         <p class="mb-1"><strong>🏢 Branch:</strong> {{ book.library_branch.city.city_name }}</p>
#                         {% for author in book.author.all %}
#                             {% if forloop.first %}
#                                 <p class="mb-1"><strong>✍️ Author:</strong> {{ author.name }}</p>
#                             {% endif %}
#                         {% endfor %}
#                     </div>
#                     <div class="card-footer bg-white border-top-0 d-flex justify-content-between">
#                         <a href="{% url 'book_detail' book.pk %}" class="btn btn-sm btn-outline-primary">View</a>
#                         <form method="post" action="{% url 'book_delete' book.pk %}">
#                             {% csrf_token %}
#                             <button class="btn btn-sm btn-outline-danger" type="submit">Delete</button>
#                         </form>
#                     </div>
#                 </div>
#             </div>
#         {% empty %}
#             <div class="col-12">
#                 <div class="alert alert-warning text-center">
#                     No books available. Add a new one!
#                 </div>
#             </div>
#         {% endfor %}
#     </div>
# </div>
# {% endblock %}










# {% extends 'base.html' %}
# {% load crispy_forms_tags %}
# {% block title %}Book Details{% endblock %}

# {% block content %}
# <div class="container py-5">
#     <div class="row justify-content-center">
#         <div class="col-md-8">

#             <!-- Title -->
#             <div class="d-flex justify-content-between align-items-center mb-4">
#                 <h2 class="text-primary">📘 Book Details</h2>
#                 <a href="{% url 'book_list' %}" class="btn btn-outline-secondary">← Back to List</a>
#             </div>

#             <!-- Book Card -->
#             <div class="card shadow-lg border-0">
#                 <div class="card-body">
#                     <h4 class="card-title mb-3 text-info">{{ book.title }}</h4>
#                     <ul class="list-group list-group-flush">
#                         <li class="list-group-item">
#                             <strong>📚 ISBN:</strong> {{ book.isbn }}
#                         </li>
#                         <li class="list-group-item">
#                             <strong>🏷️ Category:</strong> {{ book.category.name }}
#                         </li>
#                         <li class="list-group-item">
#                             <strong>🏢 Publisher:</strong> {{ book.publisher.name }}
#                         </li>
#                         <li class="list-group-item">
#                             <strong>✍️ Author(s):</strong>
#                             {% for author in book.author.all %}
#                                 {{ author.name }}{% if not forloop.last %}, {% endif %}
#                             {% endfor %}
#                         </li>
#                     </ul>

#                     <!-- Buttons -->
#                     <div class="mt-4 d-flex justify-content-between">
#                         <!-- Update Button (Modal Trigger) -->
#                         <button class="btn btn-outline-primary" data-bs-toggle="modal" data-bs-target="#editBookModal">
#                             ✏️ Update Book
#                         </button>

#                         <!-- Delete Button -->
#                         <form method="post" action="{% url 'book_delete' book.pk %}">
#                             {% csrf_token %}
#                             <button class="btn btn-outline-danger" type="submit">🗑️ Delete</button>
#                         </form>
#                     </div>
#                 </div>
#             </div>
#         </div>
#     </div>
# </div>

# <!-- 🔄 Edit Book Modal -->
# <div class="modal fade" id="editBookModal" tabindex="-1" aria-labelledby="editBookModalLabel" aria-hidden="true">
#     <div class="modal-dialog modal-lg">
#         <div class="modal-content shadow">
#             <div class="modal-header bg-primary text-white">
#                 <h5 class="modal-title" id="editBookModalLabel">✏️ Update Book</h5>
#                 <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
#             </div>
#             <div class="modal-body">
#                 <form method="post" action="{% url 'book_detail' book.pk %}">
#                     {% csrf_token %}
#                     {{ form|crispy }}
#                     <div class="d-flex justify-content-end mt-3 gap-2">
#                         <button type="submit" class="btn btn-primary">💾 Save Changes</button>
#                         <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">❌ Cancel</button>
#                     </div>
#                 </form>
#             </div>
#         </div>
#     </div>
# </div>
# {% endblock %}
