# Can Your Wearable Accurately Track Sleep?

Wearable sleep tracking is useful only when the metric is narrowed to what the sensor can actually support. Across validation studies, consumer devices perform best for sleep-wake detection, worse for quiet wakefulness, and worst for detailed sleep staging; current recommendations also distinguish fundamental sleep measures from proprietary or exploratory outputs. The evidence supports device-derived sleep duration and sleep timing trends. It does not support exporting sleep stages, sleep efficiency, wake after sleep onset, sleep quality scores, or recovery scores as if they were ground truth. ([Chinoy et al., 2021](https://academic.oup.com/sleep/article/44/5/zsaa291/6055610); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472); [Chee et al., 2025](https://www.sciencedirect.com/science/article/abs/pii/S138994572500173X))

The gap is simple: broad labels such as “sleep quality,” “recovery,” and “restorative sleep” imply more certainty than the validation literature supports. The validated signal is much narrower: a device-derived estimate of when sleep probably occurred, and how that pattern changes over time. ([Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472); [Chee et al., 2025](https://www.sciencedirect.com/science/article/abs/pii/S138994572500173X))

## What wearables are actually measuring

Polysomnography (PSG) is the reference standard for sleep measurement because it records brain activity, eye movements, muscle tone, respiratory measures, audio, and video, allowing trained scorers to classify sleep and wake in detail. Consumer wearables do not measure sleep stages directly. They infer sleep and sleep stages from indirect signals such as movement, photoplethysmography-derived heart rate, heart-rate variability, and proprietary algorithms. ([Schyvens et al., 2024](https://mhealth.jmir.org/2024/1/e52192); [Lee et al., 2023](https://mhealth.jmir.org/2023/1/e50983/); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472))

That distinction matters most for sleep staging. Deep sleep and REM sleep are PSG-scored states based primarily on brain, eye, muscle, and phasic physiological signals. A wrist or ring sensor can detect correlates of sleep stages, but it cannot directly measure the EEG features that define those stages. ([Chinoy et al., 2022](https://www.dovepress.com/performance-of-four-commercial-wearable-sleep-tracking-devices-tested--peer-reviewed-fulltext-article-NSS))

## Sleep detection is the strongest metric

Across independent PSG validation studies, modern consumer sleep trackers are generally good at detecting sleep. In a 2021 PSG study of seven consumer sleep-tracking devices, epoch-by-epoch sleep sensitivity was high across all devices, at least 0.93. ([Chinoy et al., 2021](https://academic.oup.com/sleep/article/44/5/zsaa291/6055610))

A 2025 independent PSG study of six wrist-worn devices - Fitbit Charge 5, Fitbit Sense, Withings Scanwatch, Garmin Vivosmart 4, WHOOP 4.0, and Apple Watch Series 8 - found that all devices detected more than 90 percent of sleep epochs. ([Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472))

A 2022 unrestricted home study using mobile EEG as the reference found the same direction: devices performed better for sleep-wake outcomes than for sleep stages, and sleep-wake performance was best on nights with more consolidated sleep. ([Chinoy et al., 2022](https://www.dovepress.com/performance-of-four-commercial-wearable-sleep-tracking-devices-tested--peer-reviewed-fulltext-article-NSS))

This is why the safest exportable metric is not a single absolute ground-truth number. It is a device-derived sleep duration trend, interpreted across nights and within the same device ecosystem. ([Chinoy et al., 2021](https://academic.oup.com/sleep/article/44/5/zsaa291/6055610); [Chinoy et al., 2022](https://www.dovepress.com/performance-of-four-commercial-wearable-sleep-tracking-devices-tested--peer-reviewed-fulltext-article-NSS); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472))

## Wake detection is the failure mode

Wearables are much worse at detecting wakefulness when the person is lying still. In the 2021 PSG study, wake specificity ranged from 0.18 to 0.54, meaning devices frequently missed wake epochs. ([Chinoy et al., 2021](https://academic.oup.com/sleep/article/44/5/zsaa291/6055610))

The 2025 independent PSG study found the same pattern: wake specificity ranged from 29.39 percent to 52.15 percent, and wake epochs were commonly misclassified as light sleep. The authors also found that devices significantly underestimated wake and wake after sleep onset, with wake underestimation ranging from about 12 to 40 minutes and WASO underestimation ranging from about 12 to 48 minutes. ([Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472))

This creates a directional bias. If a person lies awake in bed, the device often scores that time as sleep. That makes total sleep time look better, sleep efficiency look higher, and nighttime awakenings look smaller than they were. A 2023 multicenter validation study similarly found that wearables generally overestimated sleep by misclassifying wake stages, producing bias in sleep efficiency estimates. ([Lee et al., 2023](https://mhealth.jmir.org/2023/1/e50983/))

## Total sleep time is not clean enough as an absolute value

Total sleep time is the best-performing nightly sleep summary metric, but it still fails the export test as an absolute ground-truth number. Some studies show acceptable average performance in healthy adults: in a 2024 Oura-funded PSG study of Oura Ring Gen3, Fitbit Sense 2, and Apple Watch Series 8, nightly total sleep estimates were within about 10 minutes of PSG on average. ([Robbins et al., 2024](https://www.mdpi.com/1424-8220/24/20/6532))

Average performance is not the same as individual reliability. The same study noted that individual nightly estimates may diverge more widely, and it was conducted in healthy adults aged 20 to 50 under controlled conditions. ([Robbins et al., 2024](https://www.mdpi.com/1424-8220/24/20/6532))

A 2026 PSG study directly tested young versus older adults and found that in older adults, devices underestimated total sleep time by large margins: Fitbit Sense 2 by 74.5 minutes, Oura Ring by 75.5 minutes, Withings Sleep Mat by 45.7 minutes, and SleepScore Max by 56.5 minutes. The same study found wider limits of agreement in older adults and poorer performance for sleep stages, especially deep sleep. ([Searles et al., 2026](https://academic.oup.com/sleepadvances/article/7/1/zpag006/8422777))

For AI export, this means `total_sleep_time_minutes` is too strong. It implies a direct, reliable measurement. The safer included metric is `sleep_duration_trend_device_derived`.

## Sleep stages should be excluded

Sleep staging is where wearable accuracy degrades most. In the 2021 PSG study, sleep stage comparisons were mixed, and device performance was worse on nights with poorer or more disrupted sleep. ([Chinoy et al., 2021](https://academic.oup.com/sleep/article/44/5/zsaa291/6055610))

A 2024 systematic review of Fitbit Charge 4, Garmin Vivosmart 4, and WHOOP found moderate accuracy for some sleep parameters, but still concluded that all devices can benefit from improvement in specific sleep-stage assessment. The same review reported high sensitivity to sleep but lower specificity for wake, and noted that companies usually do not share the methodology used to score wearable sleep data. ([Schyvens et al., 2024](https://mhealth.jmir.org/2024/1/e52192))

In the 2025 independent PSG study, Cohen’s kappa values across six wrist-worn devices ranged from 0.21 to 0.53, indicating only fair-to-moderate agreement with PSG for multistate categorization. The same study reported substantial deep-sleep and REM errors, including frequent misclassification of deep sleep or REM as light sleep across multiple devices. ([Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472))

A 2023 multicenter PSG study of 11 consumer sleep technologies found broad variation across devices, with macro F1 scores ranging from 0.26 to 0.69 and only slight, fair, or moderate kappa values depending on the device. ([Lee et al., 2023](https://mhealth.jmir.org/2023/1/e50983/))

The output “32 minutes of deep sleep” is therefore false precision. The device may be detecting a physiological pattern correlated with deep sleep, but the exported number is not reliable enough to be treated as sleep architecture. ([Robbins et al., 2024](https://www.mdpi.com/1424-8220/24/20/6532); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472); [Searles et al., 2026](https://academic.oup.com/sleepadvances/article/7/1/zpag006/8422777))

## Ring versus wrist does not solve the problem

Rings can be convenient for overnight physiology, but form factor does not rescue invalid metrics. The 2024 Oura-funded PSG study reported stronger Oura performance than Fitbit or Apple for some stage metrics, but it also found poor concordance for deep sleep and REM sleep across devices, with ICCs ranging from 0.13 to 0.36 for deep sleep and 0.13 to 0.37 for REM sleep. ([Robbins et al., 2024](https://www.mdpi.com/1424-8220/24/20/6532))

Independent and broader-population studies show why the form-factor claim should not be overread. The 2026 older-adult PSG study found large Oura total-sleep-time underestimation in older adults and poor stage identification, particularly for deep sleep. ([Searles et al., 2026](https://academic.oup.com/sleepadvances/article/7/1/zpag006/8422777))

The metric, algorithm, population, and measurement context matter more than whether the sensor is worn on a finger or wrist. ([Robbins et al., 2024](https://www.mdpi.com/1424-8220/24/20/6532); [Searles et al., 2026](https://academic.oup.com/sleepadvances/article/7/1/zpag006/8422777))

## Behavior change evidence does not validate the exported metrics

There is evidence that wearable-delivered sleep interventions can improve some sleep outcomes. A 2023 systematic review and meta-analysis of randomized trials found that wearable-delivered sleep interventions reduced sleep disturbance and sleep-related impairment compared with comparators. ([Lai et al., 2023](https://onlinelibrary.wiley.com/doi/abs/10.1111/nhs.13011))

That does not validate every sleep metric. Intervention usefulness is separate from measurement validity: a feedback tool can be useful while sleep-stage labels, wake after sleep onset, and proprietary scores remain too inaccurate or opaque for ground-truth export. ([Chinoy et al., 2021](https://academic.oup.com/sleep/article/44/5/zsaa291/6055610); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472))

## Funding and conflict-of-interest check

The 2024 Oura/Fitbit/Apple PSG study was funded by Oura Ring Inc. The paper also disclosed that Robbins was a member of the Oura Ring Medical Advisory Board and reported consulting fees from Oura Ring Inc. Its favorable Oura results should be interpreted with that funding context in mind and should not be the sole basis for including Oura sleep-stage metrics. ([Robbins et al., 2024](https://www.mdpi.com/1424-8220/24/20/6532))

The 2021 seven-device PSG study reported no financial or nonfinancial conflicts of interest, no device-company funding, and no device-company involvement in study design, device selection, analysis, interpretation, writing, or review. It was funded by the Office of Naval Research. ([Chinoy et al., 2021](https://academic.oup.com/sleep/article/44/5/zsaa291/6055610))

The 2022 unrestricted home wearable study was funded by the Office of Naval Research and reported no potential conflicts of interest, no author relationships with the companies whose devices were evaluated, and no company involvement in any stage of the research. It found better performance for sleep-wake outcomes than for sleep stages. ([Chinoy et al., 2022](https://www.dovepress.com/performance-of-four-commercial-wearable-sleep-tracking-devices-tested--peer-reviewed-fulltext-article-NSS))

The 2024 systematic review and 2025 six-device PSG study were supported by Flanders Innovation & Entrepreneurship - VLAIO. The 2024 review declared no conflicts of interest, and the 2025 validation study reported no financial arrangements or affiliations and no nonfinancial conflicts. ([Schyvens et al., 2024](https://mhealth.jmir.org/2024/1/e52192); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472))

The 2023 multicenter PSG study disclosed that SleepRoutine was developed and operated by Asleep, and that the SleepRoutine algorithm was trained using data from Seoul National University Bundang Hospital, where some authors were affiliated. The paper stated that the entities played no role in study design, data collection, data analysis, interpretation, or writing, and that the authors conducted the study independently. ([Lee et al., 2023](https://mhealth.jmir.org/2023/1/e50983/))

The 2026 young-versus-older-adult PSG study reported no financial or nonfinancial disclosures and found substantial degradation in older adults. ([Searles et al., 2026](https://academic.oup.com/sleepadvances/article/7/1/zpag006/8422777))

## Metric verdicts for AI export

|Metric|Verdict|Reason|
|---|--:|---|
|`sleep_duration_trend_device_derived`|**Include**|Sleep detection sensitivity is consistently high, and unrestricted home data support sleep-wake tracking more than staging; the label must remain trend-based and device-derived. ([Chinoy et al., 2021](https://academic.oup.com/sleep/article/44/5/zsaa291/6055610); [Chinoy et al., 2022](https://www.dovepress.com/performance-of-four-commercial-wearable-sleep-tracking-devices-tested--peer-reviewed-fulltext-article-NSS); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472))|
|`sleep_window_timing_trend_device_derived`|**Include**|Include only as a coarse within-device timing trend, not as precise sleep onset latency. Validation studies support broader sleep-wake pattern tracking more than staging, and current recommendations distinguish core sleep measures from proprietary outputs. ([Chinoy et al., 2022](https://www.dovepress.com/performance-of-four-commercial-wearable-sleep-tracking-devices-tested--peer-reviewed-fulltext-article-NSS); [Chee et al., 2025](https://www.sciencedirect.com/science/article/abs/pii/S138994572500173X))|
|`total_sleep_time_minutes`|**Exclude**|Average bias can be acceptable in healthy adults, but individual divergence, poor wake detection, and large older-adult underestimation make the absolute number unsafe as ground truth. ([Robbins et al., 2024](https://www.mdpi.com/1424-8220/24/20/6532); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472); [Searles et al., 2026](https://academic.oup.com/sleepadvances/article/7/1/zpag006/8422777))|
|`sleep_efficiency_percent`|**Exclude**|Sleep efficiency depends on accurate wake detection; wearables often underestimate wake and overestimate sleep efficiency. ([Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472); [Lee et al., 2023](https://mhealth.jmir.org/2023/1/e50983/))|
|`awake_minutes` / `wake_after_sleep_onset_minutes`|**Exclude**|Wake specificity is poor, and WASO is directionally underestimated across devices. ([Chinoy et al., 2021](https://academic.oup.com/sleep/article/44/5/zsaa291/6055610); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472))|
|`sleep_onset_latency_minutes`|**Exclude**|It depends on detecting quiet wake versus sleep onset, the exact failure mode where wearables are weakest. ([Chinoy et al., 2021](https://academic.oup.com/sleep/article/44/5/zsaa291/6055610); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472))|
|`light_sleep_minutes`|**Exclude**|Light sleep is a common misclassification bucket, and stage agreement varies substantially across devices. ([Chinoy et al., 2022](https://www.dovepress.com/performance-of-four-commercial-wearable-sleep-tracking-devices-tested--peer-reviewed-fulltext-article-NSS); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472); [Lee et al., 2023](https://mhealth.jmir.org/2023/1/e50983/))|
|`deep_sleep_minutes`|**Exclude**|Deep sleep estimation shows poor-to-inconsistent agreement, wide error, and worse performance in older adults. ([Robbins et al., 2024](https://www.mdpi.com/1424-8220/24/20/6532); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472); [Searles et al., 2026](https://academic.oup.com/sleepadvances/article/7/1/zpag006/8422777))|
|`REM_sleep_minutes`|**Exclude**|REM estimates are indirect and show poor or inconsistent concordance across devices. ([Robbins et al., 2024](https://www.mdpi.com/1424-8220/24/20/6532); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472); [Lee et al., 2023](https://mhealth.jmir.org/2023/1/e50983/))|
|`sleep_stage_hypnogram`|**Exclude**|The epoch-level stage sequence implies PSG-like architecture, but multistate agreement is only slight, fair, or moderate depending on the device. ([Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472); [Lee et al., 2023](https://mhealth.jmir.org/2023/1/e50983/))|
|`sleep_score`, `readiness`, `recovery`, `restorative_sleep`|**Exclude**|These are proprietary composites with opaque or undocumented weighting; the sensor supports narrower sleep timing and duration trends, not a general health or recovery verdict. ([Schyvens et al., 2024](https://mhealth.jmir.org/2024/1/e52192); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472); [Chee et al., 2025](https://www.sciencedirect.com/science/article/abs/pii/S138994572500173X))|

## Practical interpretation

- Use wearables to track **whether your sleep schedule and device-derived sleep duration trend are stable or changing**. ([Chinoy et al., 2022](https://www.dovepress.com/performance-of-four-commercial-wearable-sleep-tracking-devices-tested--peer-reviewed-fulltext-article-NSS); [Chee et al., 2025](https://www.sciencedirect.com/science/article/abs/pii/S138994572500173X))

- Do not use wearable sleep stages to decide whether you got “enough deep sleep” or “enough REM.” ([Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472); [Searles et al., 2026](https://academic.oup.com/sleepadvances/article/7/1/zpag006/8422777))

- Do not rely on wearable sleep efficiency, awake time, or WASO if insomnia, long awakenings, older age, suspected sleep apnea, or fragmented sleep is part of the context. ([Lee et al., 2023](https://mhealth.jmir.org/2023/1/e50983/); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472); [Searles et al., 2026](https://academic.oup.com/sleepadvances/article/7/1/zpag006/8422777))

- For exported AI data, the safe label is not `sleep_health`. It is `device_derived_sleep_duration_trend` or `device_derived_sleep_timing_trend`. ([Chinoy et al., 2022](https://www.dovepress.com/performance-of-four-commercial-wearable-sleep-tracking-devices-tested--peer-reviewed-fulltext-article-NSS); [Schyvens et al., 2025](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472); [Chee et al., 2025](https://www.sciencedirect.com/science/article/abs/pii/S138994572500173X))


## References

- Chinoy ED, Cuellar JA, Huwa KE, Jameson JT, Watson CH, Bessman SC, Hirsch DA, Cooper AD, Drummond SPA, Markwald RR. [Performance of seven consumer sleep-tracking devices compared with polysomnography](https://academic.oup.com/sleep/article/44/5/zsaa291/6055610). _Sleep_. 2021;44(5):zsaa291. DOI: [10.1093/sleep/zsaa291](https://doi.org/10.1093/sleep/zsaa291). PMID: [33378539](https://pubmed.ncbi.nlm.nih.gov/33378539/).

- Chinoy ED, Cuellar JA, Jameson JT, Markwald RR. [Performance of Four Commercial Wearable Sleep-Tracking Devices Tested Under Unrestricted Conditions at Home in Healthy Young Adults](https://www.dovepress.com/performance-of-four-commercial-wearable-sleep-tracking-devices-tested--peer-reviewed-fulltext-article-NSS). _Nature and Science of Sleep_. 2022;14:493-516. DOI: [10.2147/NSS.S348795](https://doi.org/10.2147/NSS.S348795). PMID: [35345630](https://pubmed.ncbi.nlm.nih.gov/35345630/).

- Lee T, Cho Y, Cha KS, Jung J, Cho J, Kim H, Kim D, Hong J, Lee D, Keum M, Kushida CA, Yoon IY, Kim JW. [Accuracy of 11 Wearable, Nearable, and Airable Consumer Sleep Trackers: Prospective Multicenter Validation Study](https://mhealth.jmir.org/2023/1/e50983/). _JMIR mHealth and uHealth_. 2023;11:e50983. DOI: [10.2196/50983](https://doi.org/10.2196/50983). PMID: [37917155](https://pubmed.ncbi.nlm.nih.gov/37917155/).

- Schyvens AM, Van Oost NC, Aerts JM, Masci F, Peters B, Neven A, Dirix H, Wets G, Ross V, Verbraecken J. [Accuracy of Fitbit Charge 4, Garmin Vivosmart 4, and WHOOP Versus Polysomnography: Systematic Review](https://mhealth.jmir.org/2024/1/e52192). _JMIR mHealth and uHealth_. 2024;12:e52192. DOI: [10.2196/52192](https://doi.org/10.2196/52192). PMID: [38557808](https://pubmed.ncbi.nlm.nih.gov/38557808/).

- Robbins R, Weaver MD, Sullivan JP, Quan SF, Barger LK, Czeisler CA, et al. [Accuracy of Three Commercial Wearable Devices for Sleep Tracking in Healthy Adults](https://www.mdpi.com/1424-8220/24/20/6532). _Sensors_. 2024;24(20):6532. DOI: [10.3390/s24206532](https://doi.org/10.3390/s24206532). PMID: [39460013](https://pubmed.ncbi.nlm.nih.gov/39460013/).

- Lai MYC, Mong MSA, Cheng LJ, Lau Y. [The effect of wearable-delivered sleep interventions on sleep outcomes among adults: A systematic review and meta-analysis of randomised controlled trials](https://onlinelibrary.wiley.com/doi/abs/10.1111/nhs.13011). _Nursing & Health Sciences_. 2023;25(1):44-62. DOI: [10.1111/nhs.13011](https://doi.org/10.1111/nhs.13011). PMID: [36572659](https://pubmed.ncbi.nlm.nih.gov/36572659/).

- Chee MWL, Baumert M, Scott H, et al. [World Sleep Society recommendations for the use of wearable consumer health trackers that monitor sleep](https://www.sciencedirect.com/science/article/abs/pii/S138994572500173X). _Sleep Medicine_. 2025;131:106506. DOI: [10.1016/j.sleep.2025.106506](https://doi.org/10.1016/j.sleep.2025.106506). PMID: [40300398](https://pubmed.ncbi.nlm.nih.gov/40300398/).

- Schyvens AM, Peters B, Van Oost NC, Aerts JM, Masci F, Neven A, Dirix H, Wets G, Ross V, Verbraecken J. [A performance validation of six commercial wrist-worn wearable sleep-tracking devices for sleep stage scoring compared to polysomnography](https://academic.oup.com/sleepadvances/article/6/2/zpaf021/8090472). _SLEEP Advances_. 2025;6(2):zpaf021. DOI: [10.1093/sleepadvances/zpaf021](https://doi.org/10.1093/sleepadvances/zpaf021). PMID: [40303381](https://pubmed.ncbi.nlm.nih.gov/40303381/).

- Searles ME, Licata A, Cucinotta M, Kainec K, Spencer RMC. [Performance evaluation of consumer sleep-tracking wearables and nearables in healthy young and older adults](https://academic.oup.com/sleepadvances/article/7/1/zpag006/8422777). _SLEEP Advances_. 2026;7(1):zpag006. DOI: [10.1093/sleepadvances/zpag006](https://doi.org/10.1093/sleepadvances/zpag006). PMID: [41768372](https://pubmed.ncbi.nlm.nih.gov/41768372/).