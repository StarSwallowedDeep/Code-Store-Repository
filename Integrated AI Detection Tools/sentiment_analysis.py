from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# 감정 분석 객체 생성
analyzer = SentimentIntensityAnalyzer()

# 감정 분석 수행 함수
def analyze_sentiment(text):
    sentiment_scores = analyzer.polarity_scores(text)
    compound_score = sentiment_scores['compound']
    
    if compound_score >= 0.05:
        sentiment = "Positive"
    elif compound_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment, compound_score

# 텍스트 입력 받기
new_text = input("Enter a sentence: ")

# 감정 분석 수행
sentiment, score = analyze_sentiment(new_text)

# 결과 출력
print(f"Sentiment: {sentiment}, Score: {score:.2f}")