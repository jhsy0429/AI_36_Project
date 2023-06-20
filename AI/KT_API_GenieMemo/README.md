##KT 각종 api 키들

Client ID : 239ea532-a145-45f4-8295-ee4876877fec

Client Key : 0fb26b7f-9b98-53cc-bc0f-eccf6988a793

Client Secret : e35be7455626bde39956632c968b98df6e9d1458942f2c69888400166ca27f4e




##kt ai api 사용하기 앞서서 설치하는 것들

conda install -c conda-forge portaudio python=3 pyaudio grpcio grpcio-tools

그리고 proto 폴더 들어가서

(아나콘다 power shell 들어간 후, cd proto파일 경로 지정)

python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. ktaiapi.proto
