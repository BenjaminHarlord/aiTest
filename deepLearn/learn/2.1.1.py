import torch

x =torch.arange(12)
print('torch arange x: {x}'.format(x=x))

x_shape = x.shape
print('torch shape x: {x_shape}'.format(x_shape=x_shape))

x_numel = x.numel()
print('torch numel x: {x_numel}'.format(x_numel=x_numel))

x_reshape_0 = x.reshape(1,-1)
print('torch reshape x: {x_reshape_0}'.format(x_reshape_0=x_reshape_0))

x_reshape_1 = x.reshape(3,4)
print('torch reshape x: {x_reshape_1}'.format(x_reshape_1=x_reshape_1))

x_ones = torch.ones((2,4))
print('torch ones x: \n{x_ones}'.format(x_ones=x_ones))

x_zreos = torch.zeros((2,4))
print('torch zeros x: \n{x_zreos}'.format(x_zreos=x_zreos))

x_ones_more = torch.ones((2,3,4))
print('torch ones x: \n{x_ones_more}'.format(x_ones_more=x_ones_more))

x_zeros_more = torch.zeros((2,3,4))
print('torch zeros x: \n{x_zeros_more}'.format(x_zeros_more=x_zeros_more))

# 张量 入门