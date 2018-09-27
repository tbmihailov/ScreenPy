
#!/usr/bin/env bash

pip install -r requirements.txt


mkdir resources
cd resources
wget https://github.com/explosion/sense2vec/releases/download/v1.0.0a0/reddit_vectors-1.1.0.tar.gz
tar -xzf reddit_vectors-1.1.0.tar.gz

