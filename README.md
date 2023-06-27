# Khuda_Project_StyleGAN2
StyleGAN2를 이용한 게임 속 축구 선수 얼굴 이미지 생성 프로젝트입니다. <br>

---
## 논문 리뷰
"Analyzing and Improving the Image Quality of StyleGAN" 논문 리뷰를 진행했다.<br>
StyleGAN2의 전체적인 모델 구조 및 기존 StyleGAN과의 차별점 등을 알아보았다.
![StyleGAN2](https://github.com/eu2525/Khuda_Project_StyleGAN2/assets/49024115/ca3461bd-850a-47ec-a194-3d3abfc83ffd)


---
## 프로젝트 진행
### 데이터셋
- 데이터 셋으로는 인스타그램 _refifa, downtospawn 님의 게시물 이미지를 크롤링해 수집했습니다.
<img src="https://github.com/eu2525/Khuda_Project_StyleGAN2/assets/49024115/9ccb8872-3478-4ef8-9ef7-fbf9ef7731f8" width="40%"> <img src="https://github.com/eu2525/Khuda_Project_StyleGAN2/assets/49024115/4f82636a-0bfd-436c-a414-2bbb62f3b148" width="40%"> <br>
- 게시물 이미지를 Haar-based Cascade를 이용해 Face Detection을 진행 <br>
- 정사각형 형태로 얼굴 이미지 분리 후 1024*1024 크기로 resize. 
---
### 모델 학습
#### 전이학습
- FFHQ를 통해 Pretrained된 StyleGAN2 모델에 Freeze-D를 적용해 전이학습을 진행. <br>
- Freeze-D : Custom한 데이터셋  혹은 다른 도메인의 데이터셋으로 학습할 때 Discriminator의 특정 layer를 freezing 시켜 학습 시키는 방법<br>
![황희찬](https://github.com/eu2525/Khuda_Project_StyleGAN2/assets/49024115/828b811d-a213-4114-b092-20847236ba04)
#### Layer Swapping
- 서로 다른 모델의 구조를 섞는 기법
- 앞의 4개의 Layer는 FFHQ로 학습된 기존 모델 + 뒤의 5개의 Layer는 축구 선수 이미지로 전이학습한 모델.
![image](https://github.com/eu2525/Khuda_Project_StyleGAN2/assets/49024115/eb82578a-cec5-4b45-a35a-89711ede42c0)




