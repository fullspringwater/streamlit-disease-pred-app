<h1 align="center"> 🙌 streamlit-disease-pred-app</h1>

## 📃 Description
✅ 자신이 가진 증상을 체크해 그 증상들을 가지면 어떤 질병이 생길 가능성이 높은지를 예측하는 프로젝트입니다.

✅ 데이터 셋에 대한 EDA 결과를 볼 수 있습니다.

✅ 질병 예측은 Support Vector Machine 알고리즘을 이용했습니다.
## 📘 Dataset Source

 👉 출처 : https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset?select=dataset.csv

##
## 🛠 Environment

✅ Language : Python 3.7

##
## 🔨 Installation

```
pip install streamlit
```

```
pip install streamlit-option-menu
```

```
pip install joblib
```

```
pip install plotly==5.8.0
```

```
pip install scikit-learn
```


## 💼 Classifier

✅ Support Vector Machine 알고리즘을 통해 가장 유사한 질병을 예측했습니다.

<img width="1179" alt="svm" src="https://user-images.githubusercontent.com/105832330/172291034-6aad1ee9-83a7-4958-a6c0-0a681fde9879.png">

✅ GridSearch로 가장 정확도가 높은 파라미터를 구했습니다.

![grid](https://user-images.githubusercontent.com/105832330/172301486-409e3555-74f5-4254-a609-e3a4beb729f3.PNG)

✅ 정확도  

![disease_accuracy](https://user-images.githubusercontent.com/105832330/172575747-0f45069b-a7f1-435a-8310-f4fb824ab448.JPG)

✅ Confusion Matrix
![cm](https://user-images.githubusercontent.com/105832330/172575896-8f23b23a-0c4a-49a3-bb49-144d488dc8bc.png)


## 💿 Usage

### 실행하기
![disease_app_begin](https://user-images.githubusercontent.com/105832330/172292448-651ddc49-7eac-4203-ab88-80b6c7c2e7e1.gif)


### 테스트
![disease_app_test](https://user-images.githubusercontent.com/105832330/172293800-74360634-5790-4bc0-b80a-e3e3bd5a9b05.gif)

### Url
http://ec2-13-125-205-104.ap-northeast-2.compute.amazonaws.com:8501/
