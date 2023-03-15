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

<h2> 🔌코드 실행 </h2>

```python
pip install -r requirements.txt
```

<h5> 챗봇 학습 </h5>

```python
# python train_torch.py --train --gpus 1 --max_epochs 15
```
<h6> 해당 코드를 통해 데이터를 학습시켜 CheckPoint를 만들어냅니다.<br><br>
     만든 CheckPoint는 --chat 명령어를 사용하는데 이용됩니다. <br><br><br>
</h6> 

<h5> YOLO 학습 </h5>

```python
python ./Yolov5/train.py --data ./fall_dataset/data.yaml --epochs 100 --weights ./yolov5s.pt --batch-size 64 --img 640
```

<h6> 해당 코드를 입력하면 코드에 들어있는 규칙에 맞는.pt 파일을 만들어줍니다.<br><br>
     --data 에는 본인들이 사용할 이미지 데이터셋과 라벨로 구성된 .yaml파일 이름을 넣어주면 됩니다. <br><br>
     --weight는 기존의 Pre-Trained 모델로, 다양한 모델이 있지만 해당 프로젝트는 실시간 감지가 가장 주가 되기 때문에, yolov5s.pt를 사용했습니다.<br><br><br>
</h6>
     
     

<h5> 웹사이트로 들어가기 </h5>



```python
if __name__ == '__main__':
    # app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
    app.run(host="0.0.0.0", debug=True, port=int(os.environ.get("PORT", 5000)))
```

<h6> app_flask_chatbot.py 내의 코드로, Flask를 통한 웹사이트가 생성됩니다. <br><br>
     웹사이트는 해당 레퍼지토리의 Templetes, static 폴더 내의 파일을 수정하여 수정할 수 있습니다. <br><br>
     사이트 내에 있는 각 카테고리의 사진을 누르게 되면 챗봇 또는 실시간 감지창으로 넘어가게 됩니다. <br><br><br>
</h6>
