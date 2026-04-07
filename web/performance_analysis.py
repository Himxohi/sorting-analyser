import pandas as pd
from sorting_algorithms import *
from data_generator import generate_data

def run_analysis(size):

    data = generate_data(size)

    results = {}

    results['Bubble Sort'] = bubble_sort(data.copy())
    results['Selection Sort'] = selection_sort(data.copy())
    results['Insertion Sort'] = insertion_sort(data.copy())
    results['Merge Sort'] = merge_sort(data.copy())
    results['Quick Sort'] = quick_sort(data.copy())

    df = pd.DataFrame(list(results.items()), columns=['Algorithm','Time'])

    return df