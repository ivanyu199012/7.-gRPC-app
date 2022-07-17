# Examples of First glimpse into gRPC through Python

## Blog Posts
- [First glimpse into gRPC through Python (Part 1)](
https://ivanyu2021.hashnode.dev/first-glimpse-into-grpc-through-python-part-1)
- [First glimpse into gRPC through Python (Part 2)](https://ivanyu2021.hashnode.dev/first-glimpse-into-grpc-through-python-part-2)

## Requirements
- Python 3.9.10
- Virtualenv 20.13.1

## Setup
```
git clone https://github.com/ivanyu199012/7.-gRPC-app
cd 7.-gRPC-app

virtualenv sampleGrpcProjEnv
sampleGrpcProjEnv\Scripts\activate

pip install -r requirements.txt
cd SampleGrpcProj
```

## Generate protoco
- Run VS Code Task "Generate Sample protoco" Or
- Run the below command in the terminal
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./sample_service.proto
```

## Run Server
- Run VS Code Task "Start SampleService Dev" Or
- Run the below command in the terminal
```
python sample_service_test.py
```

## Run Client
- Run VS Code Task "Start SampleService Client" Or
- Run the below command in the terminal
```
python sample_service_client.py"
```

## Test
- Run VS Code Task "Test SampleService Dev" Or
- Run the below command in the terminal
```
python sample_service_client.py"
```