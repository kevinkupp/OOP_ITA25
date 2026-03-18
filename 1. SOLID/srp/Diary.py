
class Diary:
    """Class named Diary."""

    def __init__(self):
        """Class named Diary."""
        self.diary = []
        self.counter = 0

    def add_entry(self, text):
        """Add entry to the diary."""
        self.diary.append(f"{self.counter}: {text}")
        self.counter += 1

    def remove_entry(self, text):
        """Remove entry from the diary."""
        self.diary.remove(text)

    def __str__(self):
        return "\n".join(self.diary)


