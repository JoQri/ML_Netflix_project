# 🖥 Machine Learning Project
![Netflix_Logo_RGB](https://github.com/ML-project-3/ML_project/assets/80812507/46328e49-769a-4623-a16a-0288e7a1ba3c)
---
## 💡 Introduction
**넷플릭스 시즌제 드라마의 후속작 흥행 예측**  
Predicting the Next Big Hit Netflix Sequel Drama

## 프로젝트 개요
1. 팀원: 강민지, 김이영, 이예슬, 조규리, 천준규
2. 수행 기간: 2024.05.28 \~ 2024.06.28 (4주)

## 프로젝트 소개
### 배경
- Why Netflix?
    - 넷플릭스는 글로벌 스트리밍 시장을 선도하는 기업으로, 현재 190개 국가에서 서비스 中
    - OTT 시장의 성숙기 진입 -> 미국을 중심으로 스트리밍 시장 포화
    - 넷플릭스 또한 수익 증가율, 구독자 증가율이 둔화되고 있음
    -> '컨텐츠'를 통해 비즈니스 문제를 해결할 수 있음  
  <출처:한국콘텐츠진흥원, '글로벌 OTT 트렌드 Vol 5', 2024.05.14., 'https://www.kocca.kr/globalOTT/vol05/main/index.html'>
- Why Drama?
    - 드라마는 긴 서사 구조 -> 시청자들의 지속적인 관심을 확보 가능
    -> 구독자 유지, 수익 안정성에 기여

![넷플릭스그래프](https://github.com/ML-project-3/ML_project/assets/80812507/654ac587-59f8-43cb-b5c8-c90ea909fa97)
<출처:BACKLINKO, 'Netflix User & Growth Stats: How Many People Subscribe?', 2024.04.08., https://backlinko.com/netflix-users>


### 프로젝트 진행 순서
![플로우차트 (1)](https://github.com/ML-project-3/ML_project/assets/155655348/007df57f-8f62-4b23-9fed-230d74c56556)

## 데이터 수집(크롤링)
![image](https://github.com/ML-project-3/ML_project/assets/155655348/a09a657a-5c8d-4092-983c-840a23e3da8f)

- **프로젝트 전제조건**: 한국 넷플릭스에서 현재 시청 가능한 드라마 중 ~ 2023. 12. 31까지의 작품 (크롤링 날짜: 2024.06.10.)
- **JustWatch**
    - 스트리밍 동영상 검색 엔진
    - 국내에서 서비스 중인 넷플릭스 드라마 데이터 확보에 이용
   **IMDb**
   - 세계 최대의 영상 매체 데이터 베이스
   - 글로벌 평반 반영
- **Watcha**
  - 한국의 영상 매체 데이터 베이스
  - 동양권 드라마에 대한 평판 보완

## 데이터 전처리
<details>
<summary><b> 결측치, 이상치 처리 1090개 ➡ 905개 </b></summary>
  
> **결측치** :  
> < IMDb >
> 1. 연령 등급 보완: 넷플릭스 공식 자료를 참고하여 연령 등급 결측치 보완
> 2. 에피소드 별 평점 결측치 삭제: 드라마 시즌 1, 2의 에피소드 별 평점에 하나라도 결측치가 있을 시 제외
> 3. 한국 방영과의 괴리 해소: 외국에서는 방영했으나 한국에서 서비스하지 않은 경우 그 시즌만 삭제
> 4. 외전 삭제: 정식 시즌이 아니므로 제외
> ---
> < Watcha >
> 1. 평점 통합: 하나의 시즌을 파트 1, 파트 2로 구분한 경우 평균으로 처리
> 2. 결측치 보완 및 삭제:드라마 평점이 존재하지 않는 경우 제작 국가 별 중앙값으로 처리
>
> **이상치** :  
> 
> -> 


  
</details>

## EDA
![image](https://github.com/ML-project-3/ML_project/assets/80812507/812a1b3d-1fcb-4b79-9938-a149091b2cb2)
- 시즌 1개만 있는 드라마(단일 드라마)가 639개, 시즌 2개(시즌제 드라마)가 있는 드라마는 266개
---

![image](https://github.com/ML-project-3/ML_project/assets/155655348/abd01e5d-c250-4e8a-941b-68ad61d565a7)
- 시즌제 드라마의 제작이 2021년부터 감소 추세를 보임. 반면 단일 드라마의 제작은 활발함  
---

![image (1)](https://github.com/ML-project-3/ML_project/assets/80812507/a83d29c9-031c-45e3-a12a-3d0e39474b1e)
- 시즌 1, 2의 평점, 평점 참여 인원 수 데이터가 선형적임을 알 수 있음
---

![image (2)](https://github.com/ML-project-3/ML_project/assets/80812507/f0a3430a-6679-45f3-85c9-12503e4a9568)
- 미국이 221개, 대한민국이 176개로 넷플릭스 드라마가 가장 많은 두 나라임을 확인
---

![image (3)](https://github.com/ML-project-3/ML_project/assets/80812507/61bd19b4-e4e1-49e2-879b-9251f3277424)
- 19세 연령의 드라마가 가장 많으며, 그 다음으로는 15세 연령의 드라마가 많음. 가장 적은 시청 등급의 드라마는 7세임을 확인
---

## 흥행 지표 생성
![image](https://github.com/ML-project-3/ML_project/assets/155655348/d1fdd8e0-d8b5-42a8-93dd-4933835cdd78)
<details>
<summary><b> 흥행지표 자세한 내용</b></summary>
  
> **가중치_참고** :  
> **1. 제작 국가**  
>     - 2023년 넷플릭스 시청 시간 보고서 참고      
>     - 상위 1000개 드라마의 제작 국가를 조사 -> 국가 별 비율을 계산    
> **2. 연령 등급**  
>     - 2023년 넷플릭스 시청 보고서를 참조 : 상위 100개 드라마의 연령 등급과 재생 시간을 조사  
> **3. 장르**  
>     - 2023년 넷플릭스 시청 보고서를 참조
> 
> 참고 사이트: FlixPatrol, 'Preferences on Netflix in Q2 2024', 2024.06.24.  https://flixpatrol.com/preferences/netflix/overall/all/2024-2/
> 
> ---
> **계산식** :![흥행 지표](https://github.com/ML-project-3/ML_project/assets/155655348/71127273-f307-4ac5-84ce-5fec6a5a900d)
  
</details>

## 머신러닝
- 최초 / 최종 모델 성과지표 비교 (가독성을 위해 최초, 최종 모델만 비교)
  - 최초: raw 버전
  - 최종: 평점, 평점 인원 수, 유지도, 장르 다양성에 log 변환 

![first   final score](https://github.com/ML-project-3/ML_project/assets/168641346/8172b78a-be47-4896-bfe8-5638b2fc6a06)  

![image (4)](https://github.com/ML-project-3/ML_project/assets/80812507/eff76eaf-84a9-4d47-8e67-363a9b90cd63)


- 흥행 등급:  
    ![ML_Netflix project 평일오후3조 final (2)](https://github.com/ML-project-3/ML_project/assets/80812507/6d012b4f-b122-4f08-a19a-8cb5e12c4022)
    
- **대흥행**: 상위 5%에 해당하는 드라마로, 전체 드라마 중에서 가장 높은 흥행 성적을 기록한 드라마들  
  **흥행**: 상위 6-30%에 해당하는 드라마로, 전체 드라마 중에서 비교적 높은 흥행 성적을 기록한 드라마들  
  **호불호**: 전체 31-70%에 해당하는 드라마로, 대중에게 호불호가 갈리는 드라마들  
  **부진**: 전체 71-100%에 해당하는 드라마로, 흥행 성적이 저조한 드라마들  


## 추가 분석
- 추가 파생변수 season_gaps

![season_gaps score](https://github.com/ML-project-3/ML_project/assets/168641346/ea5eaee2-341d-479d-bbc1-424e8db2e667)


- 오징어 게임 2 예측

![squid_game_season_2 score](https://github.com/ML-project-3/ML_project/assets/168641346/28f748d6-88c1-401a-ac87-3eefbcb65db2)

## 비지니스 효과
1. OTT 흥행 지표 제시 → 의사결정 보조 지표로 활용
2. 콘텐츠 투자의 리스크 헷징
3. 마케팅 비용 최적화
4. 신규 구독자 확보와 기존 고객 리텐션 유지

  
## 🔥이슈 및 트러블슈팅

<details>
<summary><b>➡️ 01. IMDb 서양권 편중 문제</b></summary>
  
> **설명** : IMDb는 미국 유저가 30% 이상을 차지하고, 그 다음으로 영국, 캐나다 유저가 많은 특성을 가지고 있음. 때문에 글로벌 평판은 반영 가능하지만, 동양권 드라마에 대한 관심이 덜한 한계가 존재.
>
> **해결** :  한, 중, 일 드라마에 대한 선호가 강한 Watcha를 추가적으로 크롤링하여 동양권 드라마에 대한 평판을 보완하고자 함.
</details>

<details>
<summary><b>➡️ 02. 구글 API 횟수 제한 문제</b></summary>
  
> **설명** : 구글 api를 통한 크롤링 시 검색이 500회로 제한되는 문제
>
> **해결** : 셀레니움을 이용해 구글에 직접 검색하는 방식으로 변경. 빠르고 잦은 검색 시 일어나는 reCAPTCHA를 회피하기 위해 랜덤으로 sleep을 실행
</details>

<details>
<summary><b>➡️ 03. log 변환 문제</b></summary>

> **설명** : 수집한 데이터는 드라마 간 평점과 인기의 불균형이 존재하며, 몇 컬럼들의 데이터 분포도가 정규성를 띄지 않고 편차가 큰 값들이 존재.
>
> **해결** : 편차가 큰 값들은 이상치일 수 있지만 데이터를 삭제하기 보다는 하나의 대중의 의견이라 판단함. 이를 존중하기 위해 이상치 제거는 하지 않음. 그대신 이상치를 띄는 컬럼은 오른쪽으로 긴 꼬리를 가진 분포를 나타내므로, numpy의 로그 변환을 통해 분포가 균일해진 정규 분포에 가깝게 만듬
  
</details>

<details>
<summary><b>➡️ 04. 흥행지표의 객관성 유지</b></summary>

> **설명** : y값 생성시, 이 지표가 시청률과 같은 정량적인 값이 아닌 저희 판단으로 만든 점성적인 값이기에 흥행을 나타내는 것인 맞을까하는 의문과 객관성을 잃지 않을지 우려
>
> **해결** : 수집한 모든 컬럼들을 '드라마의 특징, 시즌과 상관없이 드라마 전체의 인기도, 각 시즌의 인기도'로 총 3 part로 분류함. 그 후 y값 생성시 오직 '각 시즌의 인기도'의 컬럼들로만 이루어진 계산식으로 흥행의 여부를 판단. 또한 흥행지표의 객관성을 유지하기 위해 도메인 공부를 통해 얻은 것으로 각 가중치를 부여함

<details>
<summary><b>➡️ 05. 시즌간 Term을 활용한 시계열 데이터의 적용 문제</b></summary>

> **설명** : 시즌간 Term이라는 시계열 데이터를 X값에 넣어 분석을 수행하였으나, 이를 사용할 경우 다음 시즌의 term이 미정인 시즌1(현재 단일 드라마로 분류된)를 예측할 수 없는 문제 발생
>
> **해결** : 사이드 프로젝트로 시계열 데이터를 포함하여 새로운 머신러닝 모델 버전를 생성한 후, 다음 시즌의 방영일자가 확실시 된 시즌 1의 작품의 흥행을 예측할 수 있게 함(예로들어: '오징어 게임2' 새 시즌 방영일자가 확실하기에 사이드 프로젝트도 수행하여 더욱 정확한 흥행을 확인할 수 있음)
</details>




