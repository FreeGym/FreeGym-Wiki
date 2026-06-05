# Wearable Blood Oxygen and Sleep Apnea Screening

Consumer wearable SpO2 is a real physiological estimate, not a clinical oxygen measurement. The sensor can detect light-absorption changes related to oxygen saturation, but wrist and ring placement introduce enough artifact, contact-pressure dependence, perfusion variability, and algorithm opacity that the exported number should not be treated as ground-truth oxygen saturation. ([Walzel et al., 2023](https://doi.org/10.3390/s23229164); [Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003); [Lambe et al., 2026](https://doi.org/10.1038/s41746-025-02238-1))

Sleep apnea screening is a narrower and more defensible use case than clinical SpO2 interpretation. A repeated nocturnal desaturation pattern can be useful as a screening signal when the exact device and algorithm have been validated against polysomnography or a clinically accepted sleep-study reference. It is not the same as diagnosing obstructive sleep apnea, measuring apnea-hypopnea index (AHI), or ruling sleep apnea out when the wearable result is normal. ([Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003); [Abd-alrazaq et al., 2024](https://doi.org/10.2196/58187))

## What the sensor can and cannot measure

Consumer watches and some ring-worn devices use photoplethysmography (PPG), usually with red and infrared light, to estimate oxygen saturation from light absorption patterns. That is mechanistically plausible because it uses the same broad optical principle as pulse oximetry, but consumer devices may use reflectance measurements at the wrist or ring rather than controlled clinical fingertip measurement. Wrist reflectance PPG has lower signal quality in real-world wear, more motion artifact, more dependence on skin contact and contact pressure, and greater sensitivity to peripheral perfusion than controlled reference pulse oximetry. ([Walzel et al., 2023](https://doi.org/10.3390/s23229164); [Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003))

In a controlled laboratory study of Apple Watch 8, Samsung Galaxy Watch 5, and Withings ScanWatch, all three watches met the ISO root-mean-square-difference threshold during induced desaturation in 18 young healthy Caucasian volunteers, but the authors emphasized that the study population was narrow and that results may not generalize to older adults, people with chronic disease, or people with different skin pigmentation. ([Walzel et al., 2023](https://doi.org/10.3390/s23229164))

That means the mechanism is plausible but the export is not self-validating. A column labeled `SpO2` does not preserve whether the user was still, asleep, well-perfused, wearing the device tightly enough, or within the validated population. For AI use, that missing measurement context is enough to make the absolute metric unsafe. ([Walzel et al., 2023](https://doi.org/10.3390/s23229164); [Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003))

## Absolute wearable SpO2: exclude

The strongest overall evidence says consumer watch SpO2 can have a low average bias while still having clinically important error for individual readings. A 2026 systematic review and meta-analysis of Apple Watch measurements found a pooled mean SpO2 bias of about -0.04 percentage points, but the limits of agreement were roughly -4.01 to +3.94 percentage points overall and widened to about -8.35 to +9.21 percentage points in hypoxic conditions. ([Lambe et al., 2026](https://doi.org/10.1038/s41746-025-02238-1))

That distinction matters. A low average bias does not mean a specific exported value is accurate. If a wearable reports 94 percent, the true value may plausibly cross clinically meaningful thresholds in either direction, especially during hypoxemia. The same review concluded that Apple Watch SpO2 values show wider limits of agreement and lower reliability in hypoxemic ranges, where accuracy matters most. ([Lambe et al., 2026](https://doi.org/10.1038/s41746-025-02238-1))

A controlled hypoxemia validation study comparing Apple Watch Series 7 with arterial blood gas and Masimo pulse oximetry found that the Apple Watch was within 2 percentage points of arterial oxygen saturation only 32.14 percent of the time, overestimated oxygen saturation in 85.33 percent of readings when arterial saturation was below 88 percent, and had an A-rms error of 5.82 percent in that hypoxemic range. The authors reported cases where the Apple Watch showed readings above 92 percent while arterial oxygen saturation was below 88 percent. ([Jiang et al., 2026](https://doi.org/10.2196/85253))

**Verdict: exclude absolute wearable SpO2.**

That applies to spot SpO2, overnight average SpO2, minimum SpO2, and time-below-threshold values when exported from a consumer wrist or ring device. These should not be used for oxygen titration, COPD monitoring, hypoxemia monitoring, or clinical triage when the downstream system may treat the number as true oxygen saturation. ([Lambe et al., 2026](https://doi.org/10.1038/s41746-025-02238-1); [Jiang et al., 2026](https://doi.org/10.2196/85253))

## Overnight desaturation patterns are a different signal

Sleep apnea screening does not require the same claim as absolute oxygen measurement. The relevant signal is often repeated oxygen desaturation or breathing disturbance over a night, not whether a single SpO2 value is exactly correct. Pattern detection can tolerate some absolute error if the trend metric itself has been validated against polysomnography or a clinically accepted sleep-study reference. ([Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003); [Gell et al., 2025](https://doi.org/10.3389/frsle.2025.1549272))

In a Samsung Galaxy Watch 4 sleep study of 97 adults undergoing polysomnography, the watch's overnight SpO2 had an overall root mean square error of 2.3 percent versus the PSG-linked reference oximeter, but the error increased with OSA severity and 26.5 percent of potential data were rejected because of contact-pressure fluctuations or saturation values below the device's reporting floor. The watch-derived oxygen desaturation index at a threshold of at least 5 events per hour predicted moderate-to-severe OSA, defined as AHI at least 15, with 89.7 percent sensitivity, 64.1 percent specificity, 79.4 percent accuracy, and an AUC of 0.908. ([Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003))

That supports a narrow claim: a validated device-specific overnight desaturation trend can help flag possible moderate-to-severe sleep apnea. It does not support treating the wearable SpO2 number as clinically precise, and it does not support exporting a generic `sleep_apnea` diagnosis. ([Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003))

A 2025 ring-worn pulse oximeter study also found strong correlations between ring-derived ODI and PSG-derived ODI/AHI, with AUC 0.92 for detecting ODI greater than 15 and AUC 0.84 for detecting AHI greater than 15. But the same study was conducted in a sleep-lab setting, used an enriched population of patients already being studied for sleep apnea, included relatively few participants without OSA, and reported wide limits of agreement. The authors stated that further studies in larger and more diverse populations were needed before broader use. ([Gell et al., 2025](https://doi.org/10.3389/frsle.2025.1549272))

**Verdict: include only the narrow metric `validated_device_specific_nocturnal_desaturation_trend`.**

That metric passes only when the exact device or algorithm has peer-reviewed validation against PSG or a clinically accepted sleep-study reference, and only when the exported column preserves that it is a screening trend. Generic `wearable_odi`, `oxygen_drops`, `sleep_breathing_score`, or `sleep_apnea_risk` should be excluded because the context and device-specific validation do not survive export. ([Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003); [Gell et al., 2025](https://doi.org/10.3389/frsle.2025.1549272))

## Sleep apnea notifications: screening prompt, not diagnosis

Wearable sleep apnea notifications are best interpreted as prompts to seek formal testing. They should not be interpreted as diagnoses, and a normal notification history should not be interpreted as ruling out sleep apnea. ([Abd-alrazaq et al., 2024](https://doi.org/10.2196/58187); [Apple, 2024](https://www.apple.com/health/pdf/sleep-apnea/Sleep_Apnea_Notifications_on_Apple_Watch_September_2024.pdf); [Samsung, 2025](https://images.samsung.com/is/content/samsung/assets/za/apps/samsung-health-monitor/2025/IFU_SLEEP-APNEA_ZA_v1.0_2024-12_v1.2.pdf))

A 2024 systematic review and meta-analysis of wearable systems for sleep apnea found pooled sensitivity of 93.8 percent and specificity of 75.2 percent for detecting sleep apnea, but the authors also reported substantial heterogeneity, only 9 of 38 studies at low risk of bias, and suboptimal severity classification accuracy of 65.1 percent. They concluded that wearable systems are promising but not ready to replace traditional sleep assessment. ([Abd-alrazaq et al., 2024](https://doi.org/10.2196/58187))

Apple's sleep apnea notification illustrates the label gap. Apple describes the feature as based on accelerometer-derived Breathing Disturbances rather than SpO2, and Apple states that Breathing Disturbances are not equivalent to AHI. Manufacturer documentation is useful here only to define the product claim, not as independent clinical evidence. ([Apple, 2024](https://www.apple.com/health/pdf/sleep-apnea/Sleep_Apnea_Notifications_on_Apple_Watch_September_2024.pdf); [Apple, 2025](https://support.apple.com/en-in/120031))

Apple's regulatory instructions report sleep apnea notification validation as 66.3 percent sensitivity and 98.5 percent specificity. That profile is consistent with a high-specificity prompt: a notification may be worth taking seriously, but absence of notification misses a meaningful fraction of cases. ([Apple, 2024](https://regulatoryinfo.apple.com/cwt/api/ext/file?fileId=sanf%2F099-42741-G+SANF+IFU_en_GB_1729249754483.pdf))

Samsung's feature is also framed as a screening-style indication rather than diagnosis. Samsung's instructions describe it as detecting signs of moderate-to-severe obstructive sleep apnea in adults over 22 based on significant breathing disruptions across a two-night monitoring period, and they warn that the watch may not catch every case. Manufacturer documentation defines the intended-use claim but does not replace peer-reviewed validation. ([Samsung, 2025](https://images.samsung.com/is/content/samsung/assets/za/apps/samsung-health-monitor/2025/IFU_SLEEP-APNEA_ZA_v1.0_2024-12_v1.2.pdf))

**Verdict: exclude wearable sleep apnea notifications as exported health metrics.**

A user-facing notification can be useful as a prompt to seek formal evaluation, but the evidence supports a screening prompt, not a diagnosis, a rule-out result, or a completed clinical pathway from notification to confirmed diagnosis and improved outcome. An exported metric labeled `sleep_apnea_detected`, `sleep_apnea_score`, `breathing_disturbances`, or `apnea_risk` can be misused as a diagnosis or rule-out signal. For AI pipelines, that is enough to exclude it. ([Abd-alrazaq et al., 2024](https://doi.org/10.2196/58187); [Apple, 2024](https://www.apple.com/health/pdf/sleep-apnea/Sleep_Apnea_Notifications_on_Apple_Watch_September_2024.pdf); [Samsung, 2025](https://images.samsung.com/is/content/samsung/assets/za/apps/samsung-health-monitor/2025/IFU_SLEEP-APNEA_ZA_v1.0_2024-12_v1.2.pdf))

## Comparison with questionnaire screening

Questionnaires have the opposite problem from many wearable notifications: they are usually sensitive but not specific. A 2021 systematic review and meta-analysis of the STOP-Bang questionnaire in 47 sleep-clinic studies found high sensitivity, generally above 90 percent for clinically significant OSA, but low specificity in many settings. The authors framed STOP-Bang as a screening and triage tool, not a diagnostic replacement for sleep testing. ([Pivetta et al., 2021](https://doi.org/10.1001/jamanetworkopen.2021.1009))

A retrospective clinic study comparing STOP-Bang with oxygen desaturation index found STOP-Bang sensitivity of 0.9 but specificity of 0.3, while ODI had higher specificity and a larger area under the curve for OSA detection. However, that ODI came from sleep-study reports, not from consumer wearables, so it supports the general value of nocturnal desaturation patterns but does not validate consumer-device exports. ([Wang et al., 2023](https://doi.org/10.1007/s11325-022-02727-7))

The public-health argument is real but not sufficient for inclusion. The wearable sleep apnea review notes that hundreds of millions of adults worldwide likely have OSA and that most cases remain undiagnosed, so a low-friction screening prompt may have value. But public-health usefulness as a prompt does not convert a proprietary wearable output into a validated diagnostic metric. ([Abd-alrazaq et al., 2024](https://doi.org/10.2196/58187))

## Conflict of interest and funding bias

The Samsung Galaxy Watch 4 sleep SpO2 validation was supported by Samsung Medical Center, so the findings should be interpreted with that Samsung-linked support in mind. The study is still useful because it used simultaneous PSG comparison, but it should not be treated as fully independent replication. ([Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003))

The ring-worn pulse oximeter study was funded by Apnimed, several authors were employees or consultants, and the funder was involved in study design, data collection, analysis, publication decision, and manuscript preparation. That is a major conflict of interest, so its favorable findings should be treated as proof-of-concept rather than independent validation. ([Gell et al., 2025](https://doi.org/10.3389/frsle.2025.1549272))

The controlled hypoxemia Apple Watch study was funded by AstraZeneca, NIH, and NSF, and one author disclosed consulting or advisory relationships including Samsung Research America. It was not presented as Apple-funded, but the author-industry relationships should still be noted. ([Jiang et al., 2026](https://doi.org/10.2196/85253))

The 2024 wearable sleep apnea systematic review reported no conflicts of interest. Its conclusions are useful because they synthesize the broader field and explicitly caution against replacing traditional sleep assessment. ([Abd-alrazaq et al., 2024](https://doi.org/10.2196/58187))

## Metric verdicts for AI export

|Metric|Verdict|Why|
|---|--:|---|
|`wearable_spo2_percent`|**Exclude**|Individual readings have limits of agreement wide enough to cross clinical thresholds, especially during hypoxemia. ([Lambe et al., 2026](https://doi.org/10.1038/s41746-025-02238-1); [Jiang et al., 2026](https://doi.org/10.2196/85253))|
|`wearable_sleep_spo2_average`|**Exclude**|Average values hide artifact, missingness, contact-pressure problems, and hypoxemic-range error. ([Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003); [Lambe et al., 2026](https://doi.org/10.1038/s41746-025-02238-1))|
|`wearable_sleep_spo2_nadir`|**Exclude**|A single minimum value is especially vulnerable to artifact and cannot be audited after export. ([Walzel et al., 2023](https://doi.org/10.3390/s23229164); [Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003))|
|`wearable_time_below_90_percent`|**Exclude**|Threshold-crossing metrics are unsafe when absolute SpO2 error crosses the same threshold. ([Lambe et al., 2026](https://doi.org/10.1038/s41746-025-02238-1); [Jiang et al., 2026](https://doi.org/10.2196/85253))|
|`generic_wearable_odi`|**Exclude**|ODI validity is device-, algorithm-, population-, and wear-condition-specific; the generic export loses those constraints. ([Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003); [Gell et al., 2025](https://doi.org/10.3389/frsle.2025.1549272))|
|`validated_device_specific_nocturnal_desaturation_trend`|**Include**|This is the narrow metric supported by peer-reviewed device-specific validation when used only as a screening trend, not as oxygen titration or diagnosis. ([Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003); [Gell et al., 2025](https://doi.org/10.3389/frsle.2025.1549272))|
|`sleep_apnea_detected`|**Exclude**|Wearables are screening prompts; they do not diagnose OSA and may miss cases. ([Abd-alrazaq et al., 2024](https://doi.org/10.2196/58187); [Apple, 2024](https://www.apple.com/health/pdf/sleep-apnea/Sleep_Apnea_Notifications_on_Apple_Watch_September_2024.pdf); [Samsung, 2025](https://images.samsung.com/is/content/samsung/assets/za/apps/samsung-health-monitor/2025/IFU_SLEEP-APNEA_ZA_v1.0_2024-12_v1.2.pdf))|
|`sleep_apnea_risk_score`|**Exclude**|Proprietary or composite risk scores should not be exported as clinical status unless the exact exported metric has peer-reviewed validation and preserves its intended screening context. ([Abd-alrazaq et al., 2024](https://doi.org/10.2196/58187); [Apple, 2024](https://www.apple.com/health/pdf/sleep-apnea/Sleep_Apnea_Notifications_on_Apple_Watch_September_2024.pdf); [Samsung, 2025](https://images.samsung.com/is/content/samsung/assets/za/apps/samsung-health-monitor/2025/IFU_SLEEP-APNEA_ZA_v1.0_2024-12_v1.2.pdf))|
|`apple_breathing_disturbances`|**Exclude**|Apple defines this as accelerometer-derived breathing disturbance, not AHI; Apple regulatory instructions report high specificity but only moderate sensitivity for sleep apnea notification. ([Apple, 2024](https://www.apple.com/health/pdf/sleep-apnea/Sleep_Apnea_Notifications_on_Apple_Watch_September_2024.pdf); [Apple, 2024](https://regulatoryinfo.apple.com/cwt/api/ext/file?fileId=sanf%2F099-42741-G+SANF+IFU_en_GB_1729249754483.pdf))|
|`samsung_sleep_apnea_feature_result`|**Exclude**|The product is framed as a screening indication for signs of moderate-to-severe OSA, not diagnosis, and device-specific conditions do not survive generic export. ([Samsung, 2025](https://images.samsung.com/is/content/samsung/assets/za/apps/samsung-health-monitor/2025/IFU_SLEEP-APNEA_ZA_v1.0_2024-12_v1.2.pdf); [Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003))|
|PSG or HSAT-derived `AHI`, `REI`, or clinical `ODI`|**Include**|These are sleep-study outputs, not consumer wearable estimates, and are the reference comparators used in validation studies. ([Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003); [Wang et al., 2023](https://doi.org/10.1007/s11325-022-02727-7))|

## Quick reference values

- Apple Watch SpO2 meta-analysis: pooled mean bias -0.04 percentage points; limits of agreement -4.01 to +3.94 percentage points overall; hypoxic subgroup limits of agreement -8.35 to +9.21 percentage points. ([Lambe et al., 2026](https://doi.org/10.1038/s41746-025-02238-1))

- Apple Watch Series 7 controlled hypoxemia study: 32.14 percent of readings within 2 percentage points of arterial oxygen saturation; A-rms 5.82 percent when arterial saturation was below 88 percent; overestimation in 85.33 percent of hypoxemic readings. ([Jiang et al., 2026](https://doi.org/10.2196/85253))

- Samsung Galaxy Watch 4 sleep validation: overnight SpO2 RMSE 2.3 percent; 26.5 percent data rejection; ODI threshold predicting AHI at least 15 had 89.7 percent sensitivity and 64.1 percent specificity. ([Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003))

- Wearable sleep apnea meta-analysis: pooled sensitivity 93.8 percent and specificity 75.2 percent for sleep apnea detection, but severity classification accuracy 65.1 percent and evidence not ready to replace traditional sleep assessment. ([Abd-alrazaq et al., 2024](https://doi.org/10.2196/58187))

- STOP-Bang meta-analysis: high sensitivity for clinically significant OSA, generally above 90 percent, but low specificity; useful for triage, not diagnosis. ([Pivetta et al., 2021](https://doi.org/10.1001/jamanetworkopen.2021.1009))


## Practical interpretation

- A wearable SpO2 value is not reliable enough for clinical oxygen decisions. The number should not guide oxygen titration, COPD management, hypoxemia monitoring, or urgent care decisions when treated as true oxygen saturation. ([Lambe et al., 2026](https://doi.org/10.1038/s41746-025-02238-1); [Jiang et al., 2026](https://doi.org/10.2196/85253))

- Repeated nocturnal desaturation patterns can be useful for screening when the exact device-specific trend has been validated against PSG or HSAT, but that claim is much narrower than "the wearable detects sleep apnea." ([Jung et al., 2022](https://doi.org/10.1016/j.sleh.2022.04.003); [Gell et al., 2025](https://doi.org/10.3389/frsle.2025.1549272))

- A positive sleep apnea notification should be treated as a reason to seek formal sleep testing, not as a diagnosis. A normal wearable result should not be treated as ruling sleep apnea out. ([Abd-alrazaq et al., 2024](https://doi.org/10.2196/58187); [Apple, 2024](https://regulatoryinfo.apple.com/cwt/api/ext/file?fileId=sanf%2F099-42741-G+SANF+IFU_en_GB_1729249754483.pdf); [Samsung, 2025](https://images.samsung.com/is/content/samsung/assets/za/apps/samsung-health-monitor/2025/IFU_SLEEP-APNEA_ZA_v1.0_2024-12_v1.2.pdf))

- The marketing gap is the finding: "blood oxygen," "sleep apnea," and "breathing disturbances" sound clinically broad, but the supported claim is narrower. Selected devices may detect repeated overnight patterns suggestive of sleep-disordered breathing in selected adults under adequate wear conditions. They do not produce clinical oxygen saturation or a sleep apnea diagnosis. ([Walzel et al., 2023](https://doi.org/10.3390/s23229164); [Abd-alrazaq et al., 2024](https://doi.org/10.2196/58187); [Apple, 2024](https://www.apple.com/health/pdf/sleep-apnea/Sleep_Apnea_Notifications_on_Apple_Watch_September_2024.pdf); [Samsung, 2025](https://images.samsung.com/is/content/samsung/assets/za/apps/samsung-health-monitor/2025/IFU_SLEEP-APNEA_ZA_v1.0_2024-12_v1.2.pdf))


## References

- Abd-alrazaq A, et al. [Detection of Sleep Apnea Using Wearable AI: Systematic Review and Meta-Analysis](https://doi.org/10.2196/58187). _Journal of Medical Internet Research_. 2024;26:e58187. DOI: 10.2196/58187.

- Apple. [Estimating Breathing Disturbances and Sleep Apnea Risk from Apple Watch](https://www.apple.com/health/pdf/sleep-apnea/Sleep_Apnea_Notifications_on_Apple_Watch_September_2024.pdf). 2024.

- Apple. [Sleep Apnoea Notification Feature Instructions for Use](https://regulatoryinfo.apple.com/cwt/api/ext/file?fileId=sanf%2F099-42741-G+SANF+IFU_en_GB_1729249754483.pdf). 2024.

- Apple. [Sleep apnoea notifications on your Apple Watch](https://support.apple.com/en-in/120031). 2025.

- Gell LK, et al. [Performance evaluation of a ring-worn pulse oximeter for the identification and monitoring of obstructive sleep apnea](https://doi.org/10.3389/frsle.2025.1549272). _Frontiers in Sleep_. 2025;4:1549272. DOI: 10.3389/frsle.2025.1549272.

- Jiang Y, et al. [Performance of Wearable Pulse Oximetry During Controlled Hypoxia Induction: Instrument Validation Study](https://doi.org/10.2196/85253). _JMIR Formative Research_. 2026;10:e85253. DOI: 10.2196/85253.

- Jung H, et al. [Performance evaluation of a wrist-worn reflectance pulse oximeter during sleep](https://doi.org/10.1016/j.sleh.2022.04.003). _Sleep Health_. 2022;8(5):420-428. DOI: 10.1016/j.sleh.2022.04.003.

- Lambe R, et al. [The accuracy of Apple Watch measurements: a living systematic review and meta-analysis](https://doi.org/10.1038/s41746-025-02238-1). _npj Digital Medicine_. 2026;9(1):63. DOI: 10.1038/s41746-025-02238-1.

- Pivetta B, et al. [Use and Performance of the STOP-Bang Questionnaire for Obstructive Sleep Apnea Screening Across Geographic Regions: A Systematic Review and Meta-Analysis](https://doi.org/10.1001/jamanetworkopen.2021.1009). _JAMA Network Open_. 2021;4(3):e211009. DOI: 10.1001/jamanetworkopen.2021.1009.

- Samsung. [Sleep Apnoea Feature: Instructions for Use](https://images.samsung.com/is/content/samsung/assets/za/apps/samsung-health-monitor/2025/IFU_SLEEP-APNEA_ZA_v1.0_2024-12_v1.2.pdf). 2025.

- Walzel S, Mikus R, Rafl-Huttova V, Rozanek M, Bachman TE, Rafl J. [Evaluation of Leading Smartwatches for the Detection of Hypoxemia: Comparison to Reference Oximeter](https://doi.org/10.3390/s23229164). _Sensors_. 2023;23(22):9164. DOI: 10.3390/s23229164.

- Wang Y, et al. [Comparison of the value of the STOP-BANG questionnaire with oxygen desaturation index in screening obstructive sleep apnea in Germany](https://doi.org/10.1007/s11325-022-02727-7). _Sleep and Breathing_. 2023;27:1315-1323. DOI: 10.1007/s11325-022-02727-7.