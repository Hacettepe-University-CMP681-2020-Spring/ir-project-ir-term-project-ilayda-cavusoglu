import numpy as np


def calculate_scores(labels, confusion_matrix):
    p_val = calculate_precision(labels, confusion_matrix)
    r_val = calculate_recall(labels, confusion_matrix)
    calculate_f_score(labels, p_val, r_val)
    calculate_accuracy(confusion_matrix)


def calculate_accuracy(confusion_matrix):
    confusion_matrix = np.array(confusion_matrix)
    print("Accuracy:")
    print(confusion_matrix.trace()/confusion_matrix.sum())


def calculate_f_score(labels, p_vals, r_vals):
    r_score = {}
    for label in labels:
        p_val = p_vals[label]
        r_val = r_vals[label]
        r_score[label] = 2 * (p_val * r_val) / (p_val + r_val)
    print("F-Score: ")
    print(r_score)


def calculate_precision(labels, confusion_matrix):
    precision = {}
    i = 0
    confusion_matrix = np.array(confusion_matrix)

    sum_of_columns = confusion_matrix.sum(axis=0)
    for label in labels:
        precision[label] = confusion_matrix[i, i] / sum_of_columns[i]
        i = i + 1
    print("Precision: ")
    print(precision)
    return precision


def calculate_recall(labels, confusion_matrix):
    recall = {}
    i = 0
    confusion_matrix = np.array(confusion_matrix)

    sum_of_rows = confusion_matrix.sum(axis=1)
    for label in labels:
        recall[label] = confusion_matrix[i, i] / sum_of_rows[i]
        i = i + 1
    print("Recall: ")
    print(recall)
    return recall
