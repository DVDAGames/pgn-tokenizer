import argparse

from datasets import load_dataset
from pgn_tokenizer.constants import (
    DATASET_NAME,
    SEED,
    SPECIAL_TOKENS,
    TOKENIZER_CHUNK_PATTERN,
    VOCAB_SIZE,
)
from tokenizers import Regex, Tokenizer
from tokenizers.decoders import ByteLevel as ByteLevelDecoder
from tokenizers.models import BPE
from tokenizers.normalizers import NFD
from tokenizers.pre_tokenizers import Split
from tokenizers.processors import ByteLevel as ByteLevelProcessor
from tokenizers.trainers import BpeTrainer

TRAINING_DATASET = "InterwebAlchemy/pgn-dataset-including-special-tokens"

OUTPUT_PATH = "./src/pgn_tokenizer/config"

# get args from command line
parser = argparse.ArgumentParser()

parser.add_argument(
    "--sample",
    action="store_true",
    help="Use a smaller sample dataset for training",
)

parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Run the script without actually saving the trained tokenizer",
)

parser.add_argument(
    "--vocab_size",
    help="Size of the vocabulary",
    default=VOCAB_SIZE,
)

args = parser.parse_args()

dataset = load_dataset(TRAINING_DATASET)

if args.sample:
    dataset = dataset["train"].train_test_split(test_size=0.1, seed=SEED)

if args.dry_run:
    print("This is a DRY RUN. No files will be saved.")

print(
    f"Training {TRAINING_DATASET} with {'sample' if args.sample else 'full'} dataset...",
)

training_data = []

for x in dataset["train"].select_columns("PGN").to_list():
    training_data.append(x["PGN"])

tokenizer = Tokenizer(
    BPE(
        unk_token=SPECIAL_TOKENS["UNKNOWN"],
        fuse_unk=True,
    ),
)

tokenizer.normalizer = NFD()

tokenizer.pre_tokenizer = Split(
    pattern=Regex(TOKENIZER_CHUNK_PATTERN),
    behavior="isolated",
)

tokenizer.post_processor = ByteLevelProcessor(trim_offsets=True)
# this should remove the extra spaces inserted by the tokenization process
# which make the output not decode to the original input
tokenizer.decoder = ByteLevelDecoder()

trainer = BpeTrainer(
    vocab_size=args.vocab_size,
    show_progress=True,
    special_tokens=list(SPECIAL_TOKENS.values()),
)

tokenizer.train_from_iterator(training_data, trainer=trainer)

if not args.dry_run:
    # save the vocab and merges files separately
    tokenizer.model.save(OUTPUT_PATH, DATASET_NAME)

    # save the tokenizer json output
    tokenizer.save(f"{OUTPUT_PATH}/{DATASET_NAME}.json")
    # save the vocab and merges files separately
    tokenizer.model.save(OUTPUT_PATH, DATASET_NAME)

    # save the tokenizer json output
    tokenizer.save(f"{OUTPUT_PATH}/{DATASET_NAME}.json")
