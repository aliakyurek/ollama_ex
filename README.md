# ollama_ex

## Setup

**Install [uv](https://github.com/astral-sh/uv):**
  ```sh
  pip install uv
  ```

**Clone the repository:**
  ```sh
  git clone https://github.com/aliakyurek/ollama_ex.git
  cd ollama_ex
  ```

**Install dependencies:**<br>
   uv will automatically create a virtual env and install the dependencies listed in `uv.lock` file.
   ```sh
   uv sync --no-dev
   ```
## Usage
* Notebook `main.ipynb` has following binding examples
  * Ollama native
  * Ollama openai
  * Langchain
  * Litellm
* Walkthrough of the examples is available in the notebook.

## Development
**Setup venv:**
```sh
uv venv
.venv\Scripts\activate
```
**Install deps:**<br>
Default dependencies
```sh
uv pip install -r pyproject.toml
```
Then groups
```sh
uv pip install --group dev
```
All together
```sh
uv pip install -r pyproject.toml --group dev
```

**Add a new dependency:**<br>
Without updating `pyproject.toml` and `uv.lock` files:
```sh
uv pip install <package_name>
```
With updating `pyproject.toml` and `uv.lock` files:
```sh
uv add <package_name>
```
Specify group:
```sh
uv add <package_name> --group dev
```




## References
- [uv](https://medium.com/@gnetkov/start-using-uv-python-package-manager-for-better-dependency-management-183e7e428760)