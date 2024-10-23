import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(punctuation, '')
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word) + 1
            else:
                result[name] = None
        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            result[name] = words.count(word)
        return result


finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))