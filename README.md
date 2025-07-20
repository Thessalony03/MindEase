# MindEase — Mental Health Support Bot 🤝

---

## 🎯 Problem

Every 40 seconds, someone loses their life to suicide.  
Students under stress often delay seeking help — this makes anxiety and burnout worse.

---

## 💡 Solution

**MindEase** is a conversational AI companion for students.  
Built with Google’s Vertex AI Agent Builder, it guides them through:
- Safe, step-by-step journaling
- Real-time sentiment detection using Cloud Run + NLP API
- Instant affirmations and mood-based comfort

---

## 🧩 Tech Stack

- Vertex AI Agent Builder (Dialogflow CX)
- Python Cloud Function (Cloud Run)
- Google Natural Language API (Sentiment Analysis)
- Firestore (optional session storage)

---

## 🔑 Features

- Intent-based small talk & mood check with custom payloads
- Guided journaling flow with multiple pages
- Sentiment webhook: NLP score + adaptive messages
- Uplifting affirmation and journaling again option
- Re-entry to Main Menu anytime

---

## 🔗 Architecture Diagram

!Architecture Diagram : <img width="2076" height="1592" alt="MindEase - FlowChart" src="https://github.com/user-attachments/assets/81dfad56-20b4-4aa1-ac1e-92af4d4748a5" />


---

## 🚀 How to Deploy

1. Create a Dialogflow CX agent in Vertex AI Agent Builder.
2. Set up intents, pages, flows, and custom payload chips.
3. Deploy Python webhook on Cloud Run:
   - Use `main.py` and `requirements.txt`
   - Add your JSON key
4. Configure fulfillment:
   - Add webhook URL in CX agent
   - Map session parameters for NLP score
5. Test end-to-end in CX simulator.

---

## 📂 Project Structure
MindEase/
│
├── main.py
├── requirements.txt
├── flowchart/diagram.png
├── README.md
├── screenshots/


---

## 📑 License & Credits

MIT License — Free for anyone to learn from.  
Built by Thessalony Dudde — AI & Conversational Design Enthusiast.

---

## 🤝 Connect

LinkedIn : https://www.linkedin.com/in/thessalony-dudde-533636243/ 
[Notion Portfolio](YOUR_NOTION_LINK)



