# Should You Trust Wearable Calorie Estimates?

Wearable calorie estimates should **not** be trusted for nutrition decisions. The export-safe verdict is: **include step-count trends for broad activity tracking; exclude wearable calorie-burn estimates.** Step counts are closer to a direct movement signal and can be useful for coarse activity tracking in normal gait, while wearable calorie estimates are indirect model outputs with errors that are too large and context-dependent for food-intake decisions. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/); [Chevance et al., 2022](https://mhealth.jmir.org/2022/4/e35626); [Mora-Gonzalez et al., 2022](https://doi.org/10.1186/s12966-022-01350-9))

## Metric verdicts

|Metric|Verdict|Why|
|---|--:|---|
|Step count, used as a coarse activity trend|**Include**|The measurement is relatively direct, and validation studies support acceptable performance during normal gait for many devices, while still showing limitations by setting, speed, and device location. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/); [Mora-Gonzalez et al., 2022](https://doi.org/10.1186/s12966-022-01350-9))|
|Step count, used as precise gait truth or activity dose in slow walking contexts|**Exclude**|Accuracy degrades substantially at slow speeds, with wrist placement performing worse than ankle, thigh, or waist placement. ([Mora-Gonzalez et al., 2022](https://doi.org/10.1186/s12966-022-01350-9); [Ngueleu et al., 2022](https://doi.org/10.1186/s12984-022-01085-5))|
|Workout calories / active calories / calories burned|**Exclude**|The device does not directly measure energy expenditure; it estimates it through model-based calculations, and validation errors are too large and context-dependent. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/); [Chevance et al., 2022](https://mhealth.jmir.org/2022/4/e35626); [Argent et al., 2022](https://doi.org/10.1007/s40279-022-01665-4))|
|Calorie-burn trend over time|**Exclude**|The validation evidence does not justify exporting it as a trusted trend metric. Estimates remain device-, activity-, age-, and model-dependent, and consumer algorithms can change over time. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/); [Chevance et al., 2022](https://mhealth.jmir.org/2022/4/e35626); [Argent et al., 2022](https://doi.org/10.1007/s40279-022-01665-4))|
|“I burned X calories, so I can eat X more”|**Exclude**|This converts an unreliable device estimate into a nutrition decision with false precision. ([Chevance et al., 2022](https://mhealth.jmir.org/2022/4/e35626); [Porter et al., 2025](https://doi.org/10.1017/jns.2024.99))|

## What wearables measure directly

Step counting is a motion-detection problem. The device is trying to identify repeated walking-like movements and convert them into a count. That is not perfect, but it is close to the sensor's native signal: accelerometers detect movement, and step-count validation studies can compare the result against directly observed steps. In the CADENCE-Adults validation study, 258 adults wore 21 devices across treadmill speeds and wear locations; at normal speeds, 15 devices performed at under 5% mean absolute percentage error, while slow walking produced much worse accuracy across all devices. ([Mora-Gonzalez et al., 2022](https://doi.org/10.1186/s12966-022-01350-9))

Energy expenditure is a different class of claim. Consumer wearables commonly estimate energy expenditure from user demographics and on-board sensors such as accelerometers and photoplethysmography-derived heart-rate signals. Criterion methods for measuring or validating energy expenditure include indirect calorimetry, direct calorimetry, and doubly labeled water; consumer wrist devices do not directly measure those criterion signals. ([Argent et al., 2022](https://doi.org/10.1007/s40279-022-01665-4))

That does not mean every calorie estimate is random. It means the displayed calorie value is a model output whose validity depends on the target population, intended output, device, activity type, testing condition, and data processing. ([Argent et al., 2022](https://doi.org/10.1007/s40279-022-01665-4); [Chevance et al., 2022](https://mhealth.jmir.org/2022/4/e35626))

## Why steps survive and calories fail

Step count is defensible when the use case is coarse: “Was today more active than yesterday?” or “Did I walk roughly 4,000 versus 10,000 steps?” A 2020 systematic review of 158 publications found that step-count validity was better in controlled laboratory settings than in free-living settings, and that Apple and Samsung had the highest validity for step count among the brands assessed. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/))

The same review found that **no brand fell within acceptable accuracy limits for energy expenditure**. That is the key distinction: the step number can be useful despite moderate error because the behavioral use case is broad; the calorie number is often used as if it were a precise metabolic measurement. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/))

Step count still has a boundary. In CADENCE-Adults, average accuracy was compromised at slow walking speeds, with mean absolute percentage error around 40% across slow speeds, compared with 7% across normal speeds. Wrist placement also performed worse than ankle, thigh, or waist placement at normal speeds. A separate systematic review of ActiGraph devices concluded that step-count validity was good only under specific conditions related to walking speed, device position, and data processing. ([Mora-Gonzalez et al., 2022](https://doi.org/10.1186/s12966-022-01350-9); [Ngueleu et al., 2022](https://doi.org/10.1186/s12984-022-01085-5))

## What validation studies show for calorie estimates

A 2022 systematic review and Bland-Altman meta-analysis of recent combined-sensing Fitbit devices included 52 studies, with 41 studies in the meta-analysis and 203 comparisons against criterion measures. After removing high-risk-of-bias studies, Fitbit energy expenditure was underestimated by an average of 2.77 kcal/min, with population limits of agreement from about -12.75 to +7.41 kcal/min. That range is far too wide for nutrition decisions. ([Chevance et al., 2022](https://mhealth.jmir.org/2022/4/e35626))

The same Fitbit review found that most included studies were laboratory protocols rather than free-living studies, most participants were young and without chronic disease, and only 15% of included studies enrolled participants older than 65. That weakens generalization to the populations most likely to rely on automated health metrics. ([Chevance et al., 2022](https://mhealth.jmir.org/2022/4/e35626))

A broader 2020 systematic review of commercial wearables reached the same practical conclusion: no assessed brand met acceptable accuracy limits for energy expenditure. The review also noted that many devices in validation studies become outdated quickly, which matters because consumer algorithms and hardware change over time. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/))

A systematic review and meta-analysis of activity monitors likewise found that energy-expenditure accuracy depended on device location, activity type, and sensing approach. Adding physiological sensors can improve estimates, but it does not make the output equivalent to a direct energy-expenditure measurement. ([O'Driscoll et al., 2020](https://doi.org/10.1136/bjsports-2018-099643); [Argent et al., 2022](https://doi.org/10.1007/s40279-022-01665-4))

Newer device-specific studies do not rescue the metric. A 2025 PLOS One study in 20 untrained Chinese women compared four low-cost smartwatches against indirect calorimetry during cycling and found device-specific mean absolute percentage errors ranging from 12.5-18.6% for one Huawei device to 49.5-57.4% for the KEEP device. The authors reported significant overestimation for some devices and advised caution for energy-balance management. ([Liu et al., 2025](https://doi.org/10.1371/journal.pone.0331399))

A 2026 lab study comparing Apple, Galaxy, Fitbit, and Garmin watches against indirect calorimetry found limited energy-expenditure accuracy across all devices. Endurance-exercise energy expenditure was consistently underestimated with wide limits of agreement, and resistance-exercise energy expenditure showed weak correlations with indirect calorimetry and poor reliability. This study was supported by SOLUM Health Care, and one author was employed by SOLUM, so it should be interpreted with that conflict in mind; the direction of the result still aligns with independent reviews showing poor energy-expenditure validity. ([Lee et al., 2026](https://doi.org/10.3390/s26082526); [Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/))

## The false-precision problem

A display like “487 calories” presents an exact integer. The validation literature does not support treating that integer as a precise metabolic measurement. When a metric has limits of agreement wide enough to span large portions of a workout's total expenditure, displaying a calorie value without visible uncertainty manufactures confidence the measurement does not deserve. ([Chevance et al., 2022](https://mhealth.jmir.org/2022/4/e35626))

This is worse in exported data. A human user might remember that wearable calories are “rough,” but a downstream system consuming a column called `calories_burned` may treat it as a measured truth. The correct export-safe verdict is therefore **exclude**, not “use with caution.”

## The behavioral argument does not save the calorie number

The best argument for showing wearable calories is behavioral: even if the number is wrong, maybe it motivates more activity. That argument fails as a validation standard. A number can be motivating and still be too inaccurate to guide food intake.

The behavioral evidence also cuts in the opposite direction. A 2025 scoping review of eating after exercise found that framing exercise as burning more calories, burning fat, or being hard work can increase post-exercise licensing and greater intake from energy-dense foods. The same review notes that smartwatches often display absolute exercise calories rather than only the additional calories above rest, which may encourage overconsumption after exercise. ([Porter et al., 2025](https://doi.org/10.1017/jns.2024.99))

Acute exercise does not automatically require immediate calorie replacement. The same review summarizes prior evidence that a bout of exercise does not necessarily cause a compensatory increase in energy intake, which means “eat back the watch calories” is not a physiologic rule. ([Porter et al., 2025](https://doi.org/10.1017/jns.2024.99))

## The narrower claim wearables can support

Wearables can support the narrow claim: “This was probably a more active day than usual,” especially when the signal is step count or movement volume. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/); [Mora-Gonzalez et al., 2022](https://doi.org/10.1186/s12966-022-01350-9))

They cannot support the broader claim: “You burned exactly 487 calories and can adjust your food intake by that amount.” ([Chevance et al., 2022](https://mhealth.jmir.org/2022/4/e35626); [Porter et al., 2025](https://doi.org/10.1017/jns.2024.99))

That is the inflation gap. Step count is a behavior-tracking metric. Wearable calorie burn is a proprietary metabolic estimate presented as if it were a measurement.

## Practical interpretation

- Use step counts to track broad activity patterns, not precise energy expenditure. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/); [Mora-Gonzalez et al., 2022](https://doi.org/10.1186/s12966-022-01350-9))

- Do not use wearable calorie estimates to set calorie intake, calculate deficits, or decide how much extra to eat after exercise. ([Chevance et al., 2022](https://mhealth.jmir.org/2022/4/e35626); [Porter et al., 2025](https://doi.org/10.1017/jns.2024.99))

- Do not export `calories_burned`, `active_calories`, or `workout_calories` as trusted health metrics. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/); [Chevance et al., 2022](https://mhealth.jmir.org/2022/4/e35626))

- Rename defensible step outputs as trend metrics when possible, such as `step_count_trend`, not as proxies for calories or metabolic load. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/); [Mora-Gonzalez et al., 2022](https://doi.org/10.1186/s12966-022-01350-9))

- A harder workout showing a higher calorie number may be directionally intuitive, but that does not make the number valid enough for nutrition decisions. ([Argent et al., 2022](https://doi.org/10.1007/s40279-022-01665-4); [Chevance et al., 2022](https://mhealth.jmir.org/2022/4/e35626))


## Bottom line

**Trust wearable step counts for coarse activity tracking. Do not trust wearable calorie estimates for nutrition decisions.**

The calorie number is not just imperfect; it is the wrong kind of metric for downstream use. It is indirect, model-based, activity-dependent, population-dependent, and displayed with a precision the evidence does not support. ([Fuller et al., 2020](https://mhealth.jmir.org/2020/9/e18694/); [Chevance et al., 2022](https://mhealth.jmir.org/2022/4/e35626); [Argent et al., 2022](https://doi.org/10.1007/s40279-022-01665-4))

## References

- Fuller D, Colwell E, Low J, Orychock K, Tobin MA, Simango B, Buote R, Van Heerden D, Luan H, Cullen K, Slade L, Taylor NGA. [Reliability and Validity of Commercially Available Wearable Devices for Measuring Steps, Energy Expenditure, and Heart Rate: Systematic Review](https://mhealth.jmir.org/2020/9/e18694/). _JMIR Mhealth Uhealth_. 2020;8(9):e18694. DOI: [10.2196/18694](https://doi.org/10.2196/18694). PMID: [32897239](https://pubmed.ncbi.nlm.nih.gov/32897239/). Funding note: funded by Dr Fuller's Canada Research Chair; one author was employed by Garmin during the publication process after completion of the paper.

- Chevance G, Golaszewski NM, Tipton E, Hekler EB, Buman M, Welk GJ, Patrick K, Godino JG. [Accuracy and Precision of Energy Expenditure, Heart Rate, and Steps Measured by Combined-Sensing Fitbits Against Reference Measures: Systematic Review and Meta-analysis](https://mhealth.jmir.org/2022/4/e35626). _JMIR Mhealth Uhealth_. 2022;10(4):e35626. DOI: [10.2196/35626](https://doi.org/10.2196/35626). PMID: [35416777](https://pubmed.ncbi.nlm.nih.gov/35416777/). No conflicts declared.

- O'Driscoll R, Turicchi J, Beaulieu K, Scott S, Matu J, Deighton K, Finlayson G, Stubbs J. [How well do activity monitors estimate energy expenditure? A systematic review and meta-analysis of the validity of current technologies](https://doi.org/10.1136/bjsports-2018-099643). _British Journal of Sports Medicine_. 2020;54(6):332-340. DOI: [10.1136/bjsports-2018-099643](https://doi.org/10.1136/bjsports-2018-099643). PMID: [30194221](https://pubmed.ncbi.nlm.nih.gov/30194221/).

- Argent R, Hetherington-Rauth M, Stang J, Tarp J, Ortega FB, Molina-Garcia P, Schumann M, Bloch W, Cheng S, Grontved A, Brond JC, Ekelund U, Sardinha LB, Caulfield B. [Recommendations for Determining the Validity of Consumer Wearables and Smartphones for the Estimation of Energy Expenditure: Expert Statement and Checklist of the INTERLIVE Network](https://doi.org/10.1007/s40279-022-01665-4). _Sports Medicine_. 2022;52:1817-1832. DOI: [10.1007/s40279-022-01665-4](https://doi.org/10.1007/s40279-022-01665-4). Conflict note: INTERLIVE included one industrial partner, Huawei Technologies Finland.

- Mora-Gonzalez J, Gould ZR, Moore CC, Aguiar EJ, Ducharme SW, Schuna JM Jr, Barreira TV, Staudenmayer J, McAvoy CR, Boikova M, Miller TA, Tudor-Locke C. [A catalog of validity indices for step counting wearable technologies during treadmill walking: the CADENCE-Adults study](https://doi.org/10.1186/s12966-022-01350-9). _International Journal of Behavioral Nutrition and Physical Activity_. 2022;19:117. DOI: [10.1186/s12966-022-01350-9](https://doi.org/10.1186/s12966-022-01350-9). Funding note: NIH/NIA grant support; funder had no role.

- Ngueleu AM, Barthod C, Best KL, Routhier F, Otis M, Batcho CS. [Criterion validity of ActiGraph monitoring devices for step counting and distance measurement in adults and older adults: a systematic review](https://doi.org/10.1186/s12984-022-01085-5). _Journal of NeuroEngineering and Rehabilitation_. 2022;19:112. DOI: [10.1186/s12984-022-01085-5](https://doi.org/10.1186/s12984-022-01085-5). Funding listed as not applicable; authors declared no conflict of interest.

- Liu Y, Liu F, Yu W, Xiao Y, Liu D, Li Z, Chen W, Gao F, Le S. [Validity of four low-cost smartwatches in estimating energy expenditure during cycling in Chinese untrained women](https://doi.org/10.1371/journal.pone.0331399). _PLOS One_. 2025;20(9):e0331399. DOI: [10.1371/journal.pone.0331399](https://doi.org/10.1371/journal.pone.0331399). Funding note: supported by public research grants; funders had no role; authors declared no competing interests.

- Lee T-H, Jun D-U, Bae J-Y, Roh H-T, Cho S-Y. [Comparative Validity of Smartwatch-Derived Heart Rate and Energy Expenditure During Endurance and Resistance Exercise](https://doi.org/10.3390/s26082526). _Sensors_. 2026;26(8):2526. DOI: [10.3390/s26082526](https://doi.org/10.3390/s26082526). Conflict note: supported by SOLUM Health Care; one author was employed by SOLUM.

- Porter A, Jago R, Robles LA, Cawley E, Rogers PJ, Ferriday D, Brunstrom JM. [Investigating the psychology of eating after exercise - a scoping review](https://doi.org/10.1017/jns.2024.99). _Journal of Nutritional Science_. 2025;14:e12. DOI: [10.1017/jns.2024.99](https://doi.org/10.1017/jns.2024.99). Funding note: NIHR Bristol Biomedical Research Centre; authors declared no competing interests.