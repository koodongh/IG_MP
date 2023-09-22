from flask import Flask, request, jsonify
from ultralytics import YOLO
import os
import shutil
import cv2

tire_model = YOLO('./custom_weight/best.pt')
ig_model = YOLO('./custom_weight/best_ig.pt')

app = Flask(__name__)

# 이미지를 저장할 디렉토리 설정
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:

        # 업로드된 이미지를 저장
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))

        # process.py 파일 실행 (이미지 처리)
        image_path = os.path.join(UPLOAD_FOLDER, file.filename)
        
        # if os.path.exists('./uploads/predict'):
        #     shutil.rmtree('./uploads/predict')
        # print('!!!!!!!!!check!!!!!!!!!!')
        # print(image_path)
        # tire_model.predict(source='./'+image_path, project = './uploads/predict', save_crop = True, conf = 0.7)
               
        # # 이미지 읽기
        # print('./uploads/predict/crops/Tire/' + file.filename)
        # image = cv2.imread('./uploads/predict/predict/crops/Tire/' + file.filename)
        # # 비율로 이미지 크기를 조절합니다.
        # scale_percent = 60  # 50%로 줄이고 싶은 경우
        # width = int(image.shape[1] * scale_percent / 100)
        # height = int(image.shape[0] * scale_percent / 100)

        # # 이미지 크기를 조절합니다.
        # image = cv2.resize(image, (width, height))

        # # 이미지 크기 및 채널 정보 추출
        # height, width, channels = image.shape

        # # 이미지 4개로 분할
        # crop_img1 = image[0:height//2, 0:width//2]
        # crop_img2 = image[0:height//2, width//2:width]
        # crop_img3 = image[height//2:height, 0:width//2]
        # crop_img4 = image[height//2:height, width//2:width]

        # CROPS_FOLDER = './uploads/crops/'
        # if not os.path.exists(CROPS_FOLDER):
        #     os.makedirs(CROPS_FOLDER)
        
        # # 이미지 저장
        # cv2.imwrite(os.path.join(CROPS_FOLDER, "crop_img1_" + file.filename), crop_img1)
        # cv2.imwrite(os.path.join(CROPS_FOLDER, "crop_img2_" + file.filename), crop_img2)
        # cv2.imwrite(os.path.join(CROPS_FOLDER, "crop_img3_" + file.filename), crop_img3)
        # cv2.imwrite(os.path.join(CROPS_FOLDER, "crop_img4_" + file.filename), crop_img4)
        
        
        # ig_model.predict(source='./uploads/crops', project = './uploads/predict', save = True, conf = 0.7)
        #os.system(f'python process.py {image_path}')

        return jsonify({'message': 'File uploaded and processed successfully'}), 200

if __name__ == '__main__':
    app.run(host='202.31.34.153', port=1111)



