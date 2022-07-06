### OUTAGE에 사용되는 AI 를 학습시키는 목적을 가진 곳

#### 기능
##### - 이미지 구별( 농작물들을 구별하는 AI model)
##### - 농작물 시장 가격을 예측하는 AImodel 
이 두가지를 만들 예정 

###### - [crawling.py](https://github.com/dlatldhs/AI_training/blob/master/crawling.py)
```
이미지 구별을 하는 AI model에 학습에 필요한 사진들을 긁어 모아주는 기능을 가진 프로그램(in python) 
만든 이유: 사진의 양이 너무 많기도 하고 많은 데이터를 모아야 하여서 사람이 할 수 있는 작업이 아니였기 때문에 이 프로그램을 만듬
```

#### CNN(Convolutional Neural Networks)
- ##### 이미지 처리에 널리 쓰이는 모델
- ##### 수동으로 특징을 추출할 필요 X
- ##### 데이터로 부터 직접학습하는 딥러닝을 위한 아키텍처
```
특징 추출 영역은 합성곱층(convolution layer)과 풀링층(Pooling layer)을 여러 겹 쌓는 형태(Conv+Maxpool)로 구성되어 있으며
이미지의 클래스를 분류하는 부분은 Fully connected(FC) 학습 방식으로 이미지를 분류한다.
```

#### 회귀분석(Regression test)
```독립 변수가 종속 변수에 어떤 영향을 끼치는지 알아볼 때 쓰는 방법```<br>
독립 변수X 와 종속 변수Y 사이의 관계를 그래프로
``` p
from sklearn.linear_model import LinearRegression
LRmodel=LinearRegression()
LRmodel.fit(X.reshape(-1, 1), Y) # fit()는 X변수를 2차원으로 넣어줘야 함
# 독립변수가 두 개면 .coef_[0]와 .coef_[1] 두 개가 자동 생성됨
beta_0 = LRmodel.coef_[0] #기울기
beta_1 = LRmodel.intercept_ #y절편
plt.scatter(X, Y)
pred_Y = beta_0*X+beta_1   # pred_Y = LRmodel.predict(X.reshape(-1, 1))
plt.plot(X, pred_Y, c='r')
plt.show( )
print('beta_0: %.2f' %beta_0)
print('beta_1: %.2f' %beta_1)
print('Loss : %.2f' %loss(Y, pred_Y))
```
<img src="https://github.com/dlatldhs/AI_training/blob/master/imgs/%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D%EC%98%88%EC%A0%9C.png?raw=true" alt="회귀분석예제" />
나타낼 수 있다.<br>
또한 평균적으로 값이 너무 크거나 작은 이상한 값을 볼 수 있어서 일치율을 맞추기에 좋은 방법 중 하나이다.
