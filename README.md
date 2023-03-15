# today_menu

<div align= "center">
  <img width="850" src="https://i.esdrop.com/d/f/NXl6YkfhTU/90s6GXiFPx.jpg">
</div>
<br>
<br>


<h2> 📊 프로젝트 개요 </h2>

<div align= "center">
<!--   <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/Tov2sHONfa.png"> -->
</div>
<br>

먼저 ‘이밥차’ 사이트에 대한 소개를 하자면, ‘이밥차’의 뜻은 ‘2천원으로 밥상 차리기’ 라는 의미로, 저렴한 가격으로 한 끼 메뉴의 레시피를 볼 수 있는 사이트입니다. 

저희 프로젝트의 목적은 앞서 설명 드린 ‘이밥차’사이트에서 검색어와 높은 연관성을 지닌 요리 레시피 3개를 추천하는 NLP기반의 추천 모델의 생성입니다

프로젝트의 기획의도는 저렴한 가격으로 만들 수 있는 다양한 레시피를 검색 및 레시피를 제공해, 사용자가 외식과 배달음식의 횟수를 줄이고, 냉장고에 보관된 재료를 활용할 수 있도록 식재료 또는 원하는 분위기에 맞는 레시피를 제공을 해줍니다.

그리고 프로젝트의 기대효과는 다양하고 간결한 레시피 제공을 통해 요리가 미숙한 사람도 쉽게 요리 할 수 있고, 그날의 식단 고민시간을 줄일 수 있다는 점입니다.


<br>
<br>

<h2> 🔌requirements 설치 </h2>

```python
pip install -r requirements.txt
```

<h2> 🍽 오늘 뭐 먹지? 🍽 </h2>

  <p>
<div>

<details>
<summary><b>메뉴명으로 추천 받기</b></summary>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/NXl6YkfhTU/xdZgV0Sevh.png">
</div>
  <h5>구축 환경 </h5>
  <h6>Python 3.8 / Google Colab </h6>
  <h5>데이터셋</h5>
  <h6>챗봇의 데이터셋은 <'AI HUB'의 감성 대화 말뭉치>와 <웰니스 챗봇 데이터> 2가지를 활용하여 데이터셋을 구성했습니다.<br><br>
      데이터셋은 총 3개의 라벨로 구성되어 있으며, 라벨의 기준은 문장을 감정으로 분류하여 일상, 부정, 긍정으로 나누었습니다.<br><br><br>
  </h6>
  <p>
</details>
<details>
<summary><b>키워드로 추천 받기</b></summary>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/NXl6YkfhTU/DxzPNmNg9J.png">
</div>
  <h5> 모델 학습 과정 </h5>
  <h6> 학습은 max_epochs=15로 15번 반복하여 Train_loss값이 가장 낮은 모델을 저장하는 방식으로 진행됩니다.<br><br>
       데이터양, 라벨의 수, max_len 총 3가지를 수정하여 3회 정도 모델 학습을 진행하였습니다. <br><br>
       최종적으로 사용한 모델은 데이터량 약 236,000개 / 라벨 총 3개 / max_len = 64이며, epochs=4일 때, Train_loss가 31.63으로 가장 낮게 나왔습니다. <br><br>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/ZjI4VldVdJ.png">
</div>
  <br><br><br>
  </h6>
  
</div>
</details>
<details>
<summary><b>문장으로 추천 받기</b></summary>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/NXl6YkfhTU/Vf725py4ae.png">
</div>
</details>
