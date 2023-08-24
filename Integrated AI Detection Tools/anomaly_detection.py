import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# 데이터셋 생성
np.random.seed(0)
normal_behavior = np.random.normal(0, 1, (1000, 10))
anomalous_behavior = np.random.normal(5, 1, (100, 10))

# 정상과 이상 동작을 합침
data = np.vstack((normal_behavior, anomalous_behavior))
labels = np.hstack((np.zeros(1000), np.ones(100)))

# 데이터셋 분할
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=0)

# 이상 행동 탐지 모델 구축
model = Sequential([
    Dense(10, input_dim=10, activation='relu'),
    Dense(5, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer=Adam(lr=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# 모델 학습
model.fit(x_train, y_train, epochs=20, batch_size=32, validation_data=(x_test, y_test))

# 이상행동 탐지 예측
predictions = model.predict(x_test)
anomalous_indices = np.where(predictions > 0.5)[0]

# 결과 출력
print("Detected anomalies:", anomalous_indices)

# 악의적인 동작 시뮬레이션 (새로운 동작)
new_behavior = np.random.normal(10, 1, (50, 10))  # 새로운 동작 생성
new_predictions = model.predict(new_behavior)

for i, prediction in enumerate(new_predictions):
    if prediction > 0.5:  # 임계값 설정
        print(f"Anomaly Detected in new behavior {i + 1}!")
        
#시스템 로그, 네트워크 트래픽, 사용자 행동 등의 데이터를 모니터링하고, 통계적, 머신러닝, 딥러닝 등의 방법을 사용하여 정상 동작과 이상 동작을 구분 