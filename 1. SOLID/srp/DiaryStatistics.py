from Diary import Diary

class DiaryStatistics(Diary):
    """Class for calculating the statistics of diary."""

    @staticmethod
    def print_statistics(diary_object):
        """Võtab suvalise objekti, millel on .diary list ja arvutab."""
        if hasattr(diary_object, 'diary') and diary_object.diary:
            count = len(diary_object.diary)
            avg = sum(len(e) for e in diary_object.diary) / count
            print(f"Sissekannete arv: {count}")
            print(f"Keskmine tähemärkide arv: {round(avg)}")