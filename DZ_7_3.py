class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = []
        for name in file_name:
            self.file_names.append(name)

    def set_file_text(self, file_name, file_text):

        self.file_text = file_text
        for name in self.file_names:
            if name == file_name:
                with open(name, 'w', encoding='utf-8') as file:
                    for line in self.file_text:
                        file.write(line + '\n')

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                all_words[name] = file.read().split()
        return all_words

    def find(self, word):
        dict_words = self.get_all_words()
        dict_word_in_file = {}
        for name, list_words in dict_words.items():
            for i in range(len(list_words)):
                if  list_words[i] == word:
                    dict_word_in_file[name] = i+1
                    break
        return dict_word_in_file


    def count(self, word):
        dict_words = self.get_all_words()
        dict_count_word_in_file = {}
        for name, list_words in dict_words.items():
            count = 0
            for i in range(len(list_words)):
                if  list_words[i] == word:
                    count += 1
            dict_count_word_in_file[name] = count
        return dict_count_word_in_file


    def __str__(self):
        return f'file_names: {self.file_names}'



if __name__ == '__main__':
    text_1 = [
        'It\'s a text for task   Найти везде,',
        'Используйте его для самопроверки.',
        'Успехов в решении задачи!',
        'text text text'
    ]

    text_2 = [
        'It\'s a text for task   Найти везде,',
        'Используйте его для самопроверки.',
        'Успехов в решении задачи!',
        'text text text text'
    ]


    finder2 = WordsFinder('test_file_1.txt', 'test_file_2.txt')
    finder2.set_file_text('test_file_1.txt', text_1)
    finder2.set_file_text('test_file_2.txt', text_2)
    print(finder2.get_all_words())
    print(finder2.find('text'))
    print(finder2.count('text'))





