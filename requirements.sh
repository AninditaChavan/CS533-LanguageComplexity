conda install torch==1.1.0
conda install cython==0.29.13 
conda install numpy==1.17.2
sudo apt-get install libhdf5-serial-dev=1.8.16+docs-4ubuntu1.1
conda install benepar[gpu]==0.1.2 --ignore-installed
conda install pytorch_pretrained_bert==0.6.2
conda install sentencepiece==0.1.83
conda install tensorflow==2.0.0
conda install tensorboard==2.0.0
conda install nltk==3.5
python -m nltk.downloader punkt averaged_perceptron_tagger
conda install git+https://github.com/lanpa/tensorboardX
conda install transformers==2.8.0
conda install tqdm==4.45.0

# Download pre-trained model
# conda install gdown
# gdown https://drive.google.com/uc?id=1LC5iVcvgksQhNVJ-CbMigqXnPAaquiA2

# # If you get a "Too many users have viewed or downloaded this file recently." error, 
# run the following 3 lines to download pre-trained model from a mirror:
# conda install internetarchive
# ia download neuraladobe-ucsdparser
# mv neuraladobe-ucsdparser/best_parser.pt .
