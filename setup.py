import setuptools

setuptools.setup(
	name = 'indicparser',
	version = '0.0.8',
	url = 'https://github.com/Saurabhbaghel/indicparser',
	packages = setuptools.find_packages(),
	package_data = {
		'configs':[
			'*.yaml'],
		'test_img':['*.jpg'],
		'test_pdf':['*.pdf']
		},
	install_requires = [
		'numpy',
		'opencv-python',
		'torch==1.5', 
		'torchvision==0.6',
		'-f https://download.pytorch.org/whl/cu101/torch_stable.html',
		'pyyaml==5.4',
		'detectron2==0.1.3',
		'-f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.5/index.html',
		'pytesseract',
		'pdf2image',
		'pdfreader',
		'layoutparser[ocr]'
		],
	
			
		
		
		