from transformers import pipeline
import torch
import pytorch_pretrained_bert as ppb
assert 'bert-large-cased' in ppb.modeling.PRETRAINED_MODEL_ARCHIVE_MAP
import os

#philschmid/bart-large-cnn-samsum
#philschmid/bart-large-cnn-samsum
#print(torch.__version__)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
def summarize_text(text: str, max_len: int) -> str:
    try:
        summary = summarizer(text, max_length=max_len, min_length=10, do_sample=False)
        return summary[0]["summary_text"]
    except IndexError as ex:
        
        return summarize_text(text=text[:(len(text) // 2)], max_len=max_len//2) + summarize_text(text=text[(len(text) // 2):], max_len=max_len//2)

