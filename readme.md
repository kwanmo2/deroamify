---
title:  "Roam to Logseq"
search: false
categories: 
  - Software
tags:
  - Python
  - NoteTaking
  - Logseq
---
Roam research(이하 Roam으로 표기)는 내가 처음 써본 백링크 노트로 제텔카스텐 관련 책을 읽고 처음으로 써보기 시작한  노트앱이다. 웹 베이스 앱이라는 점은 여러 기기를 쓰는 나에게는 큰 장점이었지만, 가장 큰 단점은 비싼 구독 가격이다. 가격은 상대적인 부분이라 Roam와 비슷한 기능, 혹은 더 많은 기능을 가지고 있는 노트앱들이 무료로 사용할 수 있게 열려있어 사용자에게 Roam 비용은 더 비싸게 느껴질 수 밖에 없다. 그래서 Roam 1년 구독이 끝난 시점에 Logseq로 옮겨오기로 했다. 기존에 Roam으로 작성했던 텍스트 데이터, 백링크를 logseq로 그대로 가져오는게 가능하지만 가장 큰 문제는 첨부파일 및 이미지 첨부다. Roam은 구글 firebase에 데이터를 업로드하고 링크를 걸어서 각 노트에 이미지를 임베딩하는 반면 logseq는 로컬 디렉토리에 이미지 파일을 저장하고 markdown 문법을 이용해서 이미지를 임베딩해야한다.
```markdown
!(이미지 이름)[이미지 파일 위치]
```

그 많은 노트 페이지의 이미지를 다운로드하고, 해당하는 노트에 들어가 링크를 위와 같이 바꿔주는 작업을 수작업으로 하는 것은 거의 불가능에 가까웠다. 찾아보던중 deRoamify(탈 Roam?)을 파이썬 스크립트로 짜놓은 [nicolevanderhoeven의 블로그](https://nicolevanderhoeven.com/blog/20210602-downloading-files-from-roam/)를 찾았다. 

사용해보니 동작하기는 하는데, 사용이 불편하고 인코딩 때문에 한글이 깨진다는 문제가 있어 아주 살짝 수정했다. Roam에서 벗어나고 싶은데 수많은 이미지 첨부파일 때문에 옮기기 꺼려지는 분들은 한 번 사용해보길 바란다. 참고로 윈도우/맥 둘 다 동작한다.

1. 터미널에서 'git clone' 입력하여 해당 파이썬 코드 다운로드

<p align="center">
  <img width="460" height="300" src="assets/2022-08-08_1.png">
</p>


2. Roam에서 Export한 md 폴더들이 있는 위치에 .py 파일 옮기기

<p align="center">
  <img width="460" height="300" src="assets/2022-08-08_2.png">
</p>


3. 터미널에서 'python3 downloadfirebase.py' 입력

<p align="center">
  <img width="460" height="300" src="assets/2022-08-08_3.png">
</p>

4. 생성된 target 폴더 안에 들어가보면, 이미지가 첨부 있었던 페이지들이 따로 나와있고 


<p align="center">
  <img width="460" height="300" src="assets/2022-08-08_7.png">
</p>

5. 노트에는 이미지 링크가 수정되어 있고, assets 폴더에는 firebase 이미지들이 png 확장자로 저장


<p align="center">
  <img width="460" height="300" src="assets/2022-08-08_8.png">
</p>

<p align="center">
  <img width="460" height="300" src="assets/2022-08-08_9.png">
</p>
