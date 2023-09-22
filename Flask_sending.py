import requests
import time
start_time = time.time()  # 시작 시간 저장


# 업로드할 이미지 파일 경로
image_file_path = './Pic_2023_08_17_100136_1.jpg'  # 실제 파일 경로로변경해야 합니다.

# 업로드할 URL (메인 컴퓨터의 Flask API 엔드포인트)
upload_url = 'http://202.31.34.153:1111/upload'  # 메인 컴퓨터의 IP 주소로 변경해야 합니다.

# 이미지 업로드
files = {'file': open(image_file_path, 'rb')}
response = requests.post(upload_url, files=files)

# 업로드 결과 확인
if response.status_code == 200:
    print('File uploaded and processed successfully')
else:
    print('Error:', response.json())

end_time = time.time()  # 종료 시간 저장

print(f"코드 실행 시간: {end_time - start_time} 초")