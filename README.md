# CamVid
CamVid original data set, and the generated 11 category labels and training grayscale images.



# Folder structure

```
.
├── CamVidColor11 # 11 classes color label
├── CamVidGray # 11 classes gray label, 0~10 for classes, 255 for ignored pixeles
├── CamVid_Label # Original CamVid color label
└── CamVid_RGB # Original CamVid rgb image
```

The original CamVid dataset image resolution is `960x720`. Other segmentation methods downsample it to `480x360`. I provide a higher resolution version.



# Group 32 classes to 11 classes

Refer [CamvidPixelLabelIDs.m](https://github.com/jijnasa/Fully-Convolutional-Neural-Network/blob/master/camvidPixelLabelIDs.m)

The map function is list as follows:

```python
RGBLabel2LabelName = {
    (128, 128, 128): "Sky",

    (0, 128, 64): "Building",
    (128, 0, 0): "Building",
    (64, 192, 0): "Building",
    (64, 0, 64): "Building",
    (192, 0, 128): "Building",

    (192, 192, 128): "Pole",
    (0, 0, 64): "Pole",

    (128, 64, 128): "Road",
    (128, 0, 192): "Road",
    (192, 0, 64): "Road",

    (0, 0, 192): "Sidewalk",
    (64, 192, 128): "Sidewalk",
    (128, 128, 192): "Sidewalk",

    (128, 128, 0): "Tree",
    (192, 192, 0): "Tree",

    (192, 128, 128): "SignSymbol",
    (128, 128, 64): "SignSymbol",
    (0, 64, 64): "SignSymbol",

    (64, 64, 128): "Fence",

    (64, 0, 128): "Car",
    (64, 128, 192): "Car",
    (192, 128, 192): "Car",
    (192, 64, 128): "Car",
    (128, 64, 64): "Car",

    (64, 64, 0): "Pedestrian",
    (192, 128, 64): "Pedestrian",
    (64, 0, 192): "Pedestrian",
    (64, 128, 64): "Pedestrian",

    (0, 128, 192): "Bicyclist",
    (192, 0, 192): "Bicyclist",

    (0, 0, 0): "Void"
}
```





# Labeling errors in CamVid

There is a problem with `Seq05VD_f02610_L.png` annotation. For pixels rgb value that do not appear in the annotation category,  we set it as `Void`.

There are detailds:

```
(2, 311) in (26, 26, 26), rgb Seq05VD_f02610_L.png, changed to Void
(2, 312) in (26, 26, 26), rgb Seq05VD_f02610_L.png, changed to Void
(2, 314) in (36, 36, 36), rgb Seq05VD_f02610_L.png, changed to Void
(2, 315) in (51, 51, 51), rgb Seq05VD_f02610_L.png, changed to Void
(2, 323) in (77, 77, 77), rgb Seq05VD_f02610_L.png, changed to Void
(2, 325) in (77, 77, 77), rgb Seq05VD_f02610_L.png, changed to Void
(2, 326) in (77, 77, 77), rgb Seq05VD_f02610_L.png, changed to Void
(2, 333) in (128, 128, 77), rgb Seq05VD_f02610_L.png, changed to Void
(2, 334) in (128, 128, 86), rgb Seq05VD_f02610_L.png, changed to Void
(2, 335) in (128, 128, 102), rgb Seq05VD_f02610_L.png, changed to Void
(2, 336) in (128, 128, 102), rgb Seq05VD_f02610_L.png, changed to Void
(2, 337) in (128, 128, 102), rgb Seq05VD_f02610_L.png, changed to Void
(2, 338) in (128, 128, 102), rgb Seq05VD_f02610_L.png, changed to Void
(2, 339) in (128, 128, 102), rgb Seq05VD_f02610_L.png, changed to Void
(2, 340) in (128, 128, 102), rgb Seq05VD_f02610_L.png, changed to Void
(2, 341) in (128, 128, 102), rgb Seq05VD_f02610_L.png, changed to Void
(2, 342) in (26, 26, 0), rgb Seq05VD_f02610_L.png, changed to Void
(2, 343) in (26, 26, 0), rgb Seq05VD_f02610_L.png, changed to Void
(2, 344) in (18, 18, 0), rgb Seq05VD_f02610_L.png, changed to Void
(3, 354) in (128, 128, 6), rgb Seq05VD_f02610_L.png, changed to Void
(3, 355) in (128, 128, 26), rgb Seq05VD_f02610_L.png, changed to Void
(3, 356) in (128, 128, 26), rgb Seq05VD_f02610_L.png, changed to Void
(3, 357) in (128, 128, 26), rgb Seq05VD_f02610_L.png, changed to Void
(3, 358) in (128, 128, 26), rgb Seq05VD_f02610_L.png, changed to Void
(3, 359) in (128, 128, 26), rgb Seq05VD_f02610_L.png, changed to Void
(3, 360) in (128, 128, 26), rgb Seq05VD_f02610_L.png, changed to Void
(3, 361) in (128, 128, 26), rgb Seq05VD_f02610_L.png, changed to Void
(3, 362) in (128, 128, 26), rgb Seq05VD_f02610_L.png, changed to Void
(3, 363) in (128, 128, 26), rgb Seq05VD_f02610_L.png, changed to Void
(3, 364) in (128, 128, 30), rgb Seq05VD_f02610_L.png, changed to Void
(3, 365) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(3, 366) in (77, 77, 0), rgb Seq05VD_f02610_L.png, changed to Void
(3, 367) in (77, 77, 0), rgb Seq05VD_f02610_L.png, changed to Void
(3, 368) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(3, 369) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(3, 370) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(3, 371) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(3, 372) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(3, 373) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(3, 374) in (128, 128, 54), rgb Seq05VD_f02610_L.png, changed to Void
(3, 375) in (128, 128, 77), rgb Seq05VD_f02610_L.png, changed to Void
(3, 376) in (128, 128, 77), rgb Seq05VD_f02610_L.png, changed to Void
(3, 377) in (51, 51, 0), rgb Seq05VD_f02610_L.png, changed to Void
(3, 378) in (51, 51, 0), rgb Seq05VD_f02610_L.png, changed to Void
(3, 379) in (51, 51, 0), rgb Seq05VD_f02610_L.png, changed to Void
(3, 380) in (51, 51, 0), rgb Seq05VD_f02610_L.png, changed to Void
(3, 381) in (51, 51, 0), rgb Seq05VD_f02610_L.png, changed to Void
(3, 382) in (51, 51, 0), rgb Seq05VD_f02610_L.png, changed to Void
(3, 383) in (51, 51, 0), rgb Seq05VD_f02610_L.png, changed to Void
(3, 384) in (48, 48, 0), rgb Seq05VD_f02610_L.png, changed to Void
(3, 385) in (26, 26, 0), rgb Seq05VD_f02610_L.png, changed to Void
(3, 386) in (26, 26, 0), rgb Seq05VD_f02610_L.png, changed to Void
(3, 387) in (26, 26, 0), rgb Seq05VD_f02610_L.png, changed to Void
(3, 388) in (26, 26, 0), rgb Seq05VD_f02610_L.png, changed to Void
(3, 389) in (128, 128, 102), rgb Seq05VD_f02610_L.png, changed to Void
(3, 390) in (128, 128, 102), rgb Seq05VD_f02610_L.png, changed to Void
(3, 391) in (128, 128, 102), rgb Seq05VD_f02610_L.png, changed to Void
(3, 392) in (128, 128, 102), rgb Seq05VD_f02610_L.png, changed to Void
(3, 393) in (128, 128, 102), rgb Seq05VD_f02610_L.png, changed to Void
(3, 394) in (128, 128, 104), rgb Seq05VD_f02610_L.png, changed to Void
(4, 405) in (102, 102, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 406) in (102, 102, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 407) in (102, 102, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 408) in (102, 102, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 409) in (102, 102, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 410) in (128, 128, 26), rgb Seq05VD_f02610_L.png, changed to Void
(4, 411) in (128, 128, 26), rgb Seq05VD_f02610_L.png, changed to Void
(4, 412) in (128, 128, 26), rgb Seq05VD_f02610_L.png, changed to Void
(4, 413) in (128, 128, 26), rgb Seq05VD_f02610_L.png, changed to Void
(4, 414) in (128, 128, 26), rgb Seq05VD_f02610_L.png, changed to Void
(4, 415) in (128, 128, 50), rgb Seq05VD_f02610_L.png, changed to Void
(4, 416) in (77, 77, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 417) in (77, 77, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 418) in (77, 77, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 419) in (77, 77, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 420) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(4, 421) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(4, 422) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(4, 423) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(4, 424) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(4, 425) in (128, 128, 75), rgb Seq05VD_f02610_L.png, changed to Void
(4, 426) in (51, 51, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 427) in (51, 51, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 428) in (128, 128, 77), rgb Seq05VD_f02610_L.png, changed to Void
(4, 429) in (128, 128, 77), rgb Seq05VD_f02610_L.png, changed to Void
(4, 430) in (51, 51, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 431) in (51, 51, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 432) in (51, 51, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 433) in (51, 51, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 434) in (51, 51, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 435) in (29, 29, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 436) in (26, 26, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 437) in (26, 26, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 438) in (26, 26, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 439) in (26, 26, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 440) in (26, 26, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 441) in (26, 26, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 442) in (26, 26, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 443) in (26, 26, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 444) in (26, 26, 0), rgb Seq05VD_f02610_L.png, changed to Void
(4, 445) in (5, 5, 0), rgb Seq05VD_f02610_L.png, changed to Void
(51, 305) in (125, 125, 125), rgb Seq05VD_f02610_L.png, changed to Void
(51, 306) in (63, 63, 63), rgb Seq05VD_f02610_L.png, changed to Void
(52, 308) in (110, 110, 110), rgb Seq05VD_f02610_L.png, changed to Void
(52, 309) in (8, 8, 8), rgb Seq05VD_f02610_L.png, changed to Void
(56, 312) in (92, 92, 92), rgb Seq05VD_f02610_L.png, changed to Void
(56, 313) in (2, 2, 2), rgb Seq05VD_f02610_L.png, changed to Void
(57, 313) in (48, 48, 48), rgb Seq05VD_f02610_L.png, changed to Void
(58, 313) in (116, 116, 116), rgb Seq05VD_f02610_L.png, changed to Void
(58, 314) in (48, 48, 48), rgb Seq05VD_f02610_L.png, changed to Void
(58, 315) in (2, 2, 2), rgb Seq05VD_f02610_L.png, changed to Void
(59, 315) in (92, 92, 92), rgb Seq05VD_f02610_L.png, changed to Void
(59, 316) in (2, 2, 2), rgb Seq05VD_f02610_L.png, changed to Void
(60, 316) in (48, 48, 48), rgb Seq05VD_f02610_L.png, changed to Void
(61, 316) in (116, 116, 116), rgb Seq05VD_f02610_L.png, changed to Void
(61, 317) in (15, 15, 15), rgb Seq05VD_f02610_L.png, changed to Void
(62, 317) in (113, 113, 113), rgb Seq05VD_f02610_L.png, changed to Void
(63, 318) in (48, 48, 48), rgb Seq05VD_f02610_L.png, changed to Void
(64, 318) in (2, 2, 2), rgb Seq05VD_f02610_L.png, changed to Void
(64, 319) in (92, 92, 92), rgb Seq05VD_f02610_L.png, changed to Void
(65, 319) in (2, 2, 2), rgb Seq05VD_f02610_L.png, changed to Void
(65, 320) in (50, 50, 0), rgb Seq05VD_f02610_L.png, changed to Void
(65, 321) in (111, 111, 0), rgb Seq05VD_f02610_L.png, changed to Void
(66, 321) in (2, 2, 0), rgb Seq05VD_f02610_L.png, changed to Void
(66, 322) in (50, 50, 50), rgb Seq05VD_f02610_L.png, changed to Void
(67, 323) in (128, 128, 63), rgb Seq05VD_f02610_L.png, changed to Void
(68, 323) in (60, 60, 0), rgb Seq05VD_f02610_L.png, changed to Void
(69, 323) in (60, 60, 0), rgb Seq05VD_f02610_L.png, changed to Void
(70, 323) in (128, 128, 68), rgb Seq05VD_f02610_L.png, changed to Void
(79, 324) in (128, 128, 123), rgb Seq05VD_f02610_L.png, changed to Void
(111, 341) in (128, 128, 3), rgb Seq05VD_f02610_L.png, changed to Void
(112, 341) in (128, 128, 63), rgb Seq05VD_f02610_L.png, changed to Void
(113, 341) in (128, 128, 69), rgb Seq05VD_f02610_L.png, changed to Void
(147, 346) in (128, 128, 92), rgb Seq05VD_f02610_L.png, changed to Void
(147, 347) in (128, 128, 3), rgb Seq05VD_f02610_L.png, changed to Void
(152, 349) in (47, 47, 0), rgb Seq05VD_f02610_L.png, changed to Void
(153, 349) in (2, 2, 0), rgb Seq05VD_f02610_L.png, changed to Void
(153, 350) in (108, 108, 0), rgb Seq05VD_f02610_L.png, changed to Void
(154, 350) in (48, 48, 0), rgb Seq05VD_f02610_L.png, changed to Void
(155, 350) in (2, 2, 0), rgb Seq05VD_f02610_L.png, changed to Void
(155, 351) in (108, 108, 0), rgb Seq05VD_f02610_L.png, changed to Void
(156, 351) in (48, 48, 0), rgb Seq05VD_f02610_L.png, changed to Void
(160, 354) in (128, 128, 126), rgb Seq05VD_f02610_L.png, changed to Void
(161, 355) in (128, 128, 3), rgb Seq05VD_f02610_L.png, changed to Void
(162, 355) in (128, 128, 92), rgb Seq05VD_f02610_L.png, changed to Void
(162, 356) in (128, 128, 3), rgb Seq05VD_f02610_L.png, changed to Void
(163, 356) in (128, 128, 78), rgb Seq05VD_f02610_L.png, changed to Void
(163, 494) in (15, 15, 15), rgb Seq05VD_f02610_L.png, changed to Void
(164, 356) in (128, 128, 126), rgb Seq05VD_f02610_L.png, changed to Void
(164, 357) in (128, 128, 21), rgb Seq05VD_f02610_L.png, changed to Void
(165, 357) in (128, 128, 113), rgb Seq05VD_f02610_L.png, changed to Void
(174, 375) in (171, 171, 86), rgb Seq05VD_f02610_L.png, changed to Void
(174, 376) in (191, 191, 126), rgb Seq05VD_f02610_L.png, changed to Void
(175, 376) in (138, 138, 20), rgb Seq05VD_f02610_L.png, changed to Void
(176, 377) in (136, 136, 15), rgb Seq05VD_f02610_L.png, changed to Void
(177, 380) in (154, 154, 51), rgb Seq05VD_f02610_L.png, changed to Void
(177, 434) in (77, 77, 0), rgb Seq05VD_f02610_L.png, changed to Void
(177, 435) in (77, 77, 0), rgb Seq05VD_f02610_L.png, changed to Void
(177, 436) in (77, 77, 0), rgb Seq05VD_f02610_L.png, changed to Void
(177, 437) in (77, 77, 0), rgb Seq05VD_f02610_L.png, changed to Void
(177, 438) in (77, 77, 0), rgb Seq05VD_f02610_L.png, changed to Void
(177, 439) in (77, 77, 0), rgb Seq05VD_f02610_L.png, changed to Void
(177, 440) in (77, 77, 0), rgb Seq05VD_f02610_L.png, changed to Void
(177, 441) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(177, 442) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(177, 443) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(177, 444) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(177, 446) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(177, 447) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(177, 448) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(177, 449) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(177, 450) in (128, 128, 51), rgb Seq05VD_f02610_L.png, changed to Void
(177, 451) in (77, 77, 0), rgb Seq05VD_f02610_L.png, changed to Void
(177, 452) in (77, 77, 77), rgb Seq05VD_f02610_L.png, changed to Void
(177, 465) in (51, 51, 51), rgb Seq05VD_f02610_L.png, changed to Void
```



# Dataset Division

see `camvid_data.py`  for details.