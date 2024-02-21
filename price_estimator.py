import tiktoken

# Here is a unit test
enc = tiktoken.get_encoding("cl100k_base")
assert enc.decode(enc.encode("hello world")) == "hello world"

#=======================================================================
model = 'gpt-4' # the model to test
price = 0.03  # the cost per 1000 tokens 

'''
Check here for the latest price: https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/)

Please note that cost of the prompt (input) and the answer (output) from LLM is different, but I did not disguish the
two cases in this script. 
If your task is a classification task, and the answer is just one or two words, you can use the input price.
If your task is a text generation task, you may need to use the output price or the mean of input and output prices.

To estimate the maximum value, use the output price.
'''

# To get the tokeniser corresponding to a specific model in the OpenAI API:
enc = tiktoken.encoding_for_model(model)

# Read the prompt file
prompt_file = 'prompt/p1.txt'
with open(prompt_file) as f:
    prompt_text = f.read()

# Read data
import pandas as pd
df = pd.read_csv('data/abstract_sample.csv', dtype=str)

# Tokenization
all_tokens = []
for i, text in enumerate(df['Abstract']):
    input_text = text + '\n' + prompt_text
    tokens = enc.encode(input_text)
    all_tokens += tokens
    print(f'{i}\t{len(tokens)}')

print('Total tokens:', len(all_tokens))
print('Estimate price (USD):', int(len(all_tokens) * price/1000))
