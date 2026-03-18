from Diary import Diary

class DiaryPersistence(Diary):
    """Class for saving and loading diary."""
    @staticmethod
    def save(diary, filename):
        """Save the diary to file."""
        with open(filename, 'w') as f:
            f.write(str(diary))
            f.close()
    @staticmethod
    def load(filename):
        """Load the diary from file."""
        new_diary = Diary()
        with open(filename, 'r') as f:
            for line in f:
                clean_line = line.strip()
                if clean_line:
                    new_diary.add_entry(clean_line)
            return new_diary