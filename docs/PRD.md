# Opis projektu
System to program CLI do wpisywania promptów do LLMa na konsoli.

# Komponenty docker-compise
- liteLLM proxy
- FastAPI

## Setup
- ma być użyty UV jako manager pakietów,
- do testów ma być skonfigurowny black, ruff i mypy
- ma być dodany pre-commit hook sprawdzajacy black, ruff i mypy
- Zmienne środowiskowe są umieszczone w pliku .env, .env.example jako przykład
- Do parsowania i walidacji  ma być użyty pydantic


## liteLLM proxy
Ma zdefiniowane dwa modele: openAI openai/gpt-5-nano i Groq groq/openai/gpt-oss-20b

## FastAPI
- Ma udostepniać jeden endpoint: /send-response (POST)

Ma wysyłać do LLM prompt urzytkownika. Ma być dodana kalsa, które wrapuje prompt użytkownika
w dodatkowy kontext.