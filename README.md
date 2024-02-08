# Sign Language Detection Language Translator

## 수화 모션 감지 번역기

### 프로젝트 셋업 가이드

1. 깃허브 리포지토리 클론 하기

   - CMD : `git clone https://github.com/HoyeonS/SLDVT.git`

2. 파이썬 virtual environment 만들기 (Recommended Name: "sldvt_env")

   - CMD : `python3 -m venv sldvt_env`

3. 파이썬 activate 하기 (Recommended Name: "sldvt_env")

   - CMD : `source sldvt_env/bin/activate`

4. Dependency Installation
   - CMD : `cd SLDVT && pip3 install -r requirements.txt`

### Update Dependencies

```pip freeze > requirements.txt```


### Troubleshoot 
* Python Version == 3.11.2 (latest version will not support mediapipe)
* command is only available for mac with linux bash
* requirements.txt 로 다운하기 어려운 경우 문서에 나와있는 디펜던시표 따라 인스톨하기
  
