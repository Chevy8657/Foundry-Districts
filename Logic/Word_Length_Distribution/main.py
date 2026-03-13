from fastapi import APIRouter
from collections import Counter

router = APIRouter()

@router.get("/logic/word-length-distribution")
def word_length_distribution(input_text: str):

    words = input_text.split()

    lengths = [len(word) for word in words]

    distribution = dict(Counter(lengths))

    return {
        "input_text": input_text,
        "distribution": distribution
    }
