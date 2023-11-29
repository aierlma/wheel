import os
import re

class SubtitleProcessor:
    """
    A class to process SRT (SubRip Text) subtitle files. This class handles the reading,
    parsing, processing, and saving of subtitles in SRT format.
    """

    def __init__(self, file_path):
        """
        Initializes the SubtitleProcessor with the file path of the SRT file.

        Args:
            file_path (str): Path to the SRT file.
        """
        self.file_path = file_path
        self.subtitles = []
        self._read_file()

    def _read_file(self):
        """
        Reads the SRT file and loads its content into memory.
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
        self.subtitles = self._parse_srt(content)

    def remove_japanese_quotes(self):
        """
        Removes Japanese quotes from the start and end of each subtitle line.

        This function iterates through each subtitle, checking and removing
        Japanese quotes 「 and 」 from the start and end of each line of the subtitle text.
        """
        for subtitle in self.subtitles:
            subtitle['text'] = subtitle['text'].replace('「', '').replace('」', '')


    def _parse_srt(self, content):
        """
        Parses the content of an SRT file into a list of subtitle dictionaries.

        Args:
            content (list of str): The content of the SRT file.

        Returns:
            list of dict: Parsed subtitles with 'index', 'time', and 'text'.
        """
        subtitles = []
        subtitle_parts = {'index': '', 'time': '', 'text': ''}
        part = ''

        for line in content:
            if line.strip() == '':
                if part not in subtitle_parts:  # 确保 part 是有效的键
                    continue
                subtitle_parts[part] = subtitle_parts[part].strip()
                subtitles.append(subtitle_parts.copy())
                subtitle_parts = {'index': '', 'time': '', 'text': ''}
                part = ''
            elif part == '':
                subtitle_parts['index'] = line.strip()
                part = 'time'
            elif part == 'time' and '-->' in line:
                subtitle_parts['time'] = line.strip()
                part = 'text'
            elif part == 'text':
                subtitle_parts['text'] += line

        return subtitles

    def merge_subtitles(self):
        """
        Merges subtitles with identical text.
        """
        merged = []
        previous = None

        for subtitle in self.subtitles:
            if previous and subtitle['text'] == previous['text']:
                previous['time'] = re.sub(r'-->.*', '--> ' + subtitle['time'].split(' --> ')[1], previous['time'])
            else:
                if previous:
                    merged.append(previous)
                previous = subtitle.copy()

        if previous:
            merged.append(previous)

        self.subtitles = merged


    def remove_specific_lines(self, texts_to_remove, kana_pattern):
        """
        Removes subtitles that contain specific texts or match a specific kana pattern.

        Args:
            texts_to_remove (list of str): Subtitles to remove based on their text.
            kana_pattern (str): Regular expression pattern for Japanese kana.
        """
        self.subtitles = [
            subtitle for subtitle in self.subtitles 
            if not any(text in subtitle['text'] for text in texts_to_remove)
            and not re.fullmatch(kana_pattern, subtitle['text'].replace('\n', '').replace(' ', ''))
        ]


    def format_srt(self):
        """
        Formats the subtitles into SRT format.

        Returns:
            str: The formatted SRT content.
        """
        formatted = []
        for i, subtitle in enumerate(self.subtitles, start=1):
            formatted.append(f"{i}\n{subtitle['time']}\n{subtitle['text']}\n\n")

        return ''.join(formatted)

    def save_to_file(self, output_file_path):
        """
        Saves the processed subtitles to a specified file.

        Args:
            output_file_path (str): The path to save the processed subtitles.
        """
        formatted_srt = self.format_srt()
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(formatted_srt)

    def remove_non_japanese_lines(self):
        """
        Removes subtitles that contain any characters other than Japanese, Arabic numerals, 
        standard ASCII symbols, Japanese punctuation marks, and the long vowel mark 'ー', including all small kana.
        """
        japanese_and_symbols_pattern = r'[0-9ぁ-んァ-ン一-龥ヵヶっゃゅょゎァィゥェォッャュョヮーヴ\s!-\/:-@\[-\`{-~、。、「」『』（）〜・…々(OK)]*[A-Ga-g]?[0-9ぁ-んァ-ン一-龥ヵヶっゃゅょゎァィゥェォッャュョヮーヴ\s!-\/:-@\[-\`{-~、。、「」『』（）〜・…々(OK)]*'
        cup = r'カップ|VTR|MG'
        self.subtitles = [subtitle for subtitle in self.subtitles if re.fullmatch(japanese_and_symbols_pattern, subtitle['text']) or re.search(cup, subtitle['text'])]



    def remove_single_japanese_char_lines(self):
        """
        Removes subtitles that contain only a single Japanese character.
        """
        single_char_pattern = r'^[ぁ-んァ-ン一-龥ーA-Za-z]$'
        self.subtitles = [subtitle for subtitle in self.subtitles if not re.fullmatch(single_char_pattern, subtitle['text'].strip())]

    def remove_repeated_sequences(self):
        """
        Removes subtitles that contain abnormal repeated sequences, 
        """
        # 正则表达式匹配重复序列
        repeated_pattern = r'(?<![、。,.\s])(.)\1{3,}(?![、。,.\s])|(?<![、。,.\s])(..)\2{3,}(?![、。,.\s])|(?<![、。,.\s])(...)\3{2,}(?![、。,.\s])|(?<![、。,.\s])(....)\4{2,}(?![、。,.\s])'
        self.subtitles = [subtitle for subtitle in self.subtitles if (not re.search(repeated_pattern, subtitle['text'].replace('\n', ''))) or len(re.search(repeated_pattern, subtitle['text'].replace('\n', '')).group(0)) + 10 < len(subtitle['text'].replace('\n', '')) or "どんどん" in subtitle['text'].replace('\n', '') or 'なになに' in subtitle['text'].replace('\n', '')]



def main():
    """
    Main function to process an SRT file.
    """
    # 从当前目录输入所有srt文件，但文件名没有merged的作为input_files
    
    input_files = [file for file in os.listdir() if file.endswith('.srt') and 'merged' not in file]
    
    kana_pattern = r'[あえんーうっ、。,.!…]+|ご視聴ありがとうございました.*|[え(あ、)+!-\/:-@\[-\`{-~、。、「」『』（）〜・…々]+(はい)*'
    texts_to_remove = ["ご視聴ありがとうございました",'ご視聴ありがとうございました。', '音楽','あー','次回予告','おやすみなさい','を愛しています']

    for input_file in input_files:
        processor = SubtitleProcessor(input_file)
        processor.merge_subtitles()
        processor.remove_repeated_sequences()
        processor.remove_japanese_quotes()
        processor.remove_non_japanese_lines()
        processor.remove_specific_lines(texts_to_remove, kana_pattern)
        processor.remove_single_japanese_char_lines()
        processor.merge_subtitles()

        output_file = input_file.rsplit('.', 1)[0] + '-merged.srt'
        processor.save_to_file(output_file)
        print(f"Processed subtitles saved to {output_file}")

if __name__ == "__main__":
    main()
