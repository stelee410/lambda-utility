python3 -m pip install --upgrade pip
pip install -r https://raw.githubusercontent.com/stelee410/lambda-utility/main/requirements.txt
pip install protobuf==3.20.*
cp /home/ubuntu/.local/lib/python3.8/site-packages/bitsandbytes/libbitsandbytes_cuda117.so /home/ubuntu/.local/lib/python3.8/site-packages/bitsandbytes/libbitsandbytes_cpu.so
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs