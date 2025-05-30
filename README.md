# <font size="6">AskMeX Chatbot</font>

<font size="4">A Twitter news aggregator chatbot that fetches recent tweets on any topic, performs text summarization and sentiment analysis, and displays results through an interactive interface.</font>

## <font size="5">🐦 Overview</font>

<font size="3">AskMeX Chatbot helps you stay updated with the latest Twitter discussions on any topic. Simply enter your query, and get the top 5 recent tweets with automatic text summarization and sentiment analysis powered by NLP techniques.</font>

## <font size="5">✨ Features</font>

<font size="3">
- Real-time Twitter data fetching using X Developer API
- Top 5 most relevant tweets retrieval
- Automatic text summarization using TextBlob
- Sentiment analysis (Positive/Negative/Neutral)
- Interactive and user-friendly Streamlit interface
- Query-based news aggregation
- Clean and organized tweet display
</font>

## <font size="5">🛠️ Technologies Used</font>

<font size="3">
- **Python** - Main programming language
- **X Developer API** - Twitter data fetching
- **TextBlob** - NLP text processing and sentiment analysis
- **Streamlit** - Interactive web interface
- **Pandas** - Data manipulation
- **Requests** - API calls handling
</font>

## <font size="5">🚀 Installation & Setup</font>

<font size="3">

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/askmex-chatbot.git
   cd askmex-chatbot
   ```

2. **Install required packages**
   ```bash
   pip install streamlit textblob pandas requests tweepy
   ```

3. **Set up X Developer API**
   - Get your API keys from [X Developer Portal](https://developer.twitter.com/)
   - Create a `config.py` file and add your API credentials:
   ```python
   API_KEY = "your_api_key"
   API_SECRET = "your_api_secret"
   ACCESS_TOKEN = "your_access_token"
   ACCESS_TOKEN_SECRET = "your_access_token_secret"
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the app**
   - Open your browser and go to `http://localhost:8501`

</font>

## <font size="5">💻 How It Works</font>

<font size="3">

### 1. **Query Input**
- User enters a topic or keyword in the chatbot interface

### 2. **Twitter Data Fetching**
- Uses X Developer API to fetch recent tweets related to the query
- Retrieves top 5 most relevant and recent tweets

### 3. **NLP Processing**
- **TextBlob** processes the tweet content
- Performs text summarization to extract key information
- Handles textual data cleaning and preprocessing

### 4. **Sentiment Analysis**
- Analyzes the emotional tone of each tweet
- Classifies sentiments as Positive, Negative, or Neutral
- Provides sentiment scores for better understanding

### 5. **Interactive Display**
- Streamlit interface presents results in an organized manner
- Shows tweet content, summary, and sentiment analysis
- User-friendly design with real-time updates

</font>

## <font size="5">🎯 Usage</font>

<font size="3">
1. Launch the Streamlit application
2. Enter your topic of interest in the input field
3. Click "Get Latest News" or press Enter
4. View the top 5 tweets with:
   - Original tweet content
   - Summarized version
   - Sentiment analysis results
5. Try different queries to explore various topics
</font>

## <font size="5">📁 Project Structure</font>

<font size="3">
```
askmex-chatbot/
│
├── app.py                 # Main Streamlit application
├── twitter_api.py         # X Developer API integration
├── summary.py       # TextBlob NLP processing
└── README.md             # Project documentation
```
</font>

## <font size="5">🔧 Key Concepts</font>

<font size="3">

### **1. API Integration**
- Utilizes X Developer API for real-time Twitter data access
- Handles authentication and rate limiting
- Fetches tweets based on user queries with proper filtering

### **2. Natural Language Processing (NLP)**
- **TextBlob Library**: Core NLP engine for text processing
- **Text Summarization**: Extracts key information from lengthy tweets
- **Sentiment Analysis**: Classifies emotions as Positive, Negative, or Neutral
- **Text Preprocessing**: Cleans and normalizes tweet content

### **3. Data Processing Pipeline**
- **Query Processing**: Handles user input and search parameters
- **Tweet Filtering**: Selects top 5 most relevant tweets
- **Content Extraction**: Removes unnecessary elements (URLs, mentions, hashtags)
- **Data Structuring**: Organizes information for display

### **4. Interactive User Interface**
- **Streamlit Framework**: Creates responsive web-based chatbot
- **Real-time Updates**: Displays results instantly after query submission
- **User-friendly Design**: Simple input field with clear output formatting
- **Responsive Layout**: Adapts to different screen sizes

### **5. Sentiment Analysis Engine**
- **Polarity Detection**: Measures positive vs negative sentiment (-1 to +1 scale)
- **Subjectivity Analysis**: Determines factual vs opinion-based content
- **Emotion Classification**: Categorizes overall tweet mood
- **Visual Indicators**: Uses colors/icons to represent sentiment results

</font>

## <font size="5">📊 Features Breakdown</font>

<font size="3">
- **Real-time Data**: Fetches the most recent tweets
- **Smart Summarization**: Extracts key points from lengthy tweets
- **Emotion Detection**: Understands the mood of discussions
- **User-friendly Interface**: Simple and intuitive design
- **Query Flexibility**: Works with any topic or keyword
</font>

## <font size="5">🤝 Contributing</font>

<font size="3">Feel free to fork this repository and submit pull requests for any improvements or new features.</font>

## <font size="5">👤 Author</font>

<font size="3">
**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
</font>

## <font size="5">🙏 Acknowledgments</font>

<font size="3">
- X Developer Platform for providing Twitter API access
- TextBlob community for NLP tools
- Streamlit team for the amazing web framework
</font>
