# Are Recovery, Readiness, and Stress Scores Meaningful?

For exported health-data pipelines, the verdict is **exclude**. Recovery, readiness, stress, body-battery, and energy scores are not direct measurements; they are proprietary composites that claim to quantify readiness, recovery, stress, or well-being. Their validity, transparency, physiological relevance, and clinical applicability remain unclear. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001)) They are built from partially validated inputs, then translated into a broader claim about the body’s state. That broader claim has not been independently validated well enough for context-stripped export. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001))

## What these scores are

A 2025 evaluation of consumer wearable composite health scores identified 14 scores across 10 manufacturers, including Fitbit Daily Readiness, Garmin Body Battery and Training Readiness, Oura Readiness and Resilience, WHOOP Recovery and Stress Monitor, Samsung Energy Score, Ultrahuman Dynamic Recovery, and others. The most common inputs were heart rate variability, resting heart rate, physical activity, and sleep duration. None of the manufacturers disclosed the exact algorithmic formula, and few provided peer-reviewed evidence supporting the accuracy or clinical relevance of the final composite score. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001))

That means the evidence question is not “can HRV or sleep be useful?” It is “does this finished score accurately measure recovery, readiness, stress, or energy in typical use?” The answer, for the listed branded composite scores, is **no qualifying evidence**. Doherty et al. concluded that while individual metrics such as HRV or resting heart rate are better supported, the proprietary algorithms behind composite health scores and the lack of methodological disclosure hinder reproducibility and independent scrutiny. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001))

## What the sensors can and cannot measure

Consumer wearables can measure some physiological signals reasonably well under certain conditions. Heart rate from photoplethysmography is generally accurate at rest, with typical mean absolute errors around 2 beats per minute, but accuracy declines during physical activity and is affected by movement, activity type, contact pressure, and sweat. ([Jamieson et al., 2025](https://doi.org/10.1038/s44325-025-00082-6))

Wearable “HRV” from optical sensors is usually pulse rate variability, not ECG-derived beat-to-beat HRV. It can correlate well with ECG-derived HRV at rest, but agreement declines as exercise intensity increases. That makes overnight or resting HRV more plausible than all-day HRV during movement, but it still does not directly measure “readiness” or “recovery.” ([Jamieson et al., 2025](https://doi.org/10.1038/s44325-025-00082-6))

Sleep tracking is also indirect. Wearables estimate sleep from movement and physiological signals, while polysomnography remains the reference standard. In validation work summarized in a 2025 review, sleep-stage agreement was moderate for some devices and fair for others, and wearables generally overestimated sleep by misclassifying awake stillness as sleep. ([Jamieson et al., 2025](https://doi.org/10.1038/s44325-025-00082-6))

Stress detection is mechanistically plausible because acute stress can increase heart rate and reduce HRV, and some devices add electrodermal activity, respiratory rate, or temperature. But this remains an arousal proxy, not a direct measurement of psychological stress. Motion artifact and vigorous movement can reduce stress-detection accuracy, and real-world studies show weak or misleading alignment between wearable stress outputs and self-reported stress or mood. ([Jamieson et al., 2025](https://doi.org/10.1038/s44325-025-00082-6); [Siepe et al., 2025](https://doi.org/10.1037/abn0001013); [van der Mee et al., 2025](https://doi.org/10.1016/j.jadr.2025.100974))

## The composite step is the unsupported step

The raw inputs are narrower than the branded claim. A wearable may estimate resting heart rate, pulse-rate variability, movement, sleep duration, respiratory rate, or temperature. A recovery or readiness score claims to infer whether the body is prepared for stress, training, or performance. The current composite-score literature does not provide enough independent evidence that these finished scores validly measure those broader states across typical users and likely-use populations. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001); [Jamieson et al., 2025](https://doi.org/10.1038/s44325-025-00082-6))

There is evidence that HRV-guided endurance training can have some value as a training-adjustment method, but that evidence does not validate proprietary green/yellow/red readiness scores. A 2021 systematic review and meta-analysis found HRV-guided training had a medium effect on submaximal physiological parameters, but only small, non-significant effects on performance and VO₂peak compared with predefined training. ([Düking et al., 2021](https://doi.org/10.1016/j.jsams.2021.04.012))

User-experience studies show that people do use these scores to guide behavior, validate feelings, and modify training or recovery routines. That is evidence that the scores affect users, not evidence that the scores accurately measure recovery or readiness. A 2026 qualitative study of WHOOP and Oura users found that scores shaped behavior and self-perception, including validation, experimentation, and sometimes emotional reactivity. The authors reported no competing interests and no funding used to assist preparation of the article. ([Ibrahim et al., 2026](https://doi.org/10.1007/s10484-025-09762-6))

## Stress scores are especially vulnerable to label inflation

The Garmin stress score illustrates the gap between physiological arousal and the word “stress.” In a large ecological momentary assessment study using Garmin VivoSmart 4 watches, the Garmin stress score was based on heart rate, HRV, and activity, used a proprietary Firstbeat algorithm, and was not described in enough detail to be reproducible. The same paper reported that Body Battery had not yet been validated in peer-reviewed research at the time of the study. ([Siepe et al., 2025](https://doi.org/10.1037/abn0001013); [available PDF](https://eiko-fried.com/wp-content/uploads/EBSCO-FullText-11_21_2025-1.pdf))

In that study, the association between self-reported stress and Garmin sensor stress was very small: a one-standard-deviation change in self-reported stress corresponded to only a 0.026-standard-deviation change in sensor stress. The authors described an “astonishing lack of overlap” between sensor and self-report stress and warned against replacing self-report with passive measures without proper validation. The study declared no conflicts of interest and was funded through European research grants, not Garmin. ([Siepe et al., 2025](https://doi.org/10.1037/abn0001013); [available PDF](https://eiko-fried.com/wp-content/uploads/EBSCO-FullText-11_21_2025-1.pdf))

A separate 2025 study of 95 healthy young adults over 28 days found that the Garmin Stress Score was associated with relaxation and positive arousal, but not with negative or high-arousal negative mood. The authors concluded that the term “Stress Score” was incorrect and misleading to consumers. ([van der Mee et al., 2025](https://doi.org/10.1016/j.jadr.2025.100974))

This broader problem is not limited to Garmin. In a 2022 longitudinal study of 657 information workers with 14,695 ecological momentary assessments, wearable-derived HRV features explained an average of only 1% of the variance in perceived stress across time windows. The authors concluded that wearable-derived HRV alone should not be treated as a proxy for perceived stress in naturalistic settings. The paper declared no conflicts of interest. ([Martinez et al., 2022](https://doi.org/10.2196/33754))

## The relative-trend argument

A personal trend can feel useful. If a user’s readiness score drops after poor sleep, alcohol, illness, or heavy training, the pattern may prompt reflection. But for export into a data pipeline, subjective usefulness is not enough. A trend-only metric should be included only when the trend of that exact score is independently validated as reliable for the intended construct. Mechanistic plausibility is not enough when the finished score is a proprietary composite with unclear validation. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001))

Garmin Body Battery is the closest example of a partial trend-like signal, but it still fails the inclusion standard. In the large student EMA study, Body Battery was negatively associated with self-reported tiredness, but the relationship was modest, person-specific estimates were heterogeneous, and the model’s RMSE was 20.46 on a 0-100 scale, roughly one-fifth of the full range. That is not strong enough to export as “energy,” “recovery,” or “readiness.” ([Siepe et al., 2025](https://doi.org/10.1037/abn0001013); [available PDF](https://eiko-fried.com/wp-content/uploads/EBSCO-FullText-11_21_2025-1.pdf))

## Brand-by-brand verdict

|Metric|Verdict|Reason|
|---|--:|---|
|WHOOP Recovery|**Exclude**|Proprietary composite. The 2025 composite-score review found no disclosed exact formula and little peer-reviewed validation for composite scores as finished outputs. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001))|
|WHOOP Stress Monitor|**Exclude**|Proprietary stress composite included in the composite-score review; stress is not directly measured, and wearable stress detection remains vulnerable to arousal/valence confusion and motion artifact. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001); [Jamieson et al., 2025](https://doi.org/10.1038/s44325-025-00082-6); [Siepe et al., 2025](https://doi.org/10.1037/abn0001013))|
|Garmin Body Battery|**Exclude**|Weak-to-modest association with tiredness in a large EMA study, large error, heterogeneous person-level associations, proprietary algorithm, and no peer-reviewed validation sufficient for export as “energy” or “recovery.” ([Siepe et al., 2025](https://doi.org/10.1037/abn0001013); [available PDF](https://eiko-fried.com/wp-content/uploads/EBSCO-FullText-11_21_2025-1.pdf))|
|Garmin Training Readiness|**Exclude**|Proprietary readiness composite with no qualifying independent validation showing that the score accurately predicts training readiness or improves outcomes versus simpler inputs or judgment. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001))|
|Garmin Stress Score|**Exclude**|Lab and real-world studies suggest it may reflect autonomic arousal, but not psychological stress. EMA studies show very small overlap with self-reported stress, and a separate mood study concluded that the “Stress Score” label is misleading. ([Siepe et al., 2025](https://doi.org/10.1037/abn0001013); [van der Mee et al., 2025](https://doi.org/10.1016/j.jadr.2025.100974))|
|Oura Readiness Score|**Exclude**|Proprietary readiness composite. Some Oura raw sleep and physiological inputs have validation literature, but that does not validate the final readiness score as a measurement of readiness. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001); [Jamieson et al., 2025](https://doi.org/10.1038/s44325-025-00082-6))|
|Samsung Energy Score|**Exclude**|Included among composite health scores with undisclosed exact formula and insufficient peer-reviewed validation for the finished score. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001))|
|Ultrahuman Dynamic Recovery|**Exclude**|Included among composite health scores with undisclosed exact formula and insufficient peer-reviewed validation for the finished score. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001))|
|FITTR HART recovery output|**Exclude**|The product page describes Recovery Score as using HRV, sleep, and resting heart rate to assess recovery, but it does not document qualifying independent peer-reviewed validation of the finished recovery output. Mechanistic plausibility is not enough. ([FITTR HART product page](https://shop.fittr.care/products/fittr-hart-ring); [FITTR FAQ](https://www.fittr.com/faq/))|
|FITTR HART stress output|**Exclude**|The product page markets stress monitoring and lists stress as a tracked feature, but it does not document qualifying independent peer-reviewed validation of the finished stress output. Stress is inferred from physiological signals and modeling, not directly measured by the ring. ([FITTR HART product page](https://shop.fittr.care/products/fittr-hart-ring); [FITTR FAQ](https://www.fittr.com/faq/); [Jamieson et al., 2025](https://doi.org/10.1038/s44325-025-00082-6))|
|Generic exported `recovery_score`, `readiness_score`, `stress_score`, `energy_score`, or `body_battery` column|**Exclude**|The column name overstates the evidence. Downstream systems should not treat these labels as ground truth because these composites lack the validation needed for that use. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001))|

## The marketing gap

The narrow claim supported by the sensor stack is: “this device may estimate resting heart rate, pulse-rate variability, sleep duration, movement, and sometimes temperature or respiratory patterns under certain conditions.” Consumer-wearable reviews support those narrower measurement categories, with important limits by device, context, and condition. ([Jamieson et al., 2025](https://doi.org/10.1038/s44325-025-00082-6))

The broader marketed claim is: “this score tells you whether you are recovered, ready, stressed, or energized.” The gap between those two claims is the finding. Composite-score reviews find proprietary algorithms, undisclosed formulae, inconsistent inputs, and insufficient validation of the finished branded scores. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001))

A high stress score does not establish psychological stress. A low recovery score does not establish impaired biological recovery. A green readiness score does not establish readiness to train hard. The output may be a user-interface prompt, but it is not a validated health metric. ([Siepe et al., 2025](https://doi.org/10.1037/abn0001013); [van der Mee et al., 2025](https://doi.org/10.1016/j.jadr.2025.100974); [Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001))

## Quick reference

- `recovery_score`: **Exclude**. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001))

- `readiness_score`: **Exclude**. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001))

- `stress_score`: **Exclude**. ([Siepe et al., 2025](https://doi.org/10.1037/abn0001013); [van der Mee et al., 2025](https://doi.org/10.1016/j.jadr.2025.100974))

- `body_battery`: **Exclude**. ([Siepe et al., 2025](https://doi.org/10.1037/abn0001013))

- `energy_score`: **Exclude**. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001))

- Raw resting heart rate, overnight HRV, sleep duration, respiratory rate, or temperature: not automatically included, but they should be evaluated under their own exact labels and device-specific validation evidence, not relabeled as recovery, readiness, stress, or energy. ([Jamieson et al., 2025](https://doi.org/10.1038/s44325-025-00082-6); [Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001))


## Practical interpretation

For human self-reflection, these scores can be used only as prompts: “Does this match how I feel?” “Did sleep, alcohol, illness, travel, or training load change?” Qualitative work supports that users do treat readiness and recovery scores as prompts for validation, self-experimentation, and behavior adjustment, but that is a behavior-design use, not a measurement-validity claim. ([Ibrahim et al., 2026](https://doi.org/10.1007/s10484-025-09762-6))

For AI systems, research datasets, coaching engines, or exported health records, the composite score should be dropped. Keep validated raw inputs only when the device, measurement condition, sampling window, and label are specific enough to preserve meaning. A context-stripped number called `readiness_score` manufactures more confidence than the evidence supports. ([Doherty et al., 2025](https://doi.org/10.1515/teb-2025-0001); [Jamieson et al., 2025](https://doi.org/10.1038/s44325-025-00082-6))

## References

- [Doherty C, Baldwin M, Lambe R, Burke D, Altini M. _Readiness, recovery, and strain: an evaluation of composite health scores in consumer wearables._ Translational Exercise Biomedicine. 2025;2(2):128-144. DOI: 10.1515/teb-2025-0001.](https://doi.org/10.1515/teb-2025-0001) The authors declared no conflicts of interest; funding came from the Health Research Board in Ireland and Research Ireland.

- [Jamieson A, Chico TJA, Jones S, Chaturvedi N, Hughes AD, Orini M. _A guide to consumer-grade wearables in cardiovascular clinical care and population health for non-experts._ npj Cardiovascular Health. 2025;2:44. DOI: 10.1038/s44325-025-00082-6.](https://doi.org/10.1038/s44325-025-00082-6) The authors declared no competing interests.

- [Siepe BS, Tutunji R, Rieble CL, Proppert RKK, Fried EI. _Associations Between Ecological Momentary Assessment and Passive Sensor Data in a Large Student Sample._ Journal of Psychopathology and Clinical Science. 2025;134(8):912-925. DOI: 10.1037/abn0001013.](https://doi.org/10.1037/abn0001013) [Available PDF.](https://eiko-fried.com/wp-content/uploads/EBSCO-FullText-11_21_2025-1.pdf) The authors declared no conflicts of interest; funding came from European research grants.

- [van der Mee DJ, Koyuncu Z, Lemmers-Jansen ILJ. _Are you stressed or just excited? What the Garmin Stress Score can say about your mood._ Journal of Affective Disorders Reports. 2025;21:100974. DOI: 10.1016/j.jadr.2025.100974.](https://doi.org/10.1016/j.jadr.2025.100974)

- [Martinez GJ, Grover T, Mattingly SM, Mark G, D’Mello S, Aledavood T, Akbar F, Robles-Granda P, Striegel A. _Alignment Between Heart Rate Variability From Fitness Trackers and Perceived Stress: Perspectives From a Large-Scale In Situ Longitudinal Study of Information Workers._ JMIR Human Factors. 2022;9(3):e33754. DOI: 10.2196/33754.](https://doi.org/10.2196/33754) The paper declared no conflicts of interest.

- [Düking P, Zinner C, Trabelsi K, Reed JL, Holmberg HC, Kunz P, Sperlich B. _Monitoring and adapting endurance training on the basis of heart rate variability monitored by wearable technologies: A systematic review with meta-analysis._ Journal of Science and Medicine in Sport. 2021;24(11):1180-1192. DOI: 10.1016/j.jsams.2021.04.012.](https://doi.org/10.1016/j.jsams.2021.04.012)

- [Ibrahim AH, Beaumont CT, Strohacker K. _“The More You Give the Wearable, the More It Gives You”: How Regular Exercisers Navigate Exercise Using Wearable Devices._ Applied Psychophysiology and Biofeedback. 2026. DOI: 10.1007/s10484-025-09762-6.](https://doi.org/10.1007/s10484-025-09762-6) The authors declared no competing interests; no sources of funding were used to assist preparation of the article.

- [FITTR HART Ring X2 product page.](https://shop.fittr.care/products/fittr-hart-ring) Manufacturer source used only to document advertised FITTR HART features and inputs, not as evidence of validity.

- [FITTR FAQ.](https://www.fittr.com/faq/) Manufacturer source used only to document advertised FITTR HART features and claims, not as evidence of validity.