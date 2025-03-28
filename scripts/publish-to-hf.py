from pathlib import Path

from transformers import AutoTokenizer, PreTrainedTokenizerFast  # noqa: E402

from packages.python.pgn_tokenizer import __version__
from packages.python.pgn_tokenizer.constants import DATASET_NAME  # noqa: E402

base_path = Path(__file__).parent.parent

tokenizer_config_path = (base_path / f"config/{DATASET_NAME}.json").resolve()
tokenizer_vocab_path = (base_path / f"config/{DATASET_NAME}-vocab.json").resolve()
tokenzier_merges_path = (base_path / f"config/{DATASET_NAME}-merges.txt").resolve()

tokenizer = PreTrainedTokenizerFast(tokenizer_file=str(tokenizer_config_path))

tokenizer.save_pretrained("./.data/tokenizer")

# copy config files to ./packages/python/pgn_tokenizer/config
(base_path / "packages/python/pgn_tokenizer/config").mkdir(parents=True, exist_ok=True)
(base_path / "packages/python/pgn_tokenizer/config").symlink_to(tokenizer_config_path)
(base_path / "packages/python/pgn_tokenizer/config").symlink_to(tokenizer_vocab_path)
(base_path / "packages/python/pgn_tokenizer/config").symlink_to(tokenzier_merges_path)

# copy config files to ./packages/typescript/config
(base_path / "packages/typescript/config").mkdir(parents=True, exist_ok=True)
(base_path / "packages/typescript/config").symlink_to(tokenizer_config_path)
(base_path / "packages/typescript/config").symlink_to(tokenizer_vocab_path)
(base_path / "packages/typescript/config").symlink_to(tokenzier_merges_path)

tokenizer = AutoTokenizer.from_pretrained("./.data/tokenizer")

tokenizer.push_to_hub(
    "InterwebAlchemy/PGNTokenizer",
    revision=__version__,
)
