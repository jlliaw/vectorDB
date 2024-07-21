# download model from hugginface
1. taide 模型授權
2. 建立 write permission 的token (refer to : https://huggingface.co/settings/tokens)
3. 安裝 huggingface-cli (refer to : https://huggingface.co/docs/huggingface_hub/guides/cli)
```
pip install -U "huggingface_hub[cli]"
```
4. 指令(待確認哪一個可以用...XD)
```
$ huggingface-cli download --local-dir taide8b --token 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 taide/Llama3-TAIDE-LX-8B-Chat-Alpha1
$ huggingface-cli login
$ huggingface-cli download --local-dir taide8b taide/Llama3-TAIDE-LX-8B-Chat-Alpha1
$ huggingface-cli download taide/Llama3-TAIDE-LX-8B-Chat-Alpha1
```

參考資料:
https://ihower.tw/blog/archives/11933

https://huggingface.co/docs/transformers/index

https://huggingface.co/docs/tokenizers/index

https://huggingface.co/learn/nlp-course/chapter2/4
