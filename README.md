# LLM_scripts
This repository is for sharing the codes for LLMs.

# Files
* `run_predict.py`: the script to prompt the LLM via the Azure OpenAI API.
* `prompt/p1.txt`: an example prompt
* `data/abstract_sample.csv`: an example data set
* `price_estimator.py`: a script to compute the cost of Azure API. Run `python price_estimator.py`. 
The example data and prompt was to prompt the LLM to extract the mean and deviation of blood pressure values based on biomedical sex.
The output wil be stored in a csv file named "cases_with_responses_{model_id}_{timestamp}".

A JSON file called "{prompt_file}.json" will also be created to keep track of predicted samples. If the script is run again with the same sample, it will first check the JSON file. If the sample is there, it will use the previous result without calling the API again.


# Running the script
The script should be executable by running `python run_predict.py` in the terminal/commandline with a Python3 environment.
To adapt the script to your task, you need to follow the steps below.
## 1. Update the Azure OpenAI API information with your own API
```
# API info
model_id = 'gpt-35'
openai.api_type = "azure"
openai.api_version = "2023-07-01-preview"
openai.api_base = "https://yguo262.openai.azure.com/"
openai.api_key = os.getenv("OPENAI_API_KEY")
engine_id = 'gpt35'
``` 
You can find these variables in the Chat playground on the Azure OpenAI platform. Just click the "View code" button to see the example code, which has all the information except for `model_id` and `engine_id`. You can choose any name for `model_id` to label the model, and `engine_id` is the API's deployment name.


Keep in mind that the code grabs the API key from the place where you're running it. To set the key, you can use `export OPENAI_API_KEY=xxxxxxx` in the command line. Just remember, you'll have to do this every time you open a new terminal.

If you prefer, you can directly insert the key into the code. It's easy, but be cautious not to accidentally upload your code with the key to Github.


## 2. Update the file path of the data and prompt.
You may also want to update these varibles:
```
col_id_name = 'ID'
col_text_name = 'Abstract'
text_placeholder = '{{abstract}}'
```
`col_id_name` is the column used as a key in the JSON file, `col_text_name` is the column of the text content, and `text_placeholder` is consistent with the prompt.
