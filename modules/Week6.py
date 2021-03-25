import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor
import requests as req


class TextComparer:
    def __init__(self, url_list):
        self.url_list = url_list
        self.filenames = []

    def __iter__(self):
        self.index = 0
        return iter

    def __next__(self):
        if self.index < len(self.filenames):
            current_index = self.index
            self.index += 1
            return self.filenames[1]
        else:
            raise StopIteration

    @staticmethod
    def download(url):
        filename_title = ""
        try:
            r = req.get(url)
            r.raise_for_status()
            filename_title = r.text.partition("Title: ")[2].splitlines()[0] + ".txt"
            with open("modules/textfiles/" + filename_title, "w") as f:
                f.write(r.text)
        except req.exceptions.HTTPError as e:
            print(e.response.text)
        except FileNotFoundError:
            print("File not found. Check the path variable and filename")
        return "modules/textfiles/" + filename_title

    def multi_download(self, url_list):
        with ThreadPoolExecutor(len(url_list)) as ex:
            res = ex.map(self.download, url_list)
        self.filenames = list(res)

    def avg_vowels(self, filename):
        vowels = ["A", "E", "I", "O", "U", "Y"]

        with open(filename) as input_file:
            text = input_file.read()

        words = text.split()
        number_of_words = len(words)

        number_of_vowels = 0

        for word in words:
            for letter in word:
                if letter.upper() in vowels:
                    number_of_vowels += 1

        score = round(number_of_vowels / number_of_words, 5)
        return score, filename

    def hardest_read(self):
        workers = multiprocessing.cpu_count()

        with ProcessPoolExecutor(workers) as executor:
            results = executor.map(self.avg_vowels, self.filenames)

        highest_avg = None

        for result in results:
            if highest_avg is None or highest_avg[0] < result[0]:
                highest_avg = result

        return highest_avg[1]
