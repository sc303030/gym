
[![codecov](https://codecov.io/gh/sc303030/gym/branch/master/graph/badge.svg?token=QXK0NIQM59)](https://codecov.io/gh/sc303030/gym)
![python](https://img.shields.io/badge/python-3.11-blue)
![python](https://img.shields.io/badge/django-4.1.4-orange)
## 대관 알리미
- 학교 체육관 대관 공지사항이 올라오면 카카오톡으로 알림을 보내주는 app입니다.

### poetry 설치
- window 기준
- WSL
```shell
curl -sSL https://install.python-poetry.org | python3 -
```
- Powershell
```shell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
- [윈도우 poetry 설치하기](https://maximum-curry30.tistory.com/435)

### poetry 설치하기
```shell
poetry install
```

### pytest 실행하기
```shell
poetry run pytest
```
- print 같이 출력하기
  - ```shell
    poetry run pytest -s
    ```
- 특정 파일만 테스트 하기
  - pyproject.toml 파일에서 tool.pytest.ini_options > addopts을 `addopts = "--reuse-db`으로 변경
  - ```shell
    poetry run pytest reminder/tests/test_model.py
    ```
  - 특정 파일 안에 있는 특정 함수만 테스트
  - ```shell
    poetry run pytest reminder/tests/test_model.py::test_create_school
    ```

### pre-commit, pre-push git hooks 설치
- pre-commit hook
```shell
pre-commit install
```

- pre-push hook
```shell
$ touch .git/hooks/pre-push
$ chmod +x .git/hooks/pre-push
$ cat <<EOF >> .git/hooks/pre-push
#!/bin/sh
poetry run pytest
status=$?

if [ $status  != 0 ]; then
    echo 'TEST FAILED! GIT PUSH REJECTED' && exit 1
else
    exit 0
fi
EOF
```
- 테스트가 0개면 에거가 발생하기 때문에 적어도 1개의 테스트를 만들어서 진행하기
