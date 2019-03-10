

setup:
	git clone https://github.com/GantMan/nsfw_model.git
	cd nsfw_model
	python ./setup.py install --user
	pip install --user Pillow
	trizen -S tensorflow python-tensorflow
	wget 'https://s3.amazonaws.com/nsfwdetector/nsfw.299x299.h5'
