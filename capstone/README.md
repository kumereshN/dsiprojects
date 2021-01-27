# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Capstone: Topic modeling on AMD and Nvidia's GPU release

### N Kumeresh, DSI-18-Singapore

## Problem Statement

As a data scientist working in Intel, Intel is looking forward to releasing their first GPU into the market. Based on our research, the fanbase primarily resides in their own respective subreddit, r/AMD and r/Nvidia. We want to analyze the reddit comments in Nvidia and AMD's subreddit, revolving around the release of the new GPU. In order to do this, we'll be conducting topic modeling on the comments and it'll provide us a high level view of what consumers are expecting from the release of these new gpus and ensure a smooth release of our GPUs into the market. The main metric will be in **interpreting the topics** and the secondary metric will be the **topic coherence scores**.

## Executive Summary

Intel is working to release their first discrete Graphic Processing Unit (GPU)(s) into the market this year. The GPU will feature all the horsepower from modern gaming oriented GPU such as ray tracing and tons of horsepower for up to 4k enthusiast tier performance. It'll be competing against AMD RDNA 2 and Nvidia's Ampere lineup. To ensure that the GPU market is primed to receive Intel's first GPU, we would want to further understand in depth on what the market is looking out for when AMD and Nvidia's release their respective GPU and as we expect a similar reaction when we release our GPU.

## Conclusion and recommendation

## Limitations
* As it's is a unsupervised type of model, it requires a lot of high quality data for interpretable topics to be formed

* It's not as accurate as topic classification models
* Not able to gain meaningful insights on the consumer behaviours.

### Summary of findings
The launch around AMD and Nvidia's GPUs have provided interesting highlights in what consumers are looking out for when purchasing GPUs. The below summarizes the findings: 

Note: The sentences highlighted in bold are present commonly in both subreddits.

AMD
* **LDA's mallet coherence score is slightly higher compared to LDA's coherence score and the topics are more interpretable as well.**
* Stock availability is the most assigned topic to the documents with over 2500 documents. Consumers are concerned with the availability to purchase the GPUs.
* Consumer making a purchase is the least assigned topic, which suggests that consumers are have high purchasing power.
* **4k resolution has a higher topic weight compared 1440p resolution which suggests that these GPUs are targeted towards the enthusiast crowd.**
* **Nvidia's RTX 3070 and 3080 seems to be the most popular models, given their high word count and topic weightage.**
* Ray tracing and dlss (Deep learning super sampling) are coveted features among consumers.


Nvidia
* **LDA's mallet coherence is slightly higher compared to LDA's coherence score and I find the topics to be more interpretable.**
* Discussion on GPU models seem to be the most discussed with over 4000 documents. It seems that the consumers desire to upgrade their current GPU.
* **3080 is the most popular GPU given the high word count and the topic weightage, followed by the 3090**
* **4k resolution is the most talked about compared to 1440p resolution given it's high word count and the topic weightage.**
* The amount of vram in a gpu also plays a crucial role as the larger resolution, the more video ram being consumed.

---

### Datasets

* amd_gpu.csv
* cleaned_combined_df.csv
* combined_df.csv
* radeon_rx_6000.csv
* rtx_3000.csv
* rtx_3060ti.csv
* rtx_3070.csv
* rtx_3080.csv
* rtx_3080_3090_leak.csv
* rtx_3080ti_priced.csv
* rtx_3090.csv
* rtx_3090_memory.csv
* rtx_3090vs3080vs3070.csv
* rx_6000_nov_18.csv
* rx_6000_rdna2.csv
* scalper_warning.csv

---
## Data Dictionary

| Feature         | Datatype | Description                                               |
|-----------------|----------|-----------------------------------------------------------|
| Reddit comments | string   | Reddit comments scrapped from their respective subreddits |
| tag             | string   | tags are either Nvidia or Amd                             |