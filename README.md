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
