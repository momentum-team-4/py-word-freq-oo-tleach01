STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        with open(file, 'r') as infile:
            self.poem = infile.read()
        return self.poem


class WordList:
    def __init__(self, text):
        self.text = text

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        file_words = self.text.lower().replace('-', " ").replace(":", '').replace(",", " ").replace(".", " ").replace("/n", " ").replace('"', " ").split()
        self.file_words = file_words
        return file_words
        # raise NotImplementedError("WordList.extract_words")

    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        removes_stops = []
        for word in self.file_words:
            if not word in STOP_WORDS:
                removes_stops.append(word)
            self.removes_stops = removes_stops
        

    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        self.freq_dict = {}
        for word in self.removes_stops:
            if word not in self.freq_dict.keys():
                self.freq_dict[word] = 1
            else:
                self.freq_dict[word] += 1
        raise NotImplementedError("WordList.get_freqs")


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """
        freq_chart = {}
        self.freqs = sorted(freq_chart, key = freq_chart.get, reverse=True)
        for num in self.freqs:
            print(num, freq_chart[num, '*' * freq_chart[num]])

        raise NotImplementedError("FreqPrinter.print_freqs")


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
