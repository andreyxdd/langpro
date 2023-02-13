# LangPro API

To install necessary packages:
```
pip install -r requirements.txt
```

To start server:
```
uvicorn main:app --reload
```

To add newly installed packaged:
```
pip3 freeze > requirements.txt
```

To work with GPT-3 model you need to get your personal API key on [openai website](http://openai.com) and save it in this folder as `openai_apikey.txt`