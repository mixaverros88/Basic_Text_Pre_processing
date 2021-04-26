"""
Mike-George Verros
ITC6010A1 - NATURAL LANGUAGE PROCESSING - SPRING TERM 2021
HW#1
"""

from functions.functions import *

file_content = get_the_content_of_a_file(get_sample_text_file_path())
lang_of_file = identify_lang_of_a_given_file(file_content)
tokenized_list = tokenization(file_content)
list_of_word_frequency_counts = token_frequency(tokenized_list)

results = [['Number of paragraphs', sum_of_paragraphs(file_content)],
           ['Number of sentences', sum_of_sentences(file_content)],
           ['Number of words', tokenized_list],
           ['Number of distinct words', sum_of_distinct_word_types(tokenized_list)],
           ['List of word frequency counts', list_of_word_frequency_counts],
           ['Remove the stopwords', remove_stop_words(tokenized_list)],
           ]

generate_world_cloud_image(list_of_word_frequency_counts)
generate_results_file(results)
