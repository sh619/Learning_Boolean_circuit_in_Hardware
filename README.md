# Learning_Boolean_circuit_in_Hardware

Reverse Derivative Ascent is a technique proposed by researchers from UCL to 'learn' Boolean circuits[1]. Potentially, this opens the door to both learning highly efficient ML inference accelerators implemented in hardware and also to undertaking the training directly in a custom-built hardware accelerator. This is in contrast to traditional techniques for learning so-called binarized neural networks where a full-precision network is quantised to a (very) low precision fixed-point implementation and then re-trained to address the resulting loss in accuracy. This project aims to build a custom hardware accelerator (and, potentially a custom hardware accelerator generator) capable of implementing these algorithms on FPGAs. 

[1]https://arxiv.org/abs/2101.10488
