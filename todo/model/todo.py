
from typing import List, Dict

class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id = code_id
        self.title = title
        self.description = description
        self.completed = False  # Inicializado en False
        self.tags: List[str] = []  # Inicializado como lista vacía

    def mark_completed(self) -> None:
        """Marca la tarea como completada."""
        self.completed = True

    def add_tag(self, tag: str) -> None:
        """Agrega una etiqueta (tag) si no está ya presente en la lista de tags."""
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        """Devuelve un string con el código del todo y el título."""
        return f"{self.code_id} - {self.title}"

    def __repr__(self) -> str:
        return f"Todo(code_id={self.code_id}, title='{self.title}', description='{self.description}', completed={self.completed}, tags={self.tags})"


class TodoBook:
    def __init__(self):
        self.todos: Dict[int, Todo] = {}  # Diccionario vacío de todos

    def add_todo(self, title: str, description: str) -> int:
        """Agrega un nuevo todo, genera un ID y lo retorna."""
        new_id = len(self.todos) + 1  # Genera un nuevo ID
        new_todo = Todo(new_id, title, description)  # Crea un nuevo objeto Todo
        self.todos[new_id] = new_todo  # Agrega el nuevo todo al diccionario
        return new_id

    def pending_todos(self) -> List[Todo]:
        """Retorna una lista de todos los todos que no han sido completados."""
        return [todo for todo in self.todos.values() if not todo.completed]

    def completed_todos(self) -> List[Todo]:
        """Retorna una lista de todos los todos que han sido completados."""
        return [todo for todo in self.todos.values() if todo.completed]

    def tags_todo_count(self) -> Dict[str, int]:
        """Retorna un diccionario con el conteo de todos para cada tag."""
        tag_count: Dict[str, int] = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag in tag_count:
                    tag_count[tag] += 1
                else:
                    tag_count[tag] = 1
        return tag_count
