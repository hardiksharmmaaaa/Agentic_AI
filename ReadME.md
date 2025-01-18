# **Finance_Agent**  

## 🚀 Project Overview
The **Finance_Agent** project is an innovative, agent-based AI application designed to deliver actionable insights and the latest financial news. This project comprises two intelligent agents:  

1. **Web_Search Agent**:  
   - Scans the web to fetch answers for any queries.  
   - Supports searching for real-time data, facts, or reports on various financial topics.  

2. **Finance_Agent**:  
   - Equipped with financial expertise and contextual knowledge.  
   - Provides the latest financial news, trends, and market insights based on user prompts.  

## 📁 Project Structure
The project is organized into the following core files and directories:

```plaintext
Finance_Agent/
├── finance_agent.py          # Main file for Finance_Agent functionality
├── web_search_agent.py       # Main file for Web_Search Agent functionality
├── requirements.txt          # Dependencies for the project
├── README.md                 # Project documentation
├── config/                   # Configuration files for API keys and settings
│   ├── api_keys.json         # API keys for web search and news
│   └── settings.json         # General agent configurations
├── examples/                 # Example prompts and usage demonstrations
│   ├── example1.txt          # Sample prompt for Finance_Agent
│   └── example2.txt          # Sample query for Web_Search Agent
└── tests/                    # Test cases for both agents
    ├── test_finance_agent.py # Unit tests for Finance_Agent
    └── test_web_search.py    # Unit tests for Web_Search Agent
```

---

## 🛠️ Features
### **Web_Search Agent**
- Searches the web in real time for user-specified queries.
- Retrieves accurate, up-to-date information.
- Supports advanced query customization (e.g., filtering by date, source, etc.).

### **Finance_Agent**
- Provides curated financial news and insights.
- Responds to specific prompts, such as:
  - *"What are the latest trends in the stock market?"*
  - *"Tell me about recent developments in cryptocurrency."*
- Can analyze and summarize information for user-friendly output.

---

## 📋 Prerequisites
To run this project, ensure you have the following:

1. **Python**: Version 3.8 or higher.
2. **API Keys**: Obtain keys for web search (e.g., Google Search API or Bing Search API) and news data.
3. **Libraries**: Install dependencies listed in `requirements.txt`.

---

## 🖥️ Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/Finance_Agent.git
   cd Finance_Agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add API keys:
   - Open the `config/api_keys.json` file and replace placeholders with your actual keys:
     ```json
     {
       "web_search_api_key": "YOUR_WEB_SEARCH_API_KEY",
       "news_api_key": "YOUR_NEWS_API_KEY"
     }
     ```

---

## 🔄 Usage
### **1. Running the Agents**
To start the agents, run the respective Python scripts:

- **Web_Search Agent**:
  ```bash
  python web_search_agent.py
  ```

- **Finance_Agent**:
  ```bash
  python finance_agent.py
  ```

### **2. Example Queries**
- For the **Web_Search Agent**, you can input:
  ```
  Find the latest stock prices for Tesla.
  ```
- For the **Finance_Agent**, try prompts like:
  ```
  Give me the latest financial news on cryptocurrency.
  ```

### **3. Combined Usage**
Both agents can work together in an integrated pipeline:
```bash
python main.py
```
Provide a prompt, and the system intelligently decides which agent to use.

---

## 🔍 Example Output
### **Finance_Agent**
Prompt:
```
What are the latest updates on Bitcoin?
```
Output:
```
[Finance_Agent]: Bitcoin rose by 2.3% today, trading at $45,000. Recent reports indicate increased adoption among institutional investors. The SEC is reviewing applications for new Bitcoin ETFs.
```

### **Web_Search Agent**
Prompt:
```
Search for "latest financial regulations in the EU."
```
Output:
```
[Web_Search Agent]: According to a recent report by Reuters, the EU is considering stricter financial regulations on cryptocurrencies to prevent money laundering. Read more: [Link to Article]
```

---

## 🧪 Testing
Run unit tests to ensure the functionality of both agents:
```bash
pytest tests/
```

---

## 🛡️ Security Notes
- Keep your API keys secure; do not share them publicly.
- Follow best practices for storing sensitive data.

---

## 🤝 Contribution Guidelines
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with a detailed description.

---

## 📞 Support
For questions or issues, contact:
- **Email**: hardiksharmaa007@gmail.com


---

