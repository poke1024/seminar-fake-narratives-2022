import os
import sys


def load_insightface():
	from insightface.app import FaceAnalysis

	app = FaceAnalysis(allowed_modules=['detection'])
	app.prepare(ctx_id=0, det_size=(640, 640))


def load_easyocr():
	import easyocr
	reader = easyocr.Reader(['en'])



def load_detr():
	from transformers import DetrFeatureExtractor, DetrForObjectDetection
	import torch

	feature_extractor = DetrFeatureExtractor.from_pretrained("facebook/detr-resnet-50")
	model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")


def load_roberta():
	from transformers import pipeline
	unmasker = pipeline('fill-mask', model='distilroberta-base')
	extractor = pipeline('feature-extraction', model='roberta-base')



def load(load_fn, name):
	print(f"loading {name}... ", end='', flush=True)
	old_stdout = sys.stdout
	old_stderr = sys.stderr
	try:
		f = open(os.devnull, 'w')
		sys.stdout = f
		sys.stderr = f
		load_fn()
	finally:
		sys.stdout = old_stdout
		sys.stderr = old_stderr
	print("OK", flush=True)


load(load_insightface, "insightface")
load(load_easyocr, "easyocr")
load(load_detr, "DETR")
load(load_roberta, "RoBERTa")
