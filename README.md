# it-hufs-2020-2
2020년 한국외대 IT 교육(블록체인 X 인공지능) : 4조 Ladybug🐞
## Introduction
### 주제: 병해충 AI 자가판톡 및 처방 플랫폼, 병해충알리미(Pest-X)
* [발표 ppt]()

### 팀 구성

|성명|담당업무|
|:--:|:--|
|김경남| - 웹 개발 <br> - Image crawler 및 국가농작물병해충관리시스템 crawler 제작 <br> - 분석기술 조사 및 정리|
|박수연| - 기획 및 운영 <br> - ppt 제작 <br> - 발표|
|이민정| - 시장 조사 <br> - ppt 제작 <br> - 발표|
|이화정| - 아이템 조사 <br> - ppt 제작|
|이혜은| - 사업성 검토 <br> - ppt 제작|

### 프로젝트 개발환경 및 언어
* Ubuntu 18.04 LTS 또는 Windows10
* Front-end: HTML, CSS, Javascript
* Data crawling + parsing: python 3.6 이상

## Getting Started
```
git clone --recursive https://github.com/kimkyeongnam/it-hufs-2020-2
cd it-hufs-2020-2

# 1. running html file
(click index.html)

# 2. running Image-Crawling
(check Image-Crawler's README)
```

## File Structure
```
.
|-- index.html
|-- images
|   |-- upload.svg
|   |-- pestx.PNG
|   `-- ladybug_logo.PNG
|-- if-hufs-2020-2
|   |-- preprocessign.py
|   |-- data
|   |   |-- pests.txt
|   |   |-- pest_list.json
|   |   |-- final.json
|   |   `-- crops.txt
|   `-- crwaling.py
|-- favicon.ico
|-- assets
|   |-- js
|   |   |-- util.js
|   |   |-- skel.min.js
|   |   |-- main.js
|   |   |-- jquery.scrollex.min.js
|   |   |-- jquery.min.js
|   |   `-- index.js
|   |-- fonts
|   |   |-- fontawesome-webfont.woff2
|   |   |-- fontawesome-webfont.woff
|   |   |-- fontawesome-webfont.ttf
|   |   |-- fontawesome-webfont.svg
|   |   |-- fontawesome-webfont.eot
|   |   `-- FontAwesome.otf
|   |-- css
|   |   |-- main.css
|   |   |-- index.css
|   |   `-- font-awesome.min.css
|   `-- LICENSE.txt
|-- README.md
`-- Image-Crawler  # submodule
    |-- requirements.txt
    |-- main.py
    |-- keywords.txt
    |-- collect_links.py
    |-- chromedriver
    |   |-- chromedriver_win32.zip
    |   |-- chromedriver_mac64.zip
    |   `-- chromedriver_linux64.zip
    `-- README.md

9 directories, 36 files
```
