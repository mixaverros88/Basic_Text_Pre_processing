from functions import *

txt = open(get_sample_text_file_path()).read()

sanitized_str = sanitize_string(txt)
results = [['Sum of Paragraphs: ', count_paragraphs(txt)],
           ['Sum of Sentences: ', count_sentences(txt)],
           ['Count Words: ', count_words(txt)],
           ['Count Distinct Words: ', count_distinct_words(sanitized_str)],
           ['Remove Stop Words: ', remove_stop_words(sanitized_str)],
           ['Get Words: ', get_words(sanitized_str)],
           ['Get Words Frequency: ', word_frequency(['mike','mike'])]]

generate_results_file(results)

# print('Sum of Paragraphs: ', count_paragraphs(txt))
# print('Sum of Sentences: ', count_sentences(txt))
# print('Count Words: ', count_words(txt))
# print('Count Distinct Words: ', count_distinct_words(txt))
# print('Remove Stop Words: ', remove_stop_words(txt))
# print('Get Words: ', get_words(txt))

