# 🧠 Chatbot IA Local com Personalidade Channer

Chatbot avançado treinado em Python com NLP (nltk + sklearn), totalmente offline e com personalidade baseada em imageboards como 4chan e Reddit. Sem necessidade de APIs ou login em serviços externos.

---

## 🚀 Como usar

```bash
pip install -r requirements.txt
python model/train_model.py
python main.py
```

---

## 📁 Estrutura

- `data/intents.json`: intenções básicas do bot
- `data/greentexts.json`: respostas no estilo greentext
- `data/slang_dict.json`: dicionário de gírias e jargões de chans
- `model/train_model.py`: treinamento do classificador com NLP
- `main.py`: executa a IA no terminal
- `bot.py`: conecta entrada, modelo e personalidade
- `persona.py`: lógica de respostas com estilo informal e irônico

---

## 🧩 Funcionalidades

✅ Interpretação de frases com gírias channer
✅ Respostas no estilo greentext (`>be me...`)
✅ Base de conhecimento local com intents configuráveis
✅ Estilo sarcástico, shitpost ou neutro baseado no contexto
✅ Totalmente offline

---

## 🛠️ Funcionalidades Futuras

🔸 **Filtro de conteúdo criminoso ou ilegal** (moderador interno)
🔸 **Análise semântica profunda com embedding local**
🔸 **Aprendizado contínuo a partir do histórico de conversa**
🔸 **Geração de memes contextuais baseados na conversa**
🔸 **Exportação de logs e modo debug para análise de chats**

---

## 👨‍💻 Requisitos

- Python 3.9+
- nltk
- scikit-learn
- numpy

Tudo listado no `requirements.txt`

---

## 📦 Contribuições

Contribuições são bem-vindas! Crie um fork e envie seu PR com melhorias, novos intents ou mais greentexts.

---

## 🕸️ Filosofia

Esse projeto busca simular um bot com conhecimento da cultura channer, com vocabulário realista, ironia, e respostas autênticas para quem vive o submundo dos imageboards.