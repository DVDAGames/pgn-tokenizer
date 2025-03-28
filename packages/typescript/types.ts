/**
 * Types for PGN Tokenizer Configuration
 */

/**
 * Represents a token added to the tokenizer's vocabulary
 */
export interface AddedToken {
  /** Unique identifier for the token */
  id: number;
  /** The actual content of the token */
  content: string;
  /** Whether the token is a single word */
  single_word: boolean;
  /** Whether to strip whitespace from the left */
  lstrip: boolean;
  /** Whether to strip whitespace from the right */
  rstrip: boolean;
  /** Whether the token is normalized */
  normalized: boolean;
  /** Whether this is a special token */
  special: boolean;
}

/**
 * Configuration for the normalizer
 */
export interface Normalizer {
  /** Type of normalization to apply */
  type: string;
}

/**
 * Configuration for the pre-tokenizer
 */
export interface PreTokenizer {
  /** Type of pre-tokenizer */
  type: string;
  /** Pattern configuration */
  pattern: {
    /** Regular expression pattern */
    Regex: string;
  };
  /** Behavior of the pre-tokenizer */
  behavior: string;
  /** Whether to invert the pattern matching */
  invert: boolean;
}

/**
 * Configuration for byte-level processing
 */
export interface PostProcessorConfig {
  /** Type of processor */
  type: string;
  /** Whether to add prefix space */
  add_prefix_space: boolean;
  /** Whether to trim offsets */
  trim_offsets: boolean;
  /** Whether to use regex */
  use_regex: boolean;
}

/**
 * Configuration for the BPE model
 */
export interface ModelConfig {
  /** Type of the model */
  type: string;
  /** Dropout rate */
  dropout: number | null;
  /** Token to use for unknown tokens */
  unk_token: string;
  /** Prefix for continuing subwords */
  continuing_subword_prefix: string | null;
  /** Suffix for end of words */
  end_of_word_suffix: string | null;
  /** Whether to fuse unknown tokens */
  fuse_unk: boolean;
  /** Whether to use byte fallback */
  byte_fallback: boolean;
  /** Whether to ignore merges */
  ignore_merges: boolean;
  /** Vocabulary mapping */
  vocab: Record<string, number>;
  /** Merge rules */
  merges: string[][];
}

/**
 * Main configuration type for the PGN tokenizer
 */
export interface PGNTokenizerConfig {
  /** Version of the tokenizer configuration */
  version: string;
  /** Truncation configuration */
  truncation: null;
  /** Padding configuration */
  padding: null;
  /** List of added tokens */
  added_tokens: AddedToken[];
  /** Normalizer configuration */
  normalizer: Normalizer;
  /** Pre-tokenizer configuration */
  pre_tokenizer: PreTokenizer;
  /** Post-processor configuration */
  post_processor: PostProcessorConfig;
  /** Decoder configuration */
  decoder: PostProcessorConfig;
  /** Model configuration */
  model: ModelConfig;
}
