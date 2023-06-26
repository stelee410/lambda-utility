storage_path="~/storage001"
venv_name="space-llama"
venv_path="$storage_path/$venv_name"

echo "To initial the workspace"
if [ ! -d "$venv_path" ]; then
  mkdir -p "$venv_path" 
  cd $storage_path
  python3 -m venv $venv_name
fi
source $venv_name/bin/activate
cd $storage_path

echo "To prepare python packages"
if [ ! -d "$storage_path/lambda-utility" ]; then
    git clone https://github.com/stelee410/lambda-utility.git
fi
cd lambda-utility
git pull
pip install -r requirements.txt
#fix minor issue of bitsandbytes
cp /home/ubuntu/.local/lib/python3.8/site-packages/bitsandbytes/libbitsandbytes_cuda117.so /home/ubuntu/.local/lib/python3.8/site-packages/bitsandbytes/libbitsandbytes_cpu.so

#echo "To install the git lfs"
#curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
#sudo apt-get install git-lfs