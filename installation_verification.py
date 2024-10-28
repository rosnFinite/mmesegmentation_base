from mmseg.apis import inference_model, init_model, show_result_pyplot
import mmcv

config_file = 'model/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024.py'
checkpoint_file = 'model/pspnet_r50-d8_512x1024_40k_cityscapes_20200605_003338-2966598c.pth'

# build the model from a config file and a checkpoint file
model = init_model(config_file, checkpoint_file, device="cuda:0")

# test a single image and show the results
img = 'demo/inputs/demo.png'  # or img = mmcv.imread(img), which will only load it once
result = inference_model(model, img)
# save the visualization results to image files
# you can change the opacity of the painted segmentation map in (0, 1].
show_result_pyplot(model, img, result, show=False, out_file='demo/results/result.jpg', opacity=0.5)
