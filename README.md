# 'NLP 기반의 추천모델' <오늘 뭐 먹지?>

<div align= "center">
  <img width="400" src="https://i.esdrop.com/d/f/NXl6YkfhTU/90s6GXiFPx.jpg">
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

<h2> 🔌구축환경 및 requirements 설치</h2>

<h5>구축 환경 </h5>
  <h6>Python 3.7 </h6>

```python
pip install -r requirements.txt
```


<h2> 🍽 오늘 뭐 먹지? 🍽 </h2>

  <p>
<div>

<details>
<summary><b>메뉴명으로 추천 받기</b></summary>
<div align= "center">
  <img width="500" src = "https://i.esdrop.com/d/f/NXl6YkfhTU/xdZgV0Sevh.png">
</div>
  
  <h5>메뉴이름으로 추천받기</h5>
  <h6>첫 번째 추천방법은 ‘메뉴의 명’을 입력 했을 때입니다.<br><br>
      이 방법은 우리가 알고 있는 메뉴의 명을 넣게 되면 비슷한 식재료의 다른 레시피를 알려줌으로서 색다른 조리할 수 있다는 장점이 있습니다.<br><br><br>
  </h6>
  <p>
</details>
<details>
<summary><b>키워드로 추천 받기</b></summary>
<div align= "center">
  <img width="500" src = "https://i.esdrop.com/d/f/NXl6YkfhTU/DxzPNmNg9J.png">
</div>
  <h5>특정 키워드로 추천받기</h5>
  <h6>두 번째 추천방법은 ‘키워드’를 입력 했을 때입니다.<br><br>
      이 방법의 경우는 ‘크리스마스’, ‘갈치’, ‘쌀쌀한’ 등 키워드를 입력할 경우 분위기나 식재료에 걸 맞는 메뉴와 그 메뉴의 레시피를 추천 받을 수 있습니다.<br><br><br>
  </h6>

</div>
  </h6>
  
</div>
</details>
<details>
<summary><b>문장으로 추천 받기</b></summary>
<div align= "center">
  <img width="500" src = "https://i.esdrop.com/d/f/NXl6YkfhTU/Vf725py4ae.png">
</div>
  <h5>문장으로 추천받기</h5>
  <h6>세 번째 추천방법은 ‘문장’을 입력 했을 때입니다.<br><br>
      이 방법은 ‘아이가 너무 좋아하는 음식’처럼 문장을 입력하면 해당 문장에 맞는 음식과 음식의 레시피를 추천 받을 수 있습니다.<br><br><br>
  </h6>
</details>
