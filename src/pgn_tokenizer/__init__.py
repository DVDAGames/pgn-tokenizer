from transformers import PreTrainedTokenizerFast

from pgn_tokenizer.constants import DATASET_NAME

tokenizer = PreTrainedTokenizerFast(tokenizer_file=f"{DATASET_NAME}.json")
