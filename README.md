# greet-release

인사말 프로그램. 버전은 유의적 버전(Semantic Versioning)을 따른다.

## 설치와 실행

```
uv sync
uv run --locked python greet.py Hee
uv run --locked python greet.py
uv run --locked pytest -q greet.py
```
