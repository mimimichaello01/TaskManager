

class Task:
    def __init__(self, id: int, title: str, is_completed: bool):
        self.id = id
        self.title = title
        self.is_completed = is_completed

    def mark_as_completed(self):
        if not self.is_completed:
            self.is_completed = True

    def rename(self, new_title: str):
        if len(new_title) > 100:
            raise ValueError("Title too long")
