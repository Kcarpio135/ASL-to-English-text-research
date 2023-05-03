# ASL-to-English-text-translation

Add videos folder to data!
'data/videos' <-- what you expect

Run requirements.txt
Run download.py to download video data

Preprocess Videos through:
'python3 DataPreprocessing/CS230_DataProcessing.py'

Crop Videos (Reccomend skip: Will run for many hours):
'python3 DataPreprocessing/crop_videos.py'

Split Videos:
'python3 DataPreprocessing/split_videos.py'

Keras Error in Train:
'python3 msasl_i3d_train_100.py'

Hand demo:
'python3 /hands/handReaderDemo.py'

Evaluate model:

'python3 pretrained_i3d.py'
