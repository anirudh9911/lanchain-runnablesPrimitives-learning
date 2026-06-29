# LangChain Runnables

A hands-on collection of examples exploring LangChain's **LCEL (LangChain Expression Language)** Runnable primitives — the building blocks for composing LLM chains.

## Concepts Covered

| File | Runnable | What it demonstrates |
|------|----------|----------------------|
| `runnable_sequence.py` | `RunnableSequence` | Chain multiple steps (prompt → model → parser) in sequence; also shows equivalent LCEL `|` pipe syntax |
| `runnable_parallel.py` | `RunnableParallel` | Run multiple chains in parallel on the same input (e.g. generate a tweet and a LinkedIn post simultaneously) |
| `runnable_passthrough.py` | `RunnablePassthrough` | Pass the original input through unchanged alongside transformed outputs |
| `runnable_lambda.py` | `RunnableLambda` | Wrap a plain Python function (e.g. word count) as a Runnable step inside a chain |
| `runnable_branch.py` | `RunnableBranch` | Conditionally route to different chains based on the output (e.g. summarize only if text exceeds 200 words) |

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/langchain-runnables.git
cd langchain-runnables
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

Run any example directly:

```bash
python runnable_sequence.py
python runnable_parallel.py
python runnable_passthrough.py
python runnable_lambda.py
python runnable_branch.py
```

## Requirements

- Python 3.9+
- OpenAI API key
