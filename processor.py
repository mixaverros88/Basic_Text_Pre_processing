"""
Mike-George Verros
ITC6010A1 - NATURAL LANGUAGE PROCESSING - SPRING TERM 2021
HW#1
"""

from functions.functions import *

txt = open(get_sample_text_file_path()).read()

sanitized_str = sanitize_string(txt)
removed_stop_word_txt = remove_stop_words(sanitized_str)
tokenized_txt = tokenization(txt)

results = [['a.	Number of paragraphs.: ', sum_of_paragraphs(txt)],
           ['b.	Number of sentences.: ', sum_of_sentences(txt)],
           ['c.	Number of words : ', sum_of_words(txt)],
           ['d.	Number of distinct words : ', sum_of_distinct_word_types(tokenized_txt)],
           ['e.	List of word frequency counts.  : ', word_frequency(tokenized_txt)],
           ['f.	Remove the stopwords  : ', removed_stop_word_txt],
           ['Sum of Distinct Words: ', sum_of_distinct_words(txt)],
           ['Sum of Words After Removing Stop Words : ', len(removed_stop_word_txt)],
           ['Get Words: ', get_words(sanitized_str)],
           ]

generate_world_cloud(word_frequency(tokenized_txt))
generate_results_file(results)

