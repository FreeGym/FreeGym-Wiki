# Wearable VO₂ Max

**Verdict: exclude.** Wearable VO₂ max should not be included as a health metric in stripped data exports. The exported column name implies a direct or clinically interpretable VO₂ max value, while the device output is a proprietary estimate derived from heart rate, movement, GPS, user-entered characteristics, and model assumptions. Apple describes its Cardio Fitness metric as an estimate of VO₂ max based on heart-rate response to physical activity, generated under conditions such as outdoor walking, running, or hiking, relatively flat ground, adequate GPS, heart-rate signal quality, and sufficient exertion. ([Apple, 2021](https://www.apple.com/healthcare/docs/site/Using_Apple_Watch_to_Estimate_Cardio_Fitness_with_VO2_max.pdf); [Apple Support, 2025](https://support.apple.com/en-in/108790))

The narrower supported claim is not "this person's VO₂ max." The supported claim is closer to: "under certain exercise conditions, some devices can produce a model-derived cardiorespiratory fitness estimate that correlates with laboratory VO₂ max at the group level." That gap is the finding. ([Molina-Garcia et al., 2022](https://doi.org/10.1007/s40279-021-01639-y))

## What wearable VO₂ max is and is not

VO₂ max is directly measured in a laboratory using respiratory gas analysis during exercise testing; in one Apple Watch validation study, indirect calorimetry was used as the criterion method for comparison. ([Železnik Mežan, 2025](https://doi.org/10.3389/fspor.2025.1707991); [Lambe et al., 2025](https://doi.org/10.1371/journal.pone.0323741))

Consumer wearables do not measure oxygen uptake. They estimate VO₂ max from signals such as heart rate, GPS-derived speed or pace, movement, and user characteristics, then map those signals onto a population model. Apple’s public-facing documentation describes Cardio Fitness as an estimate of VO₂ max based on heart-rate response to physical activity, and a validation study of Apple Watch Series 7 noted that the precise algorithm was not publicly disclosed. ([Apple, 2021](https://www.apple.com/healthcare/docs/site/Using_Apple_Watch_to_Estimate_Cardio_Fitness_with_VO2_max.pdf); [Caserman et al., 2024](https://doi.org/10.2196/59459))

That makes wearable VO₂ max an indirect model output, not a physiological measurement. The distinction matters because the exported label "VO₂ max" survives, while the device, algorithm version, activity type, heart-rate sensor type, terrain, temperature, exertion threshold, GPS quality, and medication context often do not. Apple documentation itself describes qualifying conditions for estimates, including outdoor walking, running, or hiking, relatively flat ground, adequate GPS, adequate heart-rate signal quality, and sufficient exertion. ([Apple, 2021](https://www.apple.com/healthcare/docs/site/Using_Apple_Watch_to_Estimate_Cardio_Fitness_with_VO2_max.pdf); [Apple Support, 2025](https://support.apple.com/en-in/108790))

## What the validation evidence shows

A 2022 systematic review and meta-analysis found 14 validation studies of wearable VO₂ max estimation. Resting-condition algorithms overestimated VO₂ max by a mean bias of 2.17 mL/kg/min, with wide limits of agreement from -13.07 to 17.41 mL/kg/min. Exercise-based algorithms had lower mean bias, -0.09 mL/kg/min, but still had wide limits of agreement from -9.92 to 9.74 mL/kg/min. The authors concluded that exercise-based estimates may be acceptable at the population level, but individual-level error remains too large for many sport and clinical uses. ([Molina-Garcia et al., 2022](https://doi.org/10.1007/s40279-021-01639-y))

A 2025 systematic review of wearable exercise-test estimates found 13 recent studies. Most studies on wearable VO₂ max or lactate-threshold estimation involved Garmin smartwatches, compatible chest-belt heart-rate sensors, and Firstbeat-style algorithms; VO₂ max reference testing was performed in the laboratory using treadmill graded exercise testing with respiratory gas analysis, while estimates were typically generated from submaximal outdoor runs. Seven studies were judged valid or acceptable for VO₂ max estimation, but the review also emphasized small samples, limited generalizability, unavailable algorithms, and the need for longitudinal studies to test whether estimates remain accurate and stable over months or years. ([Železnik Mežan, 2025](https://doi.org/10.3389/fspor.2025.1707991))

Apple Watch validation is less supportive. In a 2024 study of Apple Watch Series 7 against laboratory testing, the Apple estimate differed significantly from lab VO₂ max, had poor reliability by ICC, and produced a mean absolute percentage error of 15.79 percent. The device tended to overestimate people with poor fitness and underestimate people with good or excellent fitness, though subgroup sizes were small. ([Caserman et al., 2024](https://doi.org/10.2196/59459))

A 2025 PLOS One validation study found that Apple Watch underestimated VO₂ max by a mean of 6.07 mL/kg/min, with limits of agreement from -6.11 to 18.26 mL/kg/min and a mean absolute percentage error of 13.31 percent. The authors concluded that Apple Watch VO₂ max estimates require further refinement before clinical implementation. ([Lambe et al., 2025](https://doi.org/10.1371/journal.pone.0323741))

A 2026 Apple Watch Series 10 validation in _Mayo Clinic Proceedings: Digital Health_ also reported poor individual-level agreement with criterion measures, with limits of agreement from -18.23 to 5.73 mL/kg/min and mean absolute error of 6.79 mL/kg/min. ([Lambe et al., 2026](https://doi.org/10.1016/j.mcpdig.2026.100357))

Garmin evidence is more favorable in narrow settings. A 2023 study in athletes using Garmin fēnix 6 reported mean absolute percentage error of 6.85 percent and concordance correlation of 0.70 versus laboratory VO₂ max, but the authors warned against extrapolating to other devices or the general population. ([Carrier et al., 2023](https://doi.org/10.3390/technologies11030071)) A 2025 Garmin fēnix 6 study in apparently healthy active and sedentary adults reported acceptable accuracy against 15- and 30-second averaged laboratory VO₂ max, with 30-second MAPE of 7.05 percent and concordance correlation of 0.73, but it used a Garmin HRM-Run chest monitor and a controlled outdoor running protocol. ([Carrier et al., 2025](https://doi.org/10.3390/s25010275))

## Why the absolute number fails

The absolute number fails because the error is too large at the individual level. A roughly +/-10 mL/kg/min range is not a small nuisance error; the 2022 meta-analysis found this level of individual uncertainty even when mean bias looked small in exercise-based algorithms. ([Molina-Garcia et al., 2022](https://doi.org/10.1007/s40279-021-01639-y))

The estimate also depends on the heart-rate-to-workload relationship. That relationship can be altered by sensor type, heart-rate signal quality, GPS quality, terrain, activity type, exertion, temperature, medication that affects heart rate, and the protocol used to generate the estimate. Apple documentation lists GPS, heart-rate signal quality, terrain grade, exertion, activity type, and heart-rate-affecting medication as relevant to VO₂ max estimation, while the 2025 review notes that accuracy depends heavily on protocol, sensor type, subject-related parameters, and environmental conditions. ([Apple, 2021](https://www.apple.com/healthcare/docs/site/Using_Apple_Watch_to_Estimate_Cardio_Fitness_with_VO2_max.pdf); [Apple Support, 2025](https://support.apple.com/en-in/108790); [Železnik Mežan, 2025](https://doi.org/10.3389/fspor.2025.1707991); [Carrier et al., 2025](https://doi.org/10.3390/s25010275))

The device output is also partly opaque. Review authors note that manufacturers do not disclose algorithms in detail and that this limits comparability across devices. Apple Watch Series 7 validation authors similarly noted that the precise Apple Watch VO₂ max algorithm was not publicly disclosed. ([Železnik Mežan, 2025](https://doi.org/10.3389/fspor.2025.1707991); [Caserman et al., 2024](https://doi.org/10.2196/59459))

For a stripped export, that opacity is decisive. A downstream system seeing `VO2_max = 45` can treat the value like a measurement unless the export preserves device model, software version, activity type, GPS quality, heart-rate signal quality, sensor type, terrain, environmental conditions, and qualifying-workout context. The validation literature shows that those details materially affect interpretation. ([Apple, 2021](https://www.apple.com/healthcare/docs/site/Using_Apple_Watch_to_Estimate_Cardio_Fitness_with_VO2_max.pdf); [Železnik Mežan, 2025](https://doi.org/10.3389/fspor.2025.1707991))

## Can the trend be included?

**Verdict: exclude the trend too.**

The best argument for wearable VO₂ max is not that the number is accurate, but that the direction of change might be useful if the same person uses the same device under similar conditions for months. That claim is plausible, but the consumer metric does not meet the inclusion standard unless the trend itself has independent peer-reviewed validation in typical-use conditions.

The 2025 systematic review explicitly states that longitudinal studies are needed to determine whether wearable estimates remain accurate and stable over months or years. ([Železnik Mežan, 2025](https://doi.org/10.3389/fspor.2025.1707991))

Research-grade longitudinal modeling shows why trend detection is possible in principle but does not rescue consumer exports. A 2022 _npj Digital Medicine_ study used wearable sensor data to estimate cardiorespiratory fitness and detect long-term change, but it was a custom research algorithm, not a consumer watch VO₂ max export. Its direction-of-change performance was modest, with an AUC of 0.61 for detecting the direction of individual fitness change, and its change estimate correlated imperfectly with measured change. ([Spathis et al., 2022](https://doi.org/10.1038/s41746-022-00719-1))

That means the trend claim remains unvalidated for the exported consumer metric. A rising or falling watch estimate may reflect fitness change, but it may also reflect activity selection, device-specific qualifying rules, GPS quality, heart-rate signal quality, terrain, weather, sensor type, medication effects, or how often the user performs qualifying workouts. ([Apple, 2021](https://www.apple.com/healthcare/docs/site/Using_Apple_Watch_to_Estimate_Cardio_Fitness_with_VO2_max.pdf); [Apple Support, 2025](https://support.apple.com/en-in/108790); [Železnik Mežan, 2025](https://doi.org/10.3389/fspor.2025.1707991))

## Runner exception

Some runners using the same device, similar outdoor routes, and consistent training conditions may get directionally useful feedback from wearable VO₂ max. The Garmin studies support that a structured running-based estimate can be reasonably close in selected healthy or athletic samples, especially when paired with a chest strap. ([Carrier et al., 2023](https://doi.org/10.3390/technologies11030071); [Carrier et al., 2025](https://doi.org/10.3390/s25010275))

That does not justify inclusion as a general metric. The evidence is device-specific, protocol-specific, and population-specific. It does not establish that a generic exported `VO2_max` field is valid across brands, algorithms, sports, ages, clinical states, heart rhythms, medications, heat exposure, terrain, or sensor configurations. Recent review authors specifically call for larger, more heterogeneous studies and better testing across real-world environmental conditions. ([Železnik Mežan, 2025](https://doi.org/10.3389/fspor.2025.1707991))

## Marketing inflation

The marketed label is "VO₂ max," "cardio fitness," or "cardiorespiratory fitness." Apple Support describes Cardio Fitness as a measurement of VO₂ max while also stating that Apple Watch gives a cardio fitness estimate based on how hard the heart is working during outdoor workouts. ([Apple Support, 2025](https://support.apple.com/en-in/108790))

The sensor-supported claim is narrower: "a proprietary estimate of laboratory VO₂ max inferred from heart-rate and movement patterns during qualifying exercise, with device-specific error and context-dependent validity." Apple’s technical documentation and independent validation studies support that narrower framing. ([Apple, 2021](https://www.apple.com/healthcare/docs/site/Using_Apple_Watch_to_Estimate_Cardio_Fitness_with_VO2_max.pdf); [Molina-Garcia et al., 2022](https://doi.org/10.1007/s40279-021-01639-y); [Železnik Mežan, 2025](https://doi.org/10.3389/fspor.2025.1707991))

Those are not the same claim. The first reads like a physiological measurement. The second is a conditional model output.

## Funding and conflict-of-interest check

The 2022 meta-analysis was produced through the INTERLIVE consortium and was partly funded by Huawei Technologies Oy, although the authors declared no conflicts of interest. That funding connection should be considered when weighing the review, especially because the review concerns wearable-device validation. ([Molina-Garcia et al., 2022](https://doi.org/10.1007/s40279-021-01639-y); [INTERLIVE network funding statement](https://profith.ugr.es/en/networks/towards-intelligent-health-and-well-being-network-of-physical-activity-assessment/))

The 2025 PLOS One Apple Watch validation reported non-industry funding from Science Foundation Ireland’s National Challenge Fund, stated that the funder had no role in the trial, and reported no competing interests. ([Lambe et al., 2025](https://doi.org/10.1371/journal.pone.0323741))

The 2024 JMIR Apple Watch Series 7 validation declared no conflicts of interest. ([Caserman et al., 2024](https://doi.org/10.2196/59459))

The 2023 Garmin fēnix 6 athlete study reported no external funding, and the 2025 Garmin fēnix 6 study reported no external funding and no conflicts of interest. Those findings are useful but should not be generalized beyond their tested devices, protocols, and populations. ([Carrier et al., 2023](https://doi.org/10.3390/technologies11030071); [Carrier et al., 2025](https://doi.org/10.3390/s25010275))

Apple documentation is cited here only for how the company describes the metric and qualifying conditions, not as independent validation. ([Apple, 2021](https://www.apple.com/healthcare/docs/site/Using_Apple_Watch_to_Estimate_Cardio_Fitness_with_VO2_max.pdf); [Apple Support, 2025](https://support.apple.com/en-in/108790))

## Quick reference values

- Systematic review/meta-analysis: resting-condition wearable algorithms overestimated VO₂ max by 2.17 mL/kg/min, with limits of agreement from -13.07 to 17.41 mL/kg/min. ([Molina-Garcia et al., 2022](https://doi.org/10.1007/s40279-021-01639-y))

- Systematic review/meta-analysis: exercise-based algorithms had lower mean bias, -0.09 mL/kg/min, but still had limits of agreement from -9.92 to 9.74 mL/kg/min. ([Molina-Garcia et al., 2022](https://doi.org/10.1007/s40279-021-01639-y))

- Apple Watch Series 7 validation: MAPE 15.79 percent; ICC 0.47; overestimation in lower-fitness users and underestimation in higher-fitness users, with small subgroup sizes. ([Caserman et al., 2024](https://doi.org/10.2196/59459))

- Apple Watch PLOS One validation: mean underestimation 6.07 mL/kg/min; MAPE 13.31 percent; limits of agreement from -6.11 to 18.26 mL/kg/min. ([Lambe et al., 2025](https://doi.org/10.1371/journal.pone.0323741))

- Apple Watch Series 10 validation: limits of agreement from -18.23 to 5.73 mL/kg/min; mean absolute error 6.79 mL/kg/min. ([Lambe et al., 2026](https://doi.org/10.1016/j.mcpdig.2026.100357))

- Garmin fēnix 6 athlete study: MAPE 6.85 percent and concordance correlation 0.70, but the result should not be extrapolated to other devices or the general population. ([Carrier et al., 2023](https://doi.org/10.3390/technologies11030071))

- Garmin fēnix 6 healthy-adult study: 30-second laboratory comparison MAPE 7.05 percent and concordance correlation 0.73, using a Garmin HRM-Run chest monitor and controlled outdoor running protocol. ([Carrier et al., 2025](https://doi.org/10.3390/s25010275))


## Practical interpretation

- **For stripped health-data exports:** exclude wearable VO₂ max.

- **For absolute fitness classification:** exclude.

- **For clinical interpretation:** exclude.

- **For trend tracking in exported datasets:** exclude.

- **For a runner’s private training curiosity:** it may be worth glancing at only when the same device, same sensor setup, and similar routes are used over long periods, but that is not strong enough for inclusion as a health metric. ([Carrier et al., 2023](https://doi.org/10.3390/technologies11030071); [Carrier et al., 2025](https://doi.org/10.3390/s25010275))


## References

- [Molina-Garcia P, Notbohm HL, Schumann M, Argent R, Hetherington-Rauth M, Stang J, Bloch W, Cheng S, Ekelund U, Sardinha LB, Caulfield B, Brønd JC, Grøntved A, Ortega FB. Validity of Estimating the Maximal Oxygen Consumption by Consumer Wearables: A Systematic Review with Meta-analysis and Expert Statement of the INTERLIVE Network. _Sports Medicine._ 2022;52(7):1577-1597.](https://doi.org/10.1007/s40279-021-01639-y) DOI: [10.1007/s40279-021-01639-y](https://doi.org/10.1007/s40279-021-01639-y). PMID: 35072942.

- [Železnik Mežan L. Accuracy of wearables for determining the maximal oxygen uptake and lactate threshold: a qualitative systematic review. _Frontiers in Sports and Active Living._ 2025;7:1707991.](https://doi.org/10.3389/fspor.2025.1707991) DOI: [10.3389/fspor.2025.1707991](https://doi.org/10.3389/fspor.2025.1707991).

- [Caserman P, Yum S, Göbel S, Reif A, Matura S. Assessing the Accuracy of Smartwatch-Based Estimation of Maximum Oxygen Uptake Using the Apple Watch Series 7: Validation Study. _JMIR Biomedical Engineering._ 2024;9:e59459.](https://doi.org/10.2196/59459) DOI: [10.2196/59459](https://doi.org/10.2196/59459). PMID: 39083800.

- [Lambe R, O’Grady B, Baldwin M, Doherty C. Investigating the accuracy of Apple Watch VO₂ max measurements: A validation study. _PLOS One._ 2025;20(5):e0323741.](https://doi.org/10.1371/journal.pone.0323741) DOI: [10.1371/journal.pone.0323741](https://doi.org/10.1371/journal.pone.0323741). PMID: 40373042.

- [Lambe R, Schumann M, Donnelly L, Hamilton S, Lally S, Rafter E, O’Reilly S, White T, Doherty C. Accuracy of VO2 max Estimates From Apple Watch Series 10. _Mayo Clinic Proceedings: Digital Health._ 2026;4(2):100357.](https://doi.org/10.1016/j.mcpdig.2026.100357) DOI: [10.1016/j.mcpdig.2026.100357](https://doi.org/10.1016/j.mcpdig.2026.100357).

- [Carrier B, Helm MM, Cruz K, Barrios B, Navalta JW. Validation of Aerobic Capacity (VO₂max) and Lactate Threshold in Wearable Technology for Athletic Populations. _Technologies._ 2023;11(3):71.](https://doi.org/10.3390/technologies11030071) DOI: [10.3390/technologies11030071](https://doi.org/10.3390/technologies11030071).

- [Carrier B, Marten Chaves S, Navalta JW. Validation of Aerobic Capacity (VO₂max) and Pulse Oximetry in Wearable Technology. _Sensors._ 2025;25(1):275.](https://doi.org/10.3390/s25010275) DOI: [10.3390/s25010275](https://doi.org/10.3390/s25010275).

- [Spathis D, Perez-Pozuelo I, Gonzales TI, Wu Y, Brage S, Wareham N, Mascolo C. Longitudinal cardio-respiratory fitness prediction through wearables in free-living environments. _npj Digital Medicine._ 2022;5:176.](https://doi.org/10.1038/s41746-022-00719-1) DOI: [10.1038/s41746-022-00719-1](https://doi.org/10.1038/s41746-022-00719-1). PMID: 36460766.

- [Apple Inc. Using Apple Watch to Estimate Cardio Fitness with VO2 max. Apple; May 2021.](https://www.apple.com/healthcare/docs/site/Using_Apple_Watch_to_Estimate_Cardio_Fitness_with_VO2_max.pdf)

- [Apple Support. Track your cardio fitness levels. Published November 10, 2025.](https://support.apple.com/en-in/108790)

- [Towards Intelligent Health and Well-Being Network of Physical Activity Assessment. Funding statement.](https://profith.ugr.es/en/networks/towards-intelligent-health-and-well-being-network-of-physical-activity-assessment/)