import os


def load_programming_languages():
    with open(os.path.join("model_inputs", "programming_languages.txt"), "r") as f:
        programming_languages = f.read().splitlines()
    return programming_languages


def load_design_tools():
    with open(os.path.join("model_inputs", "design_tools.txt"), "r") as f:
        design_tools = f.read().splitlines()
    return design_tools


def load_stopwords():
    with open(os.path.join("model_inputs", "stopwords.txt"), "r") as g:
        stopwords = g.read().splitlines()
    return stopwords
