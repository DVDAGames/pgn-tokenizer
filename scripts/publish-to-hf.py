from pathlib import Path

from transformers import AutoTokenizer, PreTrainedTokenizerFast  # noqa: E402

from pgn_tokenizer import __version__
from pgn_tokenizer.constants import DATASET_NAME  # noqa: E402

base_path = Path(__file__).parent.parent

tokenizer_config_path = (
    base_path / f"src/pgn_tokenizer/config/{DATASET_NAME}.json"
).resolve()
tokenizer_vocab_path = (
    base_path / f"src/pgn_tokenizer/config/{DATASET_NAME}-vocab.json"
).resolve()
tokenzier_merges_path = (
    base_path / f"src/pgn_tokenizer/config/{DATASET_NAME}-merges.txt"
).resolve()

tokenizer = PreTrainedTokenizerFast(tokenizer_file=str(tokenizer_config_path))

tokenizer.save_pretrained("./.data/tokenizer")

tokenizer = AutoTokenizer.from_pretrained("./.data/tokenizer")

tokenizer.push_to_hub(
    "InterwebAlchemy/PGNTokenizer",
    revision=__version__,
)
