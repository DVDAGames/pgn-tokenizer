import PGNTokenizer from "./tokenizer";

const pgnTokenizer = new PGNTokenizer();

const encode = pgnTokenizer.encode.bind(pgnTokenizer);
const decode = pgnTokenizer.decode.bind(pgnTokenizer);

export default pgnTokenizer;

export { encode, decode };
