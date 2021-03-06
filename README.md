<h1 align="center"> π streamlit-disease-pred-app</h1>

## π Description
β μμ μ΄ κ°μ§ μ¦μμ μ²΄ν¬ν΄ κ·Έ μ¦μλ€μ κ°μ§λ©΄ μ΄λ€ μ§λ³μ΄ μκΈΈ κ°λ₯μ±μ΄ λμμ§λ₯Ό μμΈ‘νλ νλ‘μ νΈμλλ€.

β λ°μ΄ν° μμ λν EDA κ²°κ³Όλ₯Ό λ³Ό μ μμ΅λλ€.

β μ§λ³ μμΈ‘μ Support Vector Machine μκ³ λ¦¬μ¦μ μ΄μ©νμ΅λλ€.
## π Dataset Source

 π μΆμ² : https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset?select=dataset.csv

##
## π  Environment

β Language : Python 3.7

##
## π¨ Installation

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


## πΌ Classifier

β Support Vector Machine μκ³ λ¦¬μ¦μ ν΅ν΄ κ°μ₯ μ μ¬ν μ§λ³μ μμΈ‘νμ΅λλ€.

<img width="1179" alt="svm" src="https://user-images.githubusercontent.com/105832330/172291034-6aad1ee9-83a7-4958-a6c0-0a681fde9879.png">

β GridSearchλ‘ κ°μ₯ μ νλκ° λμ νλΌλ―Έν°λ₯Ό κ΅¬νμ΅λλ€.

![grid](https://user-images.githubusercontent.com/105832330/172301486-409e3555-74f5-4254-a609-e3a4beb729f3.PNG)

β μ νλ  

![disease_accuracy](https://user-images.githubusercontent.com/105832330/172575747-0f45069b-a7f1-435a-8310-f4fb824ab448.JPG)

β Confusion Matrix
![cm](https://user-images.githubusercontent.com/105832330/172575896-8f23b23a-0c4a-49a3-bb49-144d488dc8bc.png)


## πΏ Usage

### μ€ννκΈ°
![disease_app_begin](https://user-images.githubusercontent.com/105832330/172292448-651ddc49-7eac-4203-ab88-80b6c7c2e7e1.gif)


### νμ€νΈ
![disease_app_test](https://user-images.githubusercontent.com/105832330/172293800-74360634-5790-4bc0-b80a-e3e3bd5a9b05.gif)

### Url
http://ec2-3-39-230-35.ap-northeast-2.compute.amazonaws.com:8504/
